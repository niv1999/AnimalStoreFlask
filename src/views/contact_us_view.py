from flask import Blueprint, render_template

contact_us_blueprint = Blueprint("contact_us_view", __name__)

@contact_us_blueprint.route("/contact-us")
def contact_us():
    return render_template("contact_us.html")