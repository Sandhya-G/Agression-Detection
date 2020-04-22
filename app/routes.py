from app import app
import pickle
import numpy as np
from pathlib import Path
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm,SignUp


@app.route('/')
@app.route('/index')
def index():
	# Pkl_Filename = Path("model/Pickle_KNN_Model.pkl")
	# with open(Pkl_Filename, 'rb') as file:  
	# 	Pickled_KNN_Model = pickle.load(file)
	# return str(Pickled_KNN_Model)

	return render_template('home.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}'.format(form.username.data),category='success')
		return redirect(url_for('index'))
	return render_template('login.html',form=form)

@app.route('/signup')
def signup():
	form = SignUp()
	return render_template('signup.html',form=form) 