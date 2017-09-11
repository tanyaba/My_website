from flask import Blueprint

majority = Blueprint('majority', __name__, )
from . import routes

