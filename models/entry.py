from sqlalchemy import Column, String
from flask_marshmallow import Schema
from flask_restful import reqparse
from sqlalchemy.sql.schema import ForeignKey
from database import base


class Entry(base):
    __tablename__ = 'entries'
    id = Column(String, primary_key=True)
    description = Column(String)
    amount = Column(String, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)


class EntrySchema(Schema):
    class Meta:
        fields = ("id", "description", "amount", "user_id")


entry_schema = EntrySchema()
entries_schema = EntrySchema(many=True)

entryParser = reqparse.RequestParser()
entryParser.add_argument('id', type=str)
entryParser.add_argument('description', type=str)
entryParser.add_argument('amount', type=str)
entryParser.add_argument('user_id', type=str)
