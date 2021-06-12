from flask import jsonify
from flask_restful import abort, Resource
from sqlalchemy.orm.exc import NoResultFound
import uuid
from database import dbsession  # postgres
from models.user import User, user_schema, users_schema, userParser


class EndpointUsers(Resource):
    # GET ALL USERS
    def get(self):
        users = dbsession.query(User)
        print(users)
        return jsonify(users_schema.dump(users))

    # CREATE NEW USER.
    def post(self):
        args = userParser.parse_args(strict=True)  # Request body.
        newUserId = str(uuid.uuid4())  # Create new user id.
        newUser = User(
            id=newUserId, first_name=args["first_name"], last_name=args["last_name"], email=args["email"])
        dbsession.add(newUser)
        dbsession.commit()
        return {
            "id": newUserId,
            "first_name": args["first_name"],
            "last_name": args["last_name"],
            "email": args["email"]
        }


class EndpointUser(Resource):
    # GET USER WITH ID.
    def get(self, id):
        print(id)
        try:
            user = dbsession.query(User).filter(User.id == id).one()
            return jsonify(user_schema.dump(user))
        except NoResultFound as e:
            print(e)
            abort(404, message="Specified user does not exist.")

    def delete(self, id):
        try:
            user = dbsession.query(User).filter(User.id == id).one()
            dbsession.delete(user)
            dbsession.commit()
            return jsonify(user_schema.dump(user))
        except NoResultFound as e:
            print(e)
            abort(404, message="Specified user does not exist.")
