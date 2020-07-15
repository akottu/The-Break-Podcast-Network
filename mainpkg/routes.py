from mainpkg.models import Episode, Podcast
from flask import render_template, url_for, flash, redirect, request
from mainpkg.forms import AddEpisode, AddPodcast
from mainpkg import app, db
from PIL import Image
import secrets
import os

 ## name of the module - helps look for templates and static files

# posts = [
# 	{
# 	'Podcast' : 'Techbyte Tuesdays',
# 	'Episode' : 'Augmented Reality Cinemas',
# 	'Date' : 'May 5, 2020',
# 	'Logo' : 'tech.png'
# 	},
# 	{
# 	'Podcast' : 'Hot Tea and Hot Takes',
# 	'Episode' : 'Why Lime Bikes are better than Lime Scooters',
# 	'Date' : 'May 12, 2020',
# 	'Logo' : 'tea.jpeg'
# 	},
# 	{
# 	'Podcast' : 'The  Break',
# 	'Episode' : 'The Journey Here Part 2',
# 	'Date' : 'May 9, 2020',
# 	'Logo' : 'break.png'
# 	}

# ]

# main routes
@app.route('/')
@app.route('/home') ## homepage - normally return html in function
@app.route('/podcasts')
def podcasts():
    podcasts = Podcast.query.all() ## grab all podcasts and episodes from database. should only grab podcasts using DISTINCT
    return render_template('podcasts.html', podcasts = podcasts)  ## passing in argument posts

@app.route('/about') 
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# podcast pages
@app.route('/the_break')
def the_break():
    return render_template('the_break.html')

# about routes
@app.route('/producers')
def producers():
    return render_template('producers.html')

@app.route('/hosts')
def hosts():
    return render_template('hosts.html')

@app.route('/editors')
def editors():
    return render_template('editors.html')

@app.route('/marketers')
def marketers():
    return render_template('marketers.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/artists')
def artists():
    return render_template('artists.html')

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/images/podcast_pics', picture_fn)## creating path to profile picture using pathing
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn

@app.route("/podcasts/add", methods = ['GET','POST'])
def new_post():
	form = AddPodcast()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
		podcast = Podcast(name = form.name.data,
		 description = form.description.data, image_file = picture_file) ## call to Episode relation
		
		## figure out way to add image to db
		db.session.add(podcast)
		db.session.commit()
		flash('Your podcast has been added', 'success')
		return redirect(url_for('podcasts'))  ## maybe error here -redirect to index
	return render_template('add_podcast.html', title = 'New Podcast', form = form)

@app.route("/podcasts/<int:podcast_id>") ## accessed when podcast is explored
def explore(podcast_id):
	podcast = Podcast.query.get_or_404(podcast_id)
	return render_template('podcast_page.html', title=podcast.name, podcast = podcast)

## if we run this flask blog with python then it will be in debug mode
## if we import it it won't run in debug mode
if __name__ == '__main__': 
	app.run(debug=True)  

