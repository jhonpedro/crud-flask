from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import jwt_required, create_access_token, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

class User(Resource):

  def get(self, id):
    try:
      user = UserModel.find(id)
    except:
      pass
    if(user):
      return user.json()
    
    return {'message': 'user not found'}, 404

  def delete(self, id):

    user = UserModel.find(id)

    try:
      UserModel.delete(user)
    except:
      return False, 400

    return True

attributes = reqparse.RequestParser()
attributes.add_argument('name', help="name can not be blank")
attributes.add_argument('login', required=True, help="login can not be blank")
attributes.add_argument('password', required=True, help="password can not be blank")

class UserRegister(Resource):
  
  def post(self):
  
    data = attributes.parse_args()


    if UserModel.find_by_login(data['login']):
      return {'message': f"login '{data['login']}' already exists"}, 403

    user = UserModel(**data)

    try:
      user.store()  
    except:
      return False, 404

    return True, 201

class UserLogin(Resource):

  @classmethod
  def post(cls):
    data = attributes.parse_args()

    user = UserModel.find_by_login(data['login'])
  
    if user and safe_str_cmp(user.password, data['password']):
      token = create_access_token(identity=user.id)
      return {'token': token}, 200
    return {'message': 'username or password are incorrect'}, 403


class UserLogout(Resource):
  @jwt_required()
  def post(self):
    jwt_id = get_jwt()['jti']
    BLACKLIST.add(jwt_id)
    return {'message': 'logged out sucessfully'}