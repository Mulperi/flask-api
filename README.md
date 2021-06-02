# Python, PostgreSQL, Flask, SQLAlchemy

## PostgreSQL
- Install PostgreSQL (https://www.postgresql.org/download/) or with homebrew.
- Add PostgreSQL to path: `sudo nano /etc/paths` -> /Library/PostgreSQL/13/bin
- If you need to use global postgres user to login via commandline, use: `sudo -u postgres psql`
- You can check if Postgres server is running with command: `pg_isready`. Also it will show you the port.

### PostgreSQL commands:
- Open postgresql command line interface: `psql` you can also directly connect to database when connecting: `psql -U postgres -d dbname`
- List databases: `\l`
- Connect to database: `\c`
- Display tables: `\dt`
- Display table details: `\d "Users"` or `\d+`
- Create database: `CREATE DATABASE dbname;`
- Create table: `CREATE TABLE tablename;`
- Delete table: `DROP TABLE tablename;`
```
CREATE TABLE todos (
	id serial PRIMARY KEY,
	description VARCHAR ( 50 ) NOT NULL,
	done BOOLEAN NOT NULL
);
```
Insert new data into table and delete it:
```
INSERT INTO todos (description, done) values ('drink water.', TRUE);
DELETE FROM todos WHERE id == 1;
```
Create users table, insert data and view data:
```
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (50) UNIQUE NOT NULL
);

INSERT INTO users (first_name, last_name, email)
VALUES ('Angus', 'MacGyver', 'angus@phoenix.com');

SELECT * FROM users;
```

## Python
- Install venv to be able to create python virtual environment: `sudo pip3 install virtualenv`. This allows you to install dependencies specifically for this project and not globally.
- Crate virtual environment (in your project directory): `venv myenvironment` or `python3 -m venv myenvironment`.
- Activate virtual environment: `source myenvironment/bin/activate `
- Install Flask and Flask Restful: `pip3 install flask` and `pip3 install flask-restful`.
- Install SQLAlchemy, a python sql toolkit / object relational mapper (https://www.sqlalchemy.org/): `pip3 install sqlalchemy`.
- Install psycopg2, a PostgreSQL database adapter for python (https://pypi.org/project/psycopg2/): `pip3 install psycopg2`. On Mac you may need to also run `pip3 install psycopg2-binary`.
- Install marshmallow to be able to JSON serialize the database results: `pip3 install flask-marshmallow` and `pip3 install marshmallow-sqlalchemy`.
- Lastly, generate requirements file: `pip3 freeze > requirements.txt`, this allows other developers to easily install all dependencies for the project. Use `pip3 install -r requirements.txt -v` to install those packages.

### Connect to database

```
from sqlalchemy import create_engine
# Connect to database.
db_string = "postgresql://postgres:postgres@localhost:5432"
db = create_engine(db_string)
# Select data and print it.
result = db.execute("SELECT * FROM todos")  
for r in result:  
    print(r)
```



# flask-api
# flask-api
