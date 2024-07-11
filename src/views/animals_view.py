from flask import Blueprint, render_template

animals_blueprint = Blueprint("animals_view", __name__)

@animals_blueprint.route("/animals")
def animals():
    return render_template("animals.html")