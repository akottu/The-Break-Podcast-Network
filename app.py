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

@app.route('/') ## homepage - normally return html in function
def index():
	return render_template('index.html')

@app.route('/podcasts')
def podcasts():
    return render_template('podcasts.html', posts=posts) ## passing in argument posts

@app.route('/staff')
def staff():
	return 

@app.route('/about') 
def about():
    return render_template('about.html', title='About')

## if we run this flask blog with python then it will be in debug mode
## if we import it it won't run in debug mode
if __name__ == '__main__': 
	app.run(debug=True)  