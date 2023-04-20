from chat import chat

app = chat.create_app()

if __name__=='__main__':
    app.run()