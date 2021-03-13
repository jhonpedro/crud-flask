from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.hotels import Hotels, Hotel
from resources.user import User, UserRegister, UserLogin, UserLogout
from blacklist import BLACKLIST

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'asdasdadsaqw12312$!@$'
app.config['JWT_BLACKLIST_ENABLE'] = True

api = Api(app)

jwt = JWTManager(app)


@app.before_first_request
def create_database():
  database.create_all()

@jwt.token_in_blocklist_loader
def verify_blacklist(self, token):
  return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_invalidated(header, data):
  return jsonify({'message': 'you already have logged out'}), 401

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<string:id>', '/hotel')
api.add_resource(User, '/users/<int:id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/session')
api.add_resource(UserLogout, '/sessionout')

if(__name__ == '__main__'):
  from sql_alchemy import database

  database.init_app(app)
  app.run(debug=True)