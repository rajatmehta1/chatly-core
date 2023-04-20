from flask import Blueprint

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/hello')
def hello():
    return "hello world"