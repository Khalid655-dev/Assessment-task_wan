
from flask import Flask
from sqlalchemy import false
from flask_sqlalchemy import SQLAlchemy

# Defining app insatnce Using Flask Class
app = Flask(__name__)
# Secret Key for Token
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'
# Postgres Database Connection string the password and other credentials are used here which us not a good practice
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin655@localhost/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false
# creating database object using SQLALchemy ORM
db = SQLAlchemy(app)

from api.cars import cars_blueprint
from api.users import users_blueprint
# Registering the Blueprints
app.register_blueprint(cars_blueprint)
app.register_blueprint(users_blueprint)


if  __name__ == '__main__':
     # creates the database tables if it is not created 
     db.create_all() 
     app.run()
