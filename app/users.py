from flask import Blueprint

hello_blueprint = Blueprint('fir_blueprint', __name__)


@hello_blueprint.route('/hello')
def hello():
    return 'hello'
