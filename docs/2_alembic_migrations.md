# Alembic migrations

Set up Alembic in the `migrations` directory with:

```bash
$ alembic init migrations
```

This will set up some defaults in that dir. Among them check out `env.py`.

To start from a blank slate, drop the existing `Cat` table and then run:

```bash
$ alembic upgrade head
```

## Auto Generating Migrations

To auto-generate migrations (which includes creating tables from scratch) you need to modify the `env.py` file to find SQLAlchemy metadata.

Since in this example we're using plugins to get things going, modify the env.py as follows:

```python
# add your model's MetaData object here
# for 'autogenerate' support
from myapp import Cat
target_metadata = Cat.metadata
# target_metadata = None
```

Also, since we're not providing a Python package, need to export the root of this repo to your `PYTHONPATH`.

```bash
export PYTHONPATH=$(pwd)
```

Generate a new migration with:

```bash
$ alembic revision --autogenerate -m "Added Cat table"
```

A file should now me created inside the `migrations/versions` dir. After verification, we can run the migration and also commit the migration file to git.
