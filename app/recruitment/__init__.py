from flask import Blueprint

recruitment = Blueprint('recruitment', __name__)

from . import views