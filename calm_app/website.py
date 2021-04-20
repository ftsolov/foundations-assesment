from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_session import Session
from calm_app.helper_functions.functions import encrypt_password, verify_password, generate_id_key
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "safari"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:database123@localhost/calmdatabase'
app.debug = True
app.permanent_session_lifetime = timedelta(days=1)
db = SQLAlchemy(app)

Session(app)


class Users(db.Model):
    __tablename__ = "users"
    userId = db.Column(db.String(), primary_key=True, nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    children = relationship("DailyEntries")

    def __init__(self, userId, username, password):
        self.userId = userId
        self.username = username
        self.password = password


class DailyEntries(db.Model):
    __tablename__ = "dailyEntries"
    userId = db.Column(db.String(), ForeignKey('users.userId'), nullable=False)
    logId = db.Column(db.String(), primary_key=True, nullable=False)
    logEmoji = db.Column(db.String(), nullable=False)
    logTitle = db.Column(db.String(60), nullable=False)
    logDate = db.Column(db.DateTime(), nullable=False)
    logMood = db.Column(db.String(15), nullable=False)
    logRating = db.Column(db.Integer(), nullable=False)
    logDescription = db.Column(db.String(255), nullable=True)

    def __init__(self, userId, logId, logEmoji, logTitle, logDate, logMood, logRating, logDescription):
        self.userId = userId
        self.logId = logId
        self.logEmoji = logEmoji
        self.logTitle = logTitle
        self.logDate = logDate
        self.logMood = logMood
        self.logRating = logRating
        self.logDescription = logDescription


@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # check if password meets criteria (if not, prompt error) done in JS
        # check if password repeat matches (if not, prompt error) done in JS
        # read post body
        session.permanent = True
        username = request.form.get("username")
        password = request.form.get("password")
        # check if inputs are both filled in and not blank
        if not username or not password:
            # TODO: FLASH ERROR (?)
            return redirect(url_for('signup'))
        # check if username exists in the database
        existing_user = Users.query.filter_by(username=username).first()  # check if user already exists
        if existing_user is None:  # if user doesnt exist, create a new user in the database
            unique_user_id = generate_id_key()  # creates a random 8 character user ID
            encrypted_password = encrypt_password(password)
            user_info = Users(userId=unique_user_id, username=username, password=encrypted_password)
            db.session.add(user_info)
            db.session.commit()
            session["userId"] = user_info.userId

            return redirect(url_for('dashboard'))
        else:
            session["username"] = existing_user.username
            return redirect(url_for('login'))
            # TODO: HANDLE ERROR
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_id = session.get("userId")
    if user_id:
        return redirect(url_for("dashboard"))
    if request.method == 'POST':
        # read request body
        username = request.form.get("username")
        password = request.form.get("password")
        # check if inputs are both filled in and not blank
        if not username or not password:
            return
            # check if username exists in the database
        user_db = Users.query.filter_by(username=username).first()  # check if user already exists

        if user_db is None:
            flash("User not found, please try again.")
        else:
            # obtain hashed password that belongs to the username and store it
            server_hashed_password = user_db.password
            # compare password with hashed password on server
            password_correct_bool = verify_password(password, server_hashed_password)
            # if correct, display dashboard
            if password_correct_bool:
                session["userId"] = user_db.userId
                return redirect(url_for('dashboard'))
            else:
                # prompt error message
                # if wrong, prompt again and display error message
                pass
    else:
        # if wrong, prompt again and display error message
        return render_template('login.html')


@app.route('/logout')
def logout():
    # TODO: IMPLEMENT FLASHING PROPERLY IN HTML
    flash("You have been logged out.", "info")
    session.pop("userId", None)
    return redirect(url_for("login"))


@app.route('/dashboard')
def dashboard():
    user_id = session.get("userId")
    if user_id is None:
        return redirect(url_for("login"))
    else:
        entries = DailyEntries.query.filter_by(userId=user_id)
        return render_template('dashboard.html', entries=list(entries))


#
# @app.route('/fetch-daily-entries')
# def fetch_daily_entries():
#     # TODO: FIGURE OUT HOW TO FETCH THE ENTRIES OF THE USER
#     pass


@app.route('/submit-new-entry', methods=["POST"])
def submit_new_entry():
    # get input values
    log_id = generate_id_key()
    log_title = request.form.get("log-title")
    log_emoji = request.form.get("emoji")
    log_date = datetime.now()
    log_mood = request.form.get("mood")
    log_rating = request.form.get("rating")
    log_description = request.form.get("description")
    user_id = session.get("userId")
    # TODO: FIGURE OUT HOW TO PASS IN USER ID
    log_info = DailyEntries(userId=user_id, logId=log_id, logEmoji=log_emoji, logTitle=log_title, logDate=log_date,
                            logMood=log_mood, logRating=log_rating, logDescription=log_description)
    db.session.add(log_info)
    db.session.commit()
    return redirect(url_for('dashboard'))


@app.route('/details?id=<log_id>')
def show_entry_details(log_id):
    return render_template('entrydetails.html', entry_data=DailyEntries.query.filter_by(logId=log_id))


@app.template_filter()
def format_date(date: datetime):
    return f"{date.day:02d}.{date.month:02d}.{date.year},  {date.hour:02d}:{date.minute:02d}"


if __name__ == "__main__":
    db.create_all()
    app.run(host="localhost", port=8080, debug=True)
