from flask import Flask, render_template, request, redirect, url_for
import pymongo
import bcrypt

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)

