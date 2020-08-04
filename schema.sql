--- set up database and user
CREATE DATABASE my_migrations_db;
CREATE USER my_migrations_user WITH ENCRYPTED PASSWORD 'my_migrations_pass';
GRANT ALL PRIVILEGES ON DATABASE my_migrations_db TO my_migrations_user;

--- create table
CREATE TABLE IF NOT EXISTS "cat" (
    "id" serial PRIMARY KEY,
    "name" varchar(20) NOT NULL
);
