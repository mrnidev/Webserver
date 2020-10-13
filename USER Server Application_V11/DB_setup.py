
from datetime import datetime
from __main__ import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False)
	phone = db.Column(db.String(20), nullable=False)
	D_o_B = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	affiliation = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return str(self.username)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40), nullable=False)
	userID = db.Column(db.String(20), unique=True, nullable=False)
	D_o_B = db.Column(db.String(40), nullable=False, default=datetime.utcnow)
	address = db.Column(db.Text, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	user_id = db.Column(db.String(20), db.ForeignKey('user.username'), nullable=False)

	def __repr__(self):
		return (self.username)