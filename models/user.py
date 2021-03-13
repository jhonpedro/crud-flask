from sql_alchemy import database

class UserModel(database.Model):
  __tablename__ = 'users'
  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.String(50))
  login = database.Column(database.String(50))
  password = database.Column(database.String(255))
  
  def __init__(self, name, login, password):
    self.name = name
    self.login = login
    self.password = password
  
  def json(self):
    return {
      'id': self.id,
      'name': self.name,
      'login': self.login
    }
  
  @classmethod
  def find(cls, id):
    user = cls.query.filter_by(id=id).first()

    return user if user else None

  @classmethod
  def find_by_login(cls, login):
    user = cls.query.filter_by(login=login).first()

    return user if user else None

  def store(self):
    database.session.add(self)
    database.session.commit()

  def delete(self):
    database.session.delete(self)
    database.session.commit()