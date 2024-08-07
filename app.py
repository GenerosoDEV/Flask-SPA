from flask import Flask
from models.firebase_service import FirebaseService
from waitress import serve
import os, importlib, dotenv

dotenv.load_dotenv()

ignored_routes = ["/static"]
def checkConflicts(blueprint):
    temp_app = Flask(__name__)
    temp_app.register_blueprint(blueprint)
    blueprint_routes = []
    rules = temp_app.url_map.iter_rules()
    for rule in rules:
        for ignored_route in ignored_routes:
            if not rule.rule.startswith(ignored_route):
                blueprint_routes.append(rule.rule)

    app_routes = []
    app_rules = app.url_map.iter_rules()
    for rule in app_rules:
        app_routes.append(rule.rule)

    conflicts_routes = []
    for route in blueprint_routes:
        if route in app_routes:
            conflicts_routes.append(route)
            
    if conflicts_routes != []:
        return (True, conflicts_routes)
    else:
        return (False, [])

def loadFolder(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py') and file not in ['example.py', '__init__.py']:
                module_path = os.path.join(root, file)
                module_name = os.path.relpath(module_path, path).replace(os.sep, '.')
                module_name = os.path.splitext(module_name)[0]

                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, 'blueprint'):
                    blueprint = getattr(module, 'blueprint')
                    conflicts = checkConflicts(blueprint)
                    if conflicts[0]:
                        print(f"{blueprint.name} não pode ser carregado, pois tem rotas já existentes: {conflicts[1]}")
                    else:
                        app.register_blueprint(blueprint)


app = Flask(__name__)

loadFolder(os.path.join(os.path.dirname(__file__), 'views'))
loadFolder(os.path.join(os.path.dirname(__file__), 'controllers'))

if __name__ == "__main__":
    if os.getenv("DEBUG"):
        app.run(host=os.getenv("IP"), port=os.getenv("PORT"), debug=True)
    else:
        try:
            print("Aplicação iniciada.")
            serve(app, host=os.getenv("IP"), port=os.getenv("PORT"))
        except Exception as e:
            print(f"Não foi possível iniciar. Erro: {e}")