from flask import Flask
from flask_cors import CORS

from routes.dashboard import dashboard_bp
from routes.events import events_bp
from routes.offers import offers_bp
from routes.traffic import traffic_bp
from routes.transit import transit_bp


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(traffic_bp)
    app.register_blueprint(transit_bp)
    app.register_blueprint(offers_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
