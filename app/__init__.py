from .users import hello_blueprint
from flask import Flask

app = Flask(__name__)

app.register_blueprint(hello_blueprint)
