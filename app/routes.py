from app import app
import pickle
import numpy as np
from pathlib import Path
from flask import render_template,flash,redirect,url_for,request
from app.forms import LoginForm,SignUp
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from app import db
from werkzeug.urls import url_parse



@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
	if request.method == "POST":
		
		try:
			body = request.form["post-data"]
			#flash(body,category="info")
			if(len(body)>0):
				post = Post(body=body, author=current_user)
				db.session.add(post)
				db.session.commit()
				flash("New tweet was added",category="success")
			else:
				flash("Please enter something",category="info")
			return redirect(url_for('index'))
		
		except:
			db.session.rollback()
			flash("Error occured",category="danger")
	
	posts = current_user.followed_posts()
	return render_template('home.html',posts=posts)



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
	return render_template('signup.html', form=form)



@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    
    return render_template('profile.html', user=user, posts=posts)


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username),category="info")
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username),category="info")
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username),category="info")
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username),category="info")
    return redirect(url_for('user', username=username))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))