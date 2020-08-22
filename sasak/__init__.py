from flask import Flask

def create_app(config: str = "config.DevelopmentConfig"):
    app: Flask = Flask(__name__)

    app.config.from_object(config)

    with app.app_context():
        from . import sasak

        app.register_blueprint(sasak.blueprint)

    return app
