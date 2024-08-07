import models.database as db
import os
from flask import Blueprint, render_template

blueprint = Blueprint(os.path.basename(__file__).replace(".py", ""), __name__)

@blueprint.route('/example', methods=["POST", "PUT", "DELETE"])
def example():
    return render_template("example.html")