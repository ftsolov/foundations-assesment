# def fetch_data():
#     print("test")
#
# def render_dashboard():
#

def check_password(password):
    if len(password) > 6:  # check if password is more than 6 chars
        for letter in password:  # loop over letters in password
            if letter.isdigit():
                return 'true'
            else:
                print("Password does not contain number.")
    else:
        print("Password not long enough")
