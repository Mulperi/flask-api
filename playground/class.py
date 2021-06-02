import json

# Define class.
class Todo:
    # Define constructor function with parameters.
    def __init__(self, id, description):
        # Assign parameters.
        self.id = id
        self.description = description

# Instantiate new object from Todo class.
first = Todo(id=1, description="terve")

# Print json output of the object.
print(json.dumps(first.__dict__))