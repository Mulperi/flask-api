from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  

base = declarative_base()
db_string = "postgresql://postgres:postgres@localhost:5432"
db = create_engine(db_string)
Session = sessionmaker(db)
dbsession = Session()

print("database session created")

# Create
# user1 = User(first_name="test1", last_name="test1", email="kakka")
# session.add(user1)
# session.commit()

# Read
# users = dbsession.query(User)
# for user in users:
#     print(user.email)

# # Update
# doctor_strange.title = "Some2016Film"
# session.commit()

# # Delete
# session.delete(doctor_strange)
# session.commit()
