from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required, get_jwt

class Hotels(Resource):
  def get(self):
    hotels = HotelModel.find_all() 

    return hotels

class Hotel(Resource):
  arguments = reqparse.RequestParser()

  arguments.add_argument('name', type=str, required=True, help='name is required')
  arguments.add_argument('stars', type=float, required=True, help='stars is required')
  arguments.add_argument('daily', type=float, required=True, help='stars is required')
  arguments.add_argument('city',  type=str, required=True, help='city is required')
  arguments.add_argument('state')

  def get(self, id):
    try:
      hotel = HotelModel.find(id)
    except:
      pass
    if(hotel):
      return hotel.json()
    
    return {'message': 'hotel not found'}, 404

  @jwt_required()
  def post(self):
    data = Hotel.arguments.parse_args()
    new_hotel = HotelModel(**data)

    try:
      new_hotel.store()
    except:
      return {'message': 'an error ocurred in server'}, 500

    return new_hotel.json()

  @jwt_required()
  def put(self, id):
    hotel = HotelModel.find(id)

    if not (hotel):
      return {'message': 'this hotel dont exist to be edited'}, 404

    data = Hotel.arguments.parse_args()
    try:
      new_hotel = hotel.update(**data)
    except:
      return {'message': 'an error ocurred in server'}, 500

    return new_hotel.json()

  @jwt_required()
  def delete(self, id):

    hotel = HotelModel.find(id)

    try:
      HotelModel.delete(hotel)
    except:
      return False, 400

    return True
    