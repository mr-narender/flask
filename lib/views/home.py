from flask import Blueprint, render_template

from lib.helper import db

blueprint = Blueprint("home", __name__)


@blueprint.route("/")
def index():
    # creating the customer collection
    messages = db().find({"hello": "world"})
    return render_template("index.html", messages=messages)


@blueprint.route("/about")
def about():
    return "All about Flask"
