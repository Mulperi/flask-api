from endpoints.users import EndpointUsers, EndpointUser
from endpoints.entries import EndpointEntries, EndpointEntry


def register_endpoints(api):
    api.add_resource(EndpointUsers, '/users', '/users/')
    api.add_resource(EndpointUser, '/users/<string:id>', '/users/<string:id>/')
    api.add_resource(EndpointEntries, '/entries', '/entries/')
    api.add_resource(EndpointEntry, '/entries/<string:id>',
                     '/entries/<string:id>/')
