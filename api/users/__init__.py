from flask import Blueprint

# Defing blueprint for users routes
users_blueprint = Blueprint("users", __name__)
# impring the user routes from the current directory 
from . import routes