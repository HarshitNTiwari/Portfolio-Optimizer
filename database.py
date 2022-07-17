# Contains all the logic to connect to and interaxt with the database.

from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from user import User

client = MongoClient("mongodb+srv://user:test@portfolio-optimizer.tz8df.mongodb.net/?retryWrites=true&w=majority")

portfolio_db = client.get_database("PortfolioDB") # PortfolioDB is the name of the database created in mongoDB
users_collection = portfolio_db.get_collection("users") # users is the name of the collection created in PortfolioDB database
portfolio_collection = portfolio_db.get_collection("Portfolio")

# for saving user info
def save_user_info(username, email, password):	
	password_hash = generate_password_hash(password)
	users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})  #username is to be used as the primary key-its going to be unique
 
# to fetch user data from the database
def get_user(username):
	user_data = users_collection.find_one({'_id': username})
	return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None

# to save portfolio info
def save_portfolio_info(username, portfolio_dict):
	user_data = portfolio_collection.find_one({'_id': username})
	if(user_data==None):
		portfolio_collection.insert_one({'_id': username, 'stocks': [portfolio_dict]})
	else:
		portfolio_collection.update_one({'_id': username}, {'$push': {'stocks': portfolio_dict}})

# to fetch portfolio data from the database
def get_portfolio(username):
	user_data = portfolio_collection.find_one({'_id': username})
	# return User(user_data['id'], user_data['stocks']) if user_data else None
	return user_data['stocks']