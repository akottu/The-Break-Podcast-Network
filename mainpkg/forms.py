from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mainpkg.models import Episode

class AddEpisode(FlaskForm):
	podcast = StringField('Podcast',
		validators = [DataRequired()])
	name = StringField('Episode',
		validators = [DataRequired()])
	description =  TextAreaField('Description', 
		validators=[DataRequired()])
	picture = FileField('Podcast Logo',
		validators=[FileAllowed(['jpg','png'], 'Image only!'), FileRequired('File was empty!')])
	submit = SubmitField('Post')
	password = StringField('Password',
		validators = [DataRequired()])

class AddPodcast(FlaskForm):
	name = StringField('Podcast Name',
		validators = [DataRequired()])
	description =  TextAreaField('Description', 
		validators=[DataRequired()])
	picture = FileField('Podcast Logo',
		validators=[FileAllowed(['jpg','png'], 'Image only!'), FileRequired('File was empty!')])
	submit = SubmitField('Post')