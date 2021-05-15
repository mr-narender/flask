from flask import Flask

app = Flask(__name__)

from lib import views
from lib import admin_views
