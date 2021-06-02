from sqlalchemy import Column, String
from flask_marshmallow import Schema
from flask_restful import reqparse
from database import base

# User class that represents the table in database.
class User(base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Marshmallow schema allows us to dump db result as JSON.
class UserSchema(Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email")


# Marshmallow schemas instantiate.
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Parser settings.
userParser = reqparse.RequestParser()
userParser.add_argument('first_name', type=str)
userParser.add_argument('last_name', type=str)
userParser.add_argument('email', type=str)
