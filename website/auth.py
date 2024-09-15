from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        pass
    
    return render_template('/login.html')

@auth.route('/logout')
def logout():
    return "Logout"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_Name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
#PASSWORD VERIFICATION AND CHECK TEXT CODE:
        if len(email) < 4:
            flash("Email must be more than 3 characters.", category='error')
        elif len(first_Name) < 2:
            flash("First name must be more than 1 characters.", category='error')
        elif len(password1) < 7: 
            flash("password must be more than 6 characters.", category='error')
        elif password1 != password2:
            flash("password did not match.", category='error')
        else:
            new_user = User(email=email, first_Name=first_Name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully!", category='Sucess')
            
            return redirect(url_for('views.home')) #('/')


          
    return render_template('/sign_up.html')