from dotenv import load_dotenv

load_dotenv(verbose=True)
from flask import Flask, Response
from flask_cors import CORS
from instance.config import APP_CONFIG
from takehome_api.src.database import db

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(APP_CONFIG[config_name])
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return str(Response.default_status) + " OK"

    # TODO:
    # Add an appointment endpoint

    return app
