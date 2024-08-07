# Essa aplicação é preparada para o firebase.
import os
from firebase_admin import credentials, initialize_app, db
import pyrebase
import dotenv

dotenv.load_dotenv("./models/Config.env")

def initialize_firebase():
    config = {
        "type": os.getenv("type"),
        "project_id": os.getenv("project_id"),
        "private_key_id": os.getenv("private_key_id"),
        "private_key": os.getenv("private_key"),
        "client_email": os.getenv("client_email"),
        "client_id": os.getenv("client_id"),
        "auth_uri": os.getenv("auth_uri"),
        "token_uri": os.getenv("token_uri"),
        "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url"),
        "client_x509_cert_url": os.getenv("client_x509_cert_url"),
        "universe_domain": os.getenv("universe_domain"),
        "apiKey": os.getenv("apiKey"),
        "authDomain": os.getenv("authDomain"),
        "databaseURL": os.getenv("databaseURL"),
        "projectId": os.getenv("projectId"),
        "storageBucket": os.getenv("storageBucket"),
        "messagingSenderId":os.getenv("messagingSenderId"),
        "appId": os.getenv("appId")
    }
    cred = credentials.Certificate(config)
    initialize_app(cred, {'databaseURL': config['databaseURL']})

    pyrebase_config = {
        "apiKey": config["apiKey"],
        "authDomain": config["authDomain"],
        "databaseURL": config["databaseURL"],
        "storageBucket": config["storageBucket"],
        "messagingSenderId": config["messagingSenderId"],
        "appId": config["appId"]
    }
    firebase = pyrebase.initialize_app(pyrebase_config)

    return firebase

def get(reference):
    ref = db.reference(reference)
    if ref is None:
        raise ValueError
    return ref.get()

def update(reference, data):
    try:
        ref = db.reference(reference)
        ref.set(data)
    except Exception as e:
        print(e)