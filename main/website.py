from flask import Flask, request, render_template
from helper_functions import functions

app = Flask(__name__)


# TODO: Import SQLAlchemy library for python for easier database management

@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/sign_up_page')
def signup_page():
    # display the login page
    return render_template('signup.html')


@app.route('/sign_up')
def signup():
    # check if password meets criteria (if not, prompt error)
    # check if password repeat matches (if not, prompt error)
    # read post body
    # check if inputs are both filled in and not blank
    # check if username exists in the database
    # if it exists, prompt error
    # if it doesnt and everything is good, create a new user entry in the database
    # return dashboard of the user
    return render_template('signup.html')


@app.route('/login_page')
def login_page():
    # display the login page
    return render_template('login.html')


@app.route('/login_check')
def login_check():
    # read request body
    # check if inputs are both filled in and not blank
    # check if username exists in the database
    # get password from body request and hash it
    # compare hashed client side password with user password on server
    # if correct, display dashboard
    # if wrong, prompt again and display error message
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/fetch_daily_entries')
def fetch_daily_entries():
    pass


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
