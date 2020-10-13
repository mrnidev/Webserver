from flask import Flask, render_template, url_for, flash, redirect, request, send_file
from data_retrieval import index_value
from down_load_data import data_down_load
from flask_sqlalchemy import SQLAlchemy
import os
import time
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user
import random
#from DB_setup import User, Post, db_uri, db
app = Flask(__name__)

#PEOPLE_FOLDER = os.path.join('static', 'people_photo\')
#print(PEOPLE_FOLDER)
app.config['SECRET_KEY'] = 'asajksdkasdkasdkasdka'
db_path = os.path.join(os.path.dirname(__file__), 'site.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#printapp.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from DB_setup import User, Post
from  forms import RegistrationForm, LoginForm, DataColloecttionForm,  Datavisualization, Notification_Init_Session_Form, Multi_Check, Text_Entry, Numeric_Entry, Text_Statement, Range_Slider, UserForm

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(20), unique=True, nullable=False)
# 	email = db.Column(db.String(120), unique=True, nullable=False)
# 	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
# 	password = db.Column(db.String(60), nullable=False)
# 	posts = db.relationship('Post', backref='author', lazy=True)

# 	def __repr__(self):
# 		return str(self.username)

# class Post(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.String(40), unique=True, nullable=False)
# 	date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
# 	contents = db.Column(db.Text, nullable=False)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# 	def __repr__(self):
# 		return (self.title)



#app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

posts = [

{'author':'Corey Schafer',
'title':'Corey Schafer Message',
'content':'Something ...',
'date_posted':'March 01, 2019',
},
{'author':'Jhon Doe',
'title':'Jhon Doe Message',
'content':'Something ...',
'date_posted':'March 01, 2020',
}

]

code_used = False
confirmation_code = random.randint(1111, 9999)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts, title = 'Home')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
	db.create_all()
	global code_used
	global confirmation_code
	display = 'Confirmation Code'
	if code_used == True:
		code_used = False
		confirmation_code = random.randint(1111, 9999)
		flash(display +' {}'.format(confirmation_code), 'success')
	else:
		flash(display +' {}'.format(confirmation_code), 'success')
	if current_user.is_authenticated:
		flash('Already logedin','danger')
		return redirect(url_for('home'))
	form = RegistrationForm()
	if  form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, phone=form.phone_number.data, D_o_B=form.DoB.data, email=form.email.data, password=hashed_password, affiliation=form.affiliation.data)
		code = int(form.confirm_code.data)
		print(code)
		print(confirmation_code)
		if code == confirmation_code:
			db.session.add(user)
			db.session.commit()
			display = 'Account created for '
			flash(display +' {}!'.format(form.username.data), 'success')
			code_used = True
			return redirect(url_for('login'))
		else:
			flash('Invalid confirmation code!', 'danger')

	return render_template("register.html", title='Register', form=form)


@app.route("/login" , methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		flash('Already logedin','danger')
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			flash('Logged in successfully', 'success')
			return redirect(url_for('home'))
		else:
			flash('Could not Login. Please check email and password.', 'danger')
	return render_template("login.html", title='Login', form=form)

@app.route("/logout")
def logout():
	flash('Logged out successfully', 'success')
	logout_user()
	return redirect(url_for('home'))

@app.route("/account")
def account():
	return render_template("account.html", title='Account')

@app.route("/datacolloecttion")
def datacolloecttion():
	form = DataColloecttionForm()
	return render_template("datacolloecttion.html", title='Data Collection', form=form)

@app.route("/current_users")
def current_users():
	return render_template("current_users.html", title='Data Collection')

@app.route("/user_register", methods = ['GET', 'POST'])
def user_register():
	db.create_all()
	form = UserForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = Post(username=str(form.username.data), userID=str(form.userID.data), D_o_B=str(form.DoB.data), address=str(form.user_address.data), password=str(hashed_password), user_id=str(current_user))
		db.session.add(user)
		db.session.commit()
		flash('User Account for {} created successfully'.format(str(form.username.data)), 'success')
		return redirect(url_for('home'))
	return render_template("user_register.html", title='Data Collection', form=form)

@app.route("/notification_init_session_form")
def notification_init_session_form():
	form = Notification_Init_Session_Form()
	return render_template("notification_init_session_form.html", title='Data Collection', form=form)

@app.route("/multi_check")
def multi_check():
	form = Multi_Check()
	return render_template("multi_check.html", title='Data Collection', form=form)

@app.route("/text_entry")
def text_entry():
	form = Text_Entry()
	return render_template("text_entry.html", title='Data Collection', form=form)

@app.route("/numeric_entry")
def numeric_entry():
	form = Numeric_Entry()
	return render_template("numeric_entry.html", title='Data Collection', form=form)

@app.route("/text_statement")
def text_statement():
	form = Text_Statement()
	return render_template("text_statement.html", title='Data Collection', form=form)

@app.route("/range_slider")
def range_slider():
	form = Range_Slider()
	return render_template("range_slider.html", title='Data Collection', form=form)


@app.route("/return-file")
def return_file():
	bolean = data_down_load()
	if bolean == 0:
		return send_file('Final_score.csv', attachment_filename = 'Final_Score.csv')
	else:
		print('Error')

@app.route("/Survey_form")
def Survey_form():
	return render_template("Survey_form.html", title="Create New Survey")

@app.route("/Start_up_session")
def Start_up_session():
	return render_template("Start_up_session.html", title="Start Up session")

@app.route("/Notification_initiated_session")
def Notification_initiated_session():
	return render_template("Notification_initiated_session.html", title="Start Up session")

@app.route("/User_initiated_session")
def User_initiated_session():
	return render_template("User_initiated_session.html", title="Start Up session")


@app.route("/visualize", methods = ['GET', 'POST'])
def visualize():
	form = Datavisualization()
	if request.method == 'POST':
		u_id = int(form.users_id.data)
		d_id = int(form.date_id.data)
		bol, User_id= index_value(u_id, d_id)
		#full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
		#time.sleep(1)
		image_path = str(User_id) + '.png'
		#path = str(path)
		#print('Path os {}'.format(path))
		return render_template("graph.html", title='Data Visualization', form=form, users_image = image_path)

	return render_template("visualize.html", title='Data Visualization', form=form)	


if __name__ == '__main__':
	#app.run(debug=True)
	app.run(host= '223.195.36.188', port=9000, debug=True)
