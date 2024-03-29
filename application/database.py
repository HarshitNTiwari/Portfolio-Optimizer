# Contains all the logic to connect to and interact with the database.
# Using the PyMongo Driver to connect to the remote MongoDB database

from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from user import User

# Connecting to the remote MongoDB instance
client = MongoClient("mongodb+srv://user:test@portfolio-optimizer.tz8df.mongodb.net/?retryWrites=true&w=majority")

portfolio_db = client.get_database("PortfolioDB") # PortfolioDB is the name of the database created in MongoDB
users_collection = portfolio_db.get_collection("users") # users is the name of the collection created in PortfolioDB database
portfolio_collection = portfolio_db.get_collection("Portfolio") # Portfolio is the name of the collection created in PortfolioDB database

# for saving user information
def save_user_info(username, email, password):	
	password_hash = generate_password_hash(password)
	users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})  #username is to be used as the primary key
 
# to fetch user data from the database
def get_user(username):
	user_data = users_collection.find_one({'_id': username})
	# returning user object
	return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None

# to save portfolio information
def save_portfolio_info(username, portfolio_dict):
	user_data = portfolio_collection.find_one({'_id': username})
	if(user_data==None):
		portfolio_collection.insert_one({'_id': username, 'stocks': [portfolio_dict]})
	else:
		portfolio_collection.update_one({'_id': username}, {'$push': {'stocks': portfolio_dict}})

# to fetch portfolio data from the database
def get_portfolio(username):
	user_data = portfolio_collection.find_one({'_id': username})
	return user_data['stocks']