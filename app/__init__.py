from flask import Flask

def create_app():
    app = Flask(__name__)

    from .bot import bp as bot_bp
    app.register_blueprint(bot_bp)

    return app
