# The purpose of this file is to construct an application package to call factory functions
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_login import LoginManager
from config import config
from flask_pagedown import PageDown

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .second_transaction import transaction as transaction_blueprint
    app.register_blueprint(transaction_blueprint, url_prefix='/transaction')

    from .recruitment import recruitment as recruitment_blueprint
    app.register_blueprint(recruitment_blueprint, url_prefix='/recruitment')

    return app
