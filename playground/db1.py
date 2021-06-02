from sqlalchemy import create_engine
# Connect to database.
db_string = "postgresql://postgres:postgres@localhost:5432"
db = create_engine(db_string)
# Select data and print it.
result = db.execute("SELECT * FROM users2")  
for r in result:  
    print(r)