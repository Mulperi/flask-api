from sqlalchemy.orm.session import sessionmaker
from models.entry import Entry
from models.user import User
from database import base
from sqlalchemy import create_engine

db_string = "postgresql://postgres:postgres@localhost:5432"
db = create_engine(db_string)
Session = sessionmaker(db)
dbsession = Session()

# Create tables.
Entry.__table__.drop(db)
User.__table__.drop(db)
base.metadata.create_all(db)

# Insert rows.
user1 = User(id="abc-123", first_name="Mika",
             last_name="Lakanen", email="mika@phoenix.com")
user2 = User(id="def-456", first_name="Angus", last_name="MacGyver",
             email="angus@phoenix.com")
dbsession.add(user1)
dbsession.add(user2)
dbsession.commit()
entry1 = Entry(id="entry-123", description="Basic work.",
               amount="7.5", user_id="abc-123")
entry2 = Entry(id="entry-456", description="SW development.",
               amount="2", user_id="def-456")
dbsession.add(entry1)
dbsession.add(entry2)
dbsession.commit()
