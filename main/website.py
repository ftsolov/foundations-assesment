from flask import Flask, request, render_template
from helper_functions import functions

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/sign-up')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
