from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.register_blueprint(chat)
    return app    
# from flask import Blueprint

# chat = Blueprint('chat',__name__)

# @chat.route('/hello')
# def hello():
#     return "hello world"