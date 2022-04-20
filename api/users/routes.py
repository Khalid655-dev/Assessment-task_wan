from flask import request, jsonify, make_response
from itsdangerous import Serializer
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from flask import request
import models
from api.users import users_blueprint
from .schemas import UserSchema
from app import db
from app import app


@users_blueprint.route('/register', methods=['POST'])
def signup_user():  
   data = request.get_json()

   # To generate a hashed password using the password provided 
   hashed_password = generate_password_hash(data['password'], method='sha256')
   # new sholuld provide name and password
   new_user = models.User(name=data['name'], password=hashed_password)
   db.session.add(new_user) 
   db.session.commit()
   # Utilising UsersSchema to validate the input data
   serializer=UserSchema()

   #Serializing the data to JSON format
   data=serializer.dump(new_user)
   return jsonify(
        data
    ),201


@users_blueprint.route('/login', methods=['POST'])  
def login_user(): 
    auth = request.authorization   

    if not auth or not auth.username or not auth.password:  
        return make_response('could not verify', 401, {'Authentication': 'login required"'})    
     
    # To Query the user table for the name column
    user = models.User.query.filter_by(name=auth.username).first()   
    # Comparing the user password and hashed password 
    if check_password_hash(user.password, auth.password):
        # Based on the name of the user a Token will be generated which will be valid for 45 minutes
        token = jwt.encode({'name' : user.name, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, app.config['SECRET_KEY'], "HS256")
        return token 

    return make_response('could not verify',  401, {'Authentication': '"login required"'})