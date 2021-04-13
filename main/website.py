from flask import Flask, request, render_template, redirect, url_for
# from helper_functions import functions
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from passlib.hash import sha256_crypt
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:database123@localhost/calmdatabase'
app.debug = True
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "users"
    userId = db.Column(db.Integer(), primary_key=True, nullable=False)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    children = relationship("DailyEntries")

    def __init__(self, userId, username, password):
        self.userId = userId
        self.username = username
        self.password = password


class DailyEntries(db.Model):
    __tablename__ = "dailyEntries"
    userId = db.Column(db.Integer(), ForeignKey('users.userId'), nullable=False)
    logId = db.Column(db.Integer(), primary_key=True, nullable=False)
    logTitle = db.Column(db.String(60), nullable=False)
    logDate = db.Column(db.DateTime, nullable=False)
    logMood = db.Column(db.String(15), nullable=False)
    logRating = db.Column(db.Integer(), nullable=False)
    logDescription = db.Column(db.String(255), nullable=True)

    def __init__(self, userId, logId, logTitle, logDate, logMood, logRating, logDescription):
        self.userId = userId
        self.logId = logId
        self.logTitle = logTitle
        self.logDate = logDate
        self.logMood = logMood
        self.logRating = logRating
        self.logDescription = logDescription


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
    username = request.form.get("username")
    password = request.form.get("password")
    # check if inputs are both filled in and not blank
    # if not username or not password: <- python code
    # TODO: Handle error
    # check if username exists in the database
    # TODO: Read database
    # if it exists, prompt error
    # if it doesnt and everything is good, create a new user entry in the database
    # TODO: Use UUID to generate unique user ID's and save them to database
    unique_user_id = str(uuid.uuid4())[:8]  # creates a random 8 character user ID
    # TODO: Encrypt password
    encrypted_password = sha256_crypt.encrypt(password)
    # TODO: Write credentials to database
    # return dashboard of the user
    return render_template('dashboard.html')


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
