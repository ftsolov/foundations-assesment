from passlib.handlers.sha2_crypt import sha256_crypt
import uuid


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


def encrypt_password(password):
    return sha256_crypt.encrypt(password)


def verify_password(form_password, encrypted_password):
    return sha256_crypt.verify(form_password, encrypted_password)


def generate_id_key():
    return str(uuid.uuid4())[:8]
