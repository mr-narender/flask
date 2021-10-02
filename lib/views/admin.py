from flask import Blueprint

blueprint = Blueprint("admin", __name__)


@blueprint.route("/dashboard")
def dashboard():
    return "Admin dashboard"
