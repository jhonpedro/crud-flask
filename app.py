from flask import Flask
from flask_restful import Api

from resources.hotels import Hotels, Hotel

app = Flask(__name__)
api = Api(app)

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<string:id>')

if(__name__ == '__main__'):
  app.run(debug=True)