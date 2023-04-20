from flask import Flask
from chat import chat

app = Flask(__name__)
app.register_blueprint(chat.chat_bp)

if __name__=='__main__':
    app.run()