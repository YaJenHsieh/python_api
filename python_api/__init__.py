from flask import Flask
from python_api.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from python_api import route
