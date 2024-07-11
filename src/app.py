from flask import Flask
from views.home_view import home_blueprint
from views.animals_view import animals_blueprint
from views.contact_us_view import contact_us_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(animals_blueprint)
app.register_blueprint(contact_us_blueprint)