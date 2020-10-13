from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required, ValidationError, InputRequired
from data_retrieval import *
from DB_setup import User, Post

class RegistrationForm(FlaskForm):
	username = StringField('Therapist Name', validators=[DataRequired(), Length(min=2, max=20)])
	phone_number = StringField('Phone Number', render_kw={"placeholder": "010-0000-0000"}, validators=[DataRequired()])
	DoB = DateField('Date of Birth', render_kw={"placeholder": "YYYY-MM-DD"}, validators=[DataRequired()])
	email = StringField('Email ID', render_kw={"placeholder": "example@gmail.com"}, validators=[DataRequired(), Email()])
	password = PasswordField('Password', render_kw={"placeholder": "5-8"}, validators=[DataRequired(), Length(min=4, max=8)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	affiliation = StringField('Affiliation', validators=[DataRequired()])
	confirm_code = IntegerField('Confirmation Code', validators=[DataRequired()])

	submit = SubmitField('Sign Up')

	# def validate_username(self, username):
	# 	user = User.query.filter_by(username=username.data).first()
	# 	if user:
	# 		raise ValidationError('User Already Exists!')
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already taken. Please choose a different one.')

class UserForm(FlaskForm):
	username = StringField('Users Name', render_kw={"placeholder": "Jonathan HD"}, validators=[DataRequired(), Length(min=2, max=20)])
	userID = StringField("User's ID", render_kw={"placeholder": "8-digits"}, validators=[DataRequired(), Length(min=8)])
	DoB =StringField("Date of Birth", render_kw={"placeholder": "YYYY-MM-DD"}, validators=[DataRequired()])
	user_address = StringField("Home Address", validators=[DataRequired()])
	password = PasswordField('Password', render_kw={"placeholder": "5-8"}, validators=[DataRequired(), Length(min=4, max=8)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_userID(self, userID):
		user = Post.query.filter_by(userID=userID.data).first()
		if user:
			raise ValidationError('User already exists!')
	# def validate_email(self, email):
	# 	user = User.query.filter_by(email=email.data).first()
	# 	if user:
	# 		raise ValidationError('Email already taken. Please choose a different one.')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class DataColloecttionForm(FlaskForm):
	gps = RadioField('GPS Data', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice1')
	footsteps = RadioField('Foot Steps', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice1')
	game_types = SelectField('Game Type',  choices = [('gm1', 'Game 1'), 
      ('gm2', 'Game 2')], validators=[Required()])
	play_time = StringField('Played Time', validators=[DataRequired()])
	tmt_game = SelectField('TMT Type',  choices = [('gm1', 'Game 1'), 
      ('gm2', 'Game 2')], validators=[Required()])
	submit = SubmitField('Create Data')

class Notification_Init_Session_Form(FlaskForm):
	survey_name = StringField('Survey Name', validators=[DataRequired()])
	survey = TextAreaField('Survey Description', render_kw={"rows": 20, "cols": 85}, validators=[Required()])
	gps_m = RadioField('GPS', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice1')
	foot_steps = RadioField('Foot Steps', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice1')
	requiredresponse = RadioField('Required Response', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice1')
	disableback = RadioField('Disable Back Button', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice1')
	questional_label = StringField('Question Label', validators=[DataRequired()])
	questional_text = StringField('Question Text', validators=[DataRequired()])
	caption = StringField('Caption', validators=[DataRequired()])
	response = StringField('Response Option', validators=[DataRequired()])

	submit = SubmitField('Create')

class Multi_Check(FlaskForm):
	questional_label = StringField('Question Label', validators=[DataRequired()])
	questional_text = TextAreaField('Question Text', render_kw={"rows": 20, "cols": 85}, validators=[Required()])
	caption = StringField('Caption', validators=[DataRequired()])
	response_option = StringField('Response Option', validators=[DataRequired()])
	response_option_limit = StringField('Response Option Limit', validators=[DataRequired()])
	instruction = StringField('Instruction', validators=[DataRequired()])
	requiredresponse = RadioField('Required Response', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice1')
	instruction_length = StringField('Minimum Number of Instructions', validators=[DataRequired()])
	disableback = RadioField('Disable Back Button', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice1')
	submit = SubmitField('Create')

class Text_Entry(FlaskForm):
	question_label = StringField('Question Label', validators=[DataRequired()])
	question_text = TextAreaField('Question Text', render_kw={"rows": 20, "cols": 85}, validators=[Required()])
	#response_option = StringField('Response Option', validators=[DataRequired()])
	#response_option_limit = StringField('Response Option Limit', validators=[DataRequired()])
	#instruction = StringField('Instruction', validators=[DataRequired()])
	personal_identifier = RadioField('Personal Identifier', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice2')
	#required_response = StringField('Minimum Number of Instructions', validators=[DataRequired()])
	required_response = RadioField('Required Response', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice2')
	disableback = RadioField('Disable Back Button', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice2')
	submit = SubmitField('Create')

class Numeric_Entry(FlaskForm):
	questional_label = StringField('Question Label', validators=[DataRequired()])
	questional_text = TextAreaField('Question Text', render_kw={"rows": 20, "cols": 85}, validators=[Required()])
	#response_option = StringField('Response Option', validators=[DataRequired()])
	#response_option_limit = StringField('Response Option Limit', validators=[DataRequired()])
	#instruction = StringField('Instruction', validators=[DataRequired()])
	#personal_identifier = RadioField('Personal Identifier', validators=[Required()], choices=[
									#('choice1', 'Yes'), ('choice2', 'No')], default='choice2')
	#required_response = StringField('Minimum Number of Instructions', validators=[DataRequired()])
	required_response = RadioField('Required Response', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice2')
	disableback = RadioField('Disable Back Button', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice2')
	submit = SubmitField('Create')

class Text_Statement(FlaskForm):
	prompt_label = StringField('Prompt Label', validators=[DataRequired()])
	prompt_text = TextAreaField('Prompt Text', render_kw={"rows": 20, "cols": 85}, validators=[Required()])
	#response_option = StringField('Response Option', validators=[DataRequired()])
	#response_option_limit = StringField('Response Option Limit', validators=[DataRequired()])
	#instruction = StringField('Instruction', validators=[DataRequired()])
	#personal_identifier = RadioField('Personal Identifier', validators=[Required()], choices=[
									#('choice1', 'Yes'), ('choice2', 'No')], default='choice2')
	#required_response = StringField('Minimum Number of Instructions', validators=[DataRequired()])
	required_response = RadioField('Required Response', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice2')
	disableback = RadioField('Disable Back Button', validators=[Required()], choices=[
									('choice1', 'No'), ('choice2', 'No')], default='choice2')
	submit = SubmitField('Create')

class Range_Slider(FlaskForm):
	prompt_label = StringField('Question Label', validators=[DataRequired()])
	prompt_text = TextAreaField('Question Text', render_kw={"rows": 20, "cols": 85}, validators=[Required()])
	range_type = StringField('Range Type', validators=[DataRequired()])
	minimum_value = StringField('Minimum Value', validators=[DataRequired()])
	maximum_value = StringField('Maximum Value', validators=[DataRequired()])
	interval = StringField('Interval', validators=[DataRequired()])
	min_caption = StringField('Caption for Minimum Value', validators=[DataRequired()])
	max_caption = StringField('Caption for Maximum Value', validators=[DataRequired()])
	numeric_feedback = RadioField('Show Numeric Feedback', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice2')
	required_response = RadioField('Required Response', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice2')
	disableback = RadioField('Disable Back Button', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice2')
	add_trigger = RadioField('Add Trigger', validators=[Required()], choices=[
									('choice1', 'Yes'), ('choice2', 'No')], default='choice2')
	submit = SubmitField('Create')

class Datavisualization(FlaskForm):
	ids, dates = Data_Ret()
	users_id = SelectField('User ID', choices=[(index, idd) for index, idd in enumerate(ids)])
	date_id = SelectField('Select Date', choices=[(index, dat) for index, dat in enumerate(dates)])
 
