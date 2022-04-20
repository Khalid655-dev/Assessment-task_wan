from api.cars import cars_blueprint
from api.utils import token_required
from flask import request, jsonify
import models


@cars_blueprint.route('/cars', methods=['GET'])
@token_required
def get_car(current_user):
   # Providing the default data for querying the database based on year, make and model
   
   year = request.args.get('year', 2012, type=int)
   make = request.args.get('make', "BMW", type=str)
   model = request.args.get('model', "X3", type=str)
   
   # Querying the cars table for year, make and model and the first match will be retrived
   car = models.Car.query.filter_by(year= year, make= make, model= model).first()
   #pag= Cars.query.filter_by(model=Cars.model, make=Cars.make, year=Cars.year).paginate(page=page, per_page=3)
   if not car:  
       return jsonify({'message': 'Car with model, make and year does not exist'})
   

   return car.to_json()

