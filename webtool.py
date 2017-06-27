from flask import Flask, flash, render_template, request, redirect, url_for
import flask_login
from flask_login import current_user

#this came from alex init, it may need to be changed with __init__.py. 
# Prepare flask and login manager for use
#TODO: autheticate user; check if user is auth and return index.html; also serve page to outside viewers

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.secret_key = 'thisissupersecret'
@app.route('/hello', methods=['GET', 'POST'])
def my_form():
	return render_template("index.html")

users = {'user': {'pw': 'password'}} # Temporary dictionary, mysql will be later implemented
class User(flask_login.UserMixin):
	pass


@login_manager.user_loader
def user_loader(username, methods=['GET', 'POST']): # Prepares user for non-login activities
	if username not in users:
		return
	user = User()
	user.id = username
	flash('this is the user_loader method')
	return user

@login_manager.request_loader
def request_loader(request, methods=['GET', 'POST']):
	username = request.form['inputUsername']
	if username not in users:
		return
	user = User()
	user.id = username
        
	flash('this is the request loader method')
	user.isauthenticated = request.form['inputPassword'] == users[username]['inputPassword']
	return user
@app.route('/', methods=['GET', 'POST'])
def login():
        print 'hello world'
	return render_template('index.html')

       


@app.route('/create', methods=['GET', 'POST'])
def create_post():
	date = request.form['inputDate']
	location = request.form['inputLocation']
	fob = request.form['inputFoB']
	askLocation = request.form['inputAskingLocation']
	extraText = request.form['extraText']

if __name__ == "__main__":
    app.run(debug=True)
