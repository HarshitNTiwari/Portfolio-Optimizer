from werkzeug.security import check_password_hash
from flask_login import UserMixin, AnonymousUserMixin

# User class for Flask-login
class User(UserMixin, AnonymousUserMixin):
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	# def is_authenticated(self):
	# 	return True

	# def is_active(self):
	# 	return True;

	# def is_anonymous(self):
	# 	return False

	def get_id(self):
		return self.username

	def check_password(self, password_input):
		return check_password_hash(self.password, password_input)