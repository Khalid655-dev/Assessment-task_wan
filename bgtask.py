
from models import Car
from flask import abort
import json
import requests
from app import db

# Defining our Class daata to mapped into the back4app.com data
class CarData:
    def __init__(self, object_id, make, model, year, category, created_at, updated_at):
        self.object_id = object_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category
        self.created_at = created_at
        self.updated_at = updated_at
     # using the method for the above class to mape the daata into our own cars tables data
    @classmethod
    def parse_from_back4app(cls, data):
        return CarData(object_id=data.get("objectId"), make=data.get("Make"), model=data.get("Model"),
                       category=data.get("Category"), created_at=data.get("createdAt"),
                       updated_at=data.get("updatedAt"),
                       year=data.get("Year"))
     # Defining the function to converd the data into JSON format
    def to_json(self):
        return {
            "object_id": self.object_id,
            "make": self.make,
            "model": self.model,
            "category": self.category,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "year": self.year,
        }
        

# Defined a list for Back4app database classes
CLASSES_LIST = [
    'Car_Model_List',
    'Car_Model_List_Acura'
]


headers = {
    'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z',
    'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW'
}

back4app_data = {
    "objectId": "ZRgPP9dBMm",
    "Year": 2020,
    "Make": "Audi",
    "Model": "Q3",
    "Category": "SUV",
    "createdAt": "2020-01-27T20:44:17.665Z",
    "updatedAt": "2020-01-27T20:44:17.665Z",
}
# Using the Back4app.com API code to extarct and print the data by giving specific class name in the URL, here only the class name is changing
object_list = []
for class_ in CLASSES_LIST:
    url = f'https://parseapi.back4app.com/classes/Car_Model_List?count=1&limit=10&excludeKeys=Category'
    data = json.loads(
        requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
    # after printing the data results parsed into our CarData class
    for result in data['results']:
        db_obj = CarData.parse_from_back4app(result)
        # aya da pa database k awal na shta k na?
        object_list.append(db_obj.to_json())

print(json.dumps(object_list, indent=2))
# mapped the data again to store it into the local database
car1= Car(

    object_id = db_obj.object_id,
    year = db_obj.year,
    make = db_obj.make,
    model = db_obj.model,
    category = db_obj.category,
    created_at = db_obj.created_at,
    updated_at = db_obj.updated_at,
    owner_id = 1
    
)

#if db_obj is not None:
    #abort(409, description="The already Data exists in the Database")
# storing the data into local database and committing it    
db.session.add(car1)
db.session.commit()

# As we are Using the unique constraint in the local database dara objects the data
# will not store again, means no duplication in data       



    