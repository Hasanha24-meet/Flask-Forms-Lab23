from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi", "Aloosh"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
		if username == "siwarha" and password == '123':
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi", "Aloosh"]
	return render_template('home.html', facebook_friends=facebook_friends)


@app.route('/friend_exists/<string:name>')
def friend_exists(name):
  if name in facebook_friends:
    return render_template('friend_exists.html', is_friend=True)
  else:
    return render_template('friend_exists.html', is_friend=False)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
