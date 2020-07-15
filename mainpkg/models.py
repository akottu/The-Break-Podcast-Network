from mainpkg import db
from datetime import datetime

class Episode(db.Model):
	id = db.Column(db.Integer, primary_key = True) ## need primary key for SQL config
	episode = db.Column(db.String(100), nullable = False)
	podcast = db.Column(db.String(100), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) 
	description = db.Column(db.Text, nullable = False) 
	image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')

	def __repr__(self): ## how our object is printed when we print it out
		return f"Post('{self.title}','{self.date_posted}')" ## if we want content can get

class Podcast(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100), nullable = False) ## will be used to query individual episodes w/ name == podcast
	description = db.Column(db.Text, nullable = False)
	image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) 

	def __repr__(self): ## how our object is printed when we print it out
		return f"Post('{self.title}','{self.date_posted}')" ## if we want content can get

## must manually add models to db file in terminal
## from mainpkg import db
## db.drop_all()
## db.create_all()