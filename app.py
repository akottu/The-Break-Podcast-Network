from flask import Flask, render_template, url_for
app = Flask(__name__) ## name of the module - helps look for templates and static files

posts = [
	{
	'Podcast' : 'Techbyte Tuesdays',
	'Episode' : 'Augmented Reality Cinemas',
	'Date' : 'May 5, 2020',
	'Logo' : 'tech.png'
	},
	{
	'Podcast' : 'Hot Tea and Hot Takes',
	'Episode' : 'Why Lime Bikes are better than Lime Scooters',
	'Date' : 'May 12, 2020',
	'Logo' : 'tea.jpeg'
	},
	{
	'Podcast' : 'The  Break',
	'Episode' : 'The Journey Here Part 2',
	'Date' : 'May 9, 2020',
	'Logo' : 'break.png'
	}

]

# main routes
@app.route('/') ## homepage - normally return html in function
def home():
	return render_template('index.html')

@app.route('/podcasts')
def podcasts():
    return render_template('podcasts.html', posts=posts) ## passing in argument posts

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

## if we run this flask blog with python then it will be in debug mode
## if we import it it won't run in debug mode
if __name__ == '__main__': 
	app.run(host='0.0.0.0', port=5000)