from flask import Flask, render_template, request, redirect, url_for, session
#import pymongo
#import bcrypt
import utils
from flask_session import Session  # You might need to install this with pip
import os

app = Flask(__name__)
app.secret_key =  os.urandom(24) # Set a secret key for session management

app.config['SESSION_COOKIE_NAME'] = 'galletagalletametralleta'
app.config['PERMANENT_SESSION_LIFETIME'] = 60  # 1 day in seconds
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True  # Use True if your site is served over HTTPS
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        nombre = request.form['name']
        lastname=request.form['lastname']
        lastname2 = request.form['lastname2']
        nombre = nombre + " " + lastname + " " + lastname2
        email = request.form['email']  # Ensure your HTML form has a field for email
        password = request.form['password']
        
        # Insert user into MongoDB using your existing function (with any necessary modifications)
        utils.insertar_usuario(nombre,email, password)  # This may need to include email and any other adaptations
        
        # Redirect to login page after successful registration
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if utils.obtener_usuarios(email, password):  # Assuming this function exists and returns True if credentials are correct
            session['user_logged_in'] = True
            session['username'] = email
            return redirect(url_for('success'))
        else:
            return 'Login Failed'
    return render_template('login.html')  # Assuming you have a login.html template

    
@app.route('/success')
def success():
    if not session.get('user_logged_in'):
        return redirect(url_for('login'))
    if session.get('user_logged_in'):
        username = session.get('username')
        # Pass the username to the template to display user-specific information
        return render_template('successful.html', username=username)
    else:
        return 'Not logged in'


@app.route('/not_succesful')
def not_succesful():
    return render_template('not_successful.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    # Redirect to main page or login page
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

