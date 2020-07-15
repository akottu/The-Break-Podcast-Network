from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '4c9f48d3ba3a1c354b9ad6aa5024895f' ## setting config value in application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' ##  creates site.db in project directory
db = SQLAlchemy(app)

from mainpkg import routes