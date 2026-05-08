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

    @app.after_request
    def add_no_cache_headers(response):
        # Always fetch a fresh page so previous rendered markdown is not reused.
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response

    return app
