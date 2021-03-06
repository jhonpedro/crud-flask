from flask_restful import Resource, reqparse

hotels = [
  {
    'id': 0,
    'name': 'Alpha Hotel',
    'stars': 4.3,
    'daily': 420,
    'city': 'Iporá',
    'state': 'Goiás'
  },
  {
    'id': 1,
    'name': 'Bravo Hotel',
    'stars': 5,
    'daily': 500,
    'city': 'Rio de Janeiro',
    'state': 'Rio de Janeiro'
  },
  {
    'id': 2,
    'name': 'Beta Hotel',
    'stars': 4,
    'daily': 250,
    'city': 'Santa catatrina',
    'state': 'Paraná'
  },
]

from models.hotel import HotelModel


class Hotels(Resource):
  def get(self):
    return hotels

class Hotel(Resource):
  arguments = reqparse.RequestParser()

  arguments.add_argument('name')
  arguments.add_argument('stars')
  arguments.add_argument('daily')
  arguments.add_argument('city')
  arguments.add_argument('state')

  def find_hotel(id):
    for hotel in hotels:
      if(hotel['id'] == int(id)):
        return hotel
    return None

  def get(self, id):
    hotel = Hotel.find_hotel(id)
    if(hotel):
      return hotel
    
    return {'message': 'Hotel not found'}, 404


  def post(self, id):
    data = Hotel.arguments.parse_args()

    new_hotel_object = HotelModel(None, **data)
    new_hotel = new_hotel_object.json()
    hotels.append(new_hotel)

    return new_hotel

  def put(self, id):
    hotel = Hotel.find_hotel(id)

    data = Hotel.arguments.parse_args()

    new_hotel_object = HotelModel(None, **data)
    new_hotel = new_hotel_object.json()

    if(hotel):
      new_hotel['id'] = int(id)
      hotel.update(new_hotel)

      return new_hotel, 200
    new_hotel['id'] = len(hotels)
    hotels.append(new_hotel)

    return new_hotel, 201

  def delete(self, id):

    hotel = Hotel.find_hotel(id)

    try:
      hotels.remove(hotel)
    except:
      return False, 400


    return True

