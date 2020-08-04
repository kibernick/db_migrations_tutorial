# Intro

When just starting out with storing data, the simplest thing after saving data to a file would be to save it to a 
database. The simplest database to use is SQLite, and it's covered by the 
[Python standard library](https://docs.python.org/3/library/sqlite3.html).

[plain_python.py](../plain_python.py) is an example of how to use a Postgresql database with plain Python. It requires 
installing the `psycopg2` library (driver) to talk to the database. Additionally, setting up the database and user is
done manually, using the commands in [schema.sql](../schema.sql).

## Adding structure

Reasons for adding more structure to programs working with databases, and not just have scripts:

* each person involved has to remember which script they ran
* different databases - e.g. (n) local databases, testing, production
  * doing a rolling update in production by hand, doesn't sound like a fun time
* new team member joining - requires creating a "dump" of your database and it could be in a "dirty" state

## Database migration

A **database migration** means transforming your data and the way you store it. It can come in the form of scripts and 
lets us automate this process.

Two flavours:

* **Schema migration** – changing your database schema, for example: adding or removing tables, renaming columns, 
changing the field types, adding triggers.
* **Data migration** - adding, deleting and transforming data.

Two directions:

* Up / Forwards
* Down / Backwards (rollback)

## Tools

Migration tools help us automate these changes. They usually write to a separate "migrations" table, which tracks 
migrations for that specific database. This way we can keep track of back and forward movements between the states of 
the database.

The tools don't let us execute operations on the databases but help us make **migration scripts**, which can be run to 
make the changes. These can later be committed to git and shared with our team.

We can also use these tools to migrate data from one database to another, and between different types of databases.

### Examples:

* For smaller frameworks like Flask, FastAPI etc:
    * [SQLAlchemy](https://docs.sqlalchemy.org/en/13/) + [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
* Django, a bigger, batteries-included web framework, uses [Django migrations](https://docs.djangoproject.com/en/3.0/topics/migrations/) :)
* Non-Python projects: Flyway (Java+XML)
    * Can also use Alembic, less automated
    
The principles of generating files that describe the migrations are the same across the different tools/libraries.

### Raw SQL and ORMs

A lot of the tools like Alembic take advantage of **object-relational mappings** (ORM), where we map entities in our
database to Python objects, to automate migration script generation. This covers most use cases, but we can also write 
plain SQL if we need to do something more advanced.

