#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate class and models module here to set up our migrations using our flask application instance and our SQLAlchemy instance
from flask_migrate import Migrate
from models import db

# create an instance of the Flask class
# We also initialized our application for use within our database configuration with db.init_app(app)
app = Flask(__name__)

# configure our db
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# set up a migration for our Flask app instance and our SQLAlchemy instance
migrate = Migrate(app, db)

# Initialize our application for use within our database configuration
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
