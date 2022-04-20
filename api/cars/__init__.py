from flask import Blueprint

# Defining Blueprint for cars routes
cars_blueprint = Blueprint("cars", __name__)
# importing the cars routes from the current directory
from . import routes