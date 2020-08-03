-- create our db
DO
$do$
BEGIN
   IF EXISTS (SELECT FROM pg_database WHERE datname = 'my_migrations_db') THEN
      RAISE NOTICE 'Database already exists';
   ELSE
      PERFORM dblink_exec('dbname=' || current_database()
                        , 'CREATE DATABASE my_migrations_db');
   END IF;
END
$do$;

-- create our user and set rights
DO
$do$
BEGIN
    IF EXISTS (
        SELECT FROM pg_catalog.pg_roles  -- SELECT list can be empty for this
        WHERE  rolname = 'my_migrations_user'
    ) THEN
        RAISE NOTICE 'User already exists';
    ELSE
        CREATE ROLE my_migrations_user LOGIN PASSWORD 'my_migrations_pass';
        GRANT ALL PRIVILEGES ON DATABASE my_migrations_db TO my_migrations_user;
   END IF;
END
$do$;

