from flask import Flask, Blueprint
from api.repository import engine, Base

main = Blueprint('main', __name__)

from api import routes


def init_app():
    app = Flask(__name__)
    Base.metadata.create_all(bind=engine)

    app.register_blueprint(main)

    return app
