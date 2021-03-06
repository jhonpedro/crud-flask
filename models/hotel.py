from resources.hotels import hotels

class HotelModel:
  def __init__(self, id, name, stars, daily, city, state):
    self.id = id if id != None else len(hotels)
    self.name = name
    self.stars = stars
    self.daily = daily
    self.city = city
    self.state = state
  
  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'stars': self.stars,
      'daily': self.daily,
      'city': self.city,
      'state': self.state
    }
