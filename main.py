from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
import database
from resources import register_endpoints

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)
register_endpoints(api)


if __name__ == '__main__':
    app.run(debug=True)
