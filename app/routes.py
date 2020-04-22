from app import app
import pickle
import numpy as np
from pathlib import Path
from flask import render_template,flash,redirect,url_for,request
from app.forms import LoginForm,SignUp
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app import db



@app.route('/')
@app.route('/index')
@login_required
def index():
	# Pkl_Filename = Path("model/Pickle_KNN_Model.pkl")
	# with open(Pkl_Filename, 'rb') as file:  
	# 	Pickled_KNN_Model = pickle.load(file)
	# return str(Pickled_KNN_Model)

	return render_template('home.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password',category='danger')
			return redirect(url_for('login'))
		login_user(user)
		#always use absolute path for next argument to prevent attacker from redirecting to maliciou sites
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(url_for('index'))
	return render_template('login.html',form=form)

@app.route('/signup',methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = SignUp()
	if form.validate_on_submit():
		user = User(username=form.username.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!',"success")
		return redirect(url_for('login'))
	return render_template('signup.html',  form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))