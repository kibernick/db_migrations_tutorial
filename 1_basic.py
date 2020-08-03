"""
Set up a postgress DB with:

$ psql 
=# CREATE DATABASE my_migrations_db;
=# CREATE USER my_migrations_user WITH ENCRYPTED PASSWORD 'my_migrations_pass';
=# GRANT ALL PRIVILEGES ON DATABASE my_migrations_db TO my_migrations_user;
"""

import psycopg2


conn = psycopg2.connect(database="my_migrations_db", 
                        user="my_migrations_user", 
                        password="my_migrations_pass")

cur = conn.cursor()


# Execute a command: this creates a new table
cur.execute("""
CREATE TABLE IF NOT EXISTS Cat (
    "id" serial PRIMARY KEY,
    "name" varchar(20) NOT NULL
);
""")
conn.commit()

# Insert some data
cur.execute("INSERT INTO Cat (name) VALUES (%s)", ("Roger",))

some_cats = ["Ginger", "Tubby", "Stacy"]

for some_cat in some_cats:
    cur.execute("INSERT INTO Cat (name) VALUES (%s)", (some_cat,))

conn.commit()

