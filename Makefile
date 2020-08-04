run:
	FLASK_APP=myapp.py flask run

install:
	python3 -m venv venv
	source ./venv/bin/activate
	pip install -r requirements.txt
