from flask import Flask, render_template, request, redirect, url_for
import pymongo
import bcrypt
import utils

app = Flask(__name__)

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

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        password = request.form['password']
        
        # Retrieve user credentials from MongoDB using your existing function
        credentials = utils.obtener_usuarios(email, password)  # This may need to include email and any other adaptations
        if credentials == "Usuario autenticado exitosamente.":
            return redirect(url_for('successfull'))
        else:
            return redirect(url_for('not_succesfull'))
    else:
        return render_template('login.html')
    
@app.route('/successfull')
def successfull():
    return render_template('successfull.html')
@app.route('/not_succesfull')
def not_succesfull():
    return render_template('not_successfull.html')
"""
@app.route('/signup', methods=['GET', 'POST'])
def signup():
        return render_template('signup.html')
"""
if __name__ == '__main__':
    app.run(debug=True)

