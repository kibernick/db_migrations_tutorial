"""read in some cats

Revision ID: 2aec8bdecc20
Revises: 0e1a322a8e2c
Create Date: 2020-08-04 22:24:51.568311

"""
from alembic import op
from sqlalchemy import orm

from myapp import Cat  # TODO: make sure that "myapp" is available in this scope

# revision identifiers, used by Alembic.
revision = "2aec8bdecc20"
down_revision = "0e1a322a8e2c"
branch_labels = None
depends_on = None


EXAMPLE_DATA = ["Ginger", "Tubby", "Stacy"]


def upgrade():
    # Connect your declarative model to the database going through the migration.
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    for cat_name in EXAMPLE_DATA:
        cat = Cat(name=cat_name)
        session.add(cat)

    session.commit()


def downgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    session.query(Cat).delete()  # Deletes all records!
    session.commit()
