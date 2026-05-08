from flask import Flask

from .routes import bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        MAX_CONTENT_LENGTH=2 * 1024 * 1024,
    )

    if test_config is not None:
        app.config.update(test_config)

    app.register_blueprint(bp)
    return app
