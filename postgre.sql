DROP TABLE users;
CREATE TABLE users (
	id VARCHAR (50) PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (50) UNIQUE NOT NULL
);

INSERT INTO users (id, first_name, last_name, email)
VALUES ("994307c0-d74d-4079-b500-e020f61034f8", "Mika", "Lakanen", 'mika@phoenix.com');

INSERT INTO users (id, first_name, last_name, email)
VALUES ("49d2da0b-df32-4c26-9786-3d4cc5564afb", "Angus", "MacGyver", 'angus@phoenix.com');

SELECT * FROM users;

DROP TABLE entries;
CREATE TABLE entries(
   id VARCHAR (50) PRIMARY KEY NOT NULL,
   user_id VARCHAR (50) NOT NULL,
   hours DECIMAL NOT NULL,
   CONSTRAINT fk_user_id
      FOREIGN KEY(user_id) 
	  REFERENCES users(id)
);

INSERT INTO entries(id, user_id, hours) 
VALUES ('1', '994307c0-d74d-4079-b500-e020f61034f8', 7.5);

INSERT INTO entries(id, user_id, hours) 
VALUES ('2', '49d2da0b-df32-4c26-9786-3d4cc5564afb', 2);




CREATE TABLE device1values (
	id VARCHAR (50) PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (50) UNIQUE NOT NULL
);