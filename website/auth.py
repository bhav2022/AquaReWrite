from flask import Blueprint, render_template, request, flash, redirect
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login-page', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login Successful', category='success')
                login_user(user, remember=True)
                return redirect('/go-to-home')
            else:
                flash('Incorrect password', category='danger')
        else:
            flash('Email does not exist.', category='danger')

    return render_template("login.html", user=current_user)

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='danger')
        elif len(email) < 4:
            flash('Email should be greater than 4 characters', category='danger')
        elif len(first_name) < 2:
            flash('Name should be loger than 1 character,', category='danger')
        elif len(last_name) < 2:
            flash('Name should be loger than 1 character,', category='danger')
        elif len(password1) < 8:
            flash('Password should atleast be 8 characters long.', category='danger')
        elif password1 != password2:
            flash("Passwords don't match.", category='danger')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Registration Successful', category='success')
            login_user(new_user, remember=True)
            return redirect('/go-to-home')
    return render_template("register.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out successfuly", category="success")
    return redirect('/login-page')