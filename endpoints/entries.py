from flask import jsonify
from flask_restful import abort, Resource
from sqlalchemy.exc import IntegrityError, NoReferenceError
from sqlalchemy.orm.exc import NoResultFound
import uuid
from database import dbsession  # postgres
from models.entry import Entry, entry_schema, entries_schema, entryParser


class EndpointEntries(Resource):
    def get(self):
        entries = dbsession.query(Entry)
        print(entries)
        return jsonify(entries_schema.dump(entries))

    def post(self):
        args = entryParser.parse_args(strict=True)  # Request body.
        newId = str(uuid.uuid4())  # Create new user id.
        newItem = Entry(
            id=newId, description=args["description"], amount=args["amount"], user_id=args["user_id"])
        try:
            dbsession.add(newItem)
            dbsession.commit()
        except IntegrityError as e:
            dbsession.rollback()
            abort(400, message="Specified user does not exist.")

        return {
            "id": newId,
            "description": args["description"],
            "amount": args["amount"],
            "user_id": args["user_id"]
        }


class EndpointEntry(Resource):
    def get(self, id):
        print(id)
        try:
            entry = dbsession.query(Entry).filter(Entry.id == id).one()
            return jsonify(entry_schema.dump(entry))
        except NoResultFound as e:
            print(e)
            abort(404, message="Specified entry does not exist.")


    def delete(self, id):
        try:
            entry = dbsession.query(Entry).filter(Entry.id == id).one()
            dbsession.delete(entry)
            dbsession.commit()
            return jsonify(entry_schema.dump(entry))
        except NoResultFound as e:
            print(e)
            abort(404, message="Specified entry does not exist.")
