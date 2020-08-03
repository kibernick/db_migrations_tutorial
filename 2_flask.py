"""An example Flask app

run with: FLASK_APP=2_flask.py flask run

initialize alembic with 
"""
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://my_migrations_user:my_migrations_pass@localhost/my_migrations_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Cat(db.Model):
    id = db.Column(db.Integer, db.Sequence('cat_id_seq'), primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Cat %r>' % self.name

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


###

@app.route('/')
def hello_world():
    n_cats = Cat.query.count()
    return f"Hello, World, you're full of cats: {n_cats}"

####

@app.route('/cats', methods=['GET'])
def list_cats():
    """Lists all the cats in the database.

    >>> import requests
    >>> requests.get("http://127.0.0.1:5000/cats")
    """
    cats = Cat.query.all()
    return jsonify([cat.as_dict() for cat in cats])


@app.route('/cats', methods=['POST'])
def add_cat():
    """Add a new cat.

    >>> import requests
    >>> cat = {"name": "Tommy"}
    >>> requests.post("http://127.0.0.1:5000/cats", json=cat)

    NOTE: No validation :')
    """
    new_cat = Cat(**request.json)
    db.session.add(new_cat)
    db.session.commit()

    return jsonify(new_cat.as_dict())


@app.route('/cats/<int:cat_id>', methods=['GET'])
def get_cat(cat_id: int):
    """Retrieve a specific cat from the database.

    >>> import requests
    >>> requests.get("http://127.0.0.1:5000/cats")
    """
    cat = Cat.query.get(cat_id)
    if not cat:
        return make_response("Not found", 404)

    return cat.as_dict()
    


@app.route('/cats/<int:cat_id>/rate/<int:rating>', methods=['GET'])
def delete_cat(cat_id: int, rating: int):
    """Give a cat a rating.

    >>> import requests
    >>> requests.get("http://127.0.0.1:5000/cats/XXX/rate/YYY")
    """
    cat = Cat.query.get(cat_id)
    if not cat:
        return make_response("Not found", 404)

    # TODO: implement rating!
    return cat.as_dict()
