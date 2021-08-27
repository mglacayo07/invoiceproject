Invoice Project 
=======

Back End Programming Exercise.

Set it up
------

Create a virtual environment and install the requirements

    $ python3 -m venv ./venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt

or

    $ mkvirtualenv marsbackend
    $ workon marsbackend
    $ pip install -r requirements.txt

Get the local database ready.<br>
Change USER and PASSWORD database credentials on db.py 

    $ python init_db.py

Start the development server

    $ FLASK_APP=app.py flask run
    * Serving Flask app 'app.py' (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Check the service at http://127.0.0.1:5000/


Dependencies
------

invoiceproject uses Flask as a web framework, Flask RESTx for creating the interface, and SQLAlchemy to handle the database models. It uses a MySQL database.
