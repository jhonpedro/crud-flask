from sql_alchemy import database

class HotelModel(database.Model):
  __tablename__ = 'hotels'
  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.Integer)
  stars = database.Column(database.Float(precision=1))
  daily = database.Column(database.Float(precision=2))
  city = database.Column(database.String(255))
  state = database.Column(database.String(255))
  
  def __init__(self, name, stars, daily, city, state):
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
  
  @classmethod
  def find(cls, id):
    hotel = cls.query.filter_by(id=id).first()

    return hotel if hotel else None

  @classmethod
  def find_all(cls):
    hotels = cls.query.all()

    return [hotel.json() for hotel in hotels]

  def store(self):
    database.session.add(self)
    database.session.commit()

  def update(self, name, stars, daily, city, state):
    self.name = name
    self.stars = stars
    self.daily = daily
    self.city = city
    self.state = state
    
    self.store()

    return self

  def delete(self):
    database.session.delete(self)
    database.session.commit()