from flask import Flask, request, render_template, url_for, flash, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from user import User

from database import get_user, save_user_info

from calculate import Calculate_portfolio
from database import get_user

app = Flask(__name__)
app.secret_key = b'hdhcbchhh'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# home page
@app.route('/')   
def home():
    return render_template('home.html')
 
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/calculate', methods=['POST','GET'])
def calculate():
    if request.method == "POST":
        tickers = request.form["tickers"]
        output = Calculate_portfolio(tickers)
        flash("Portfolio generated successfully!", "info")
        flash( output, "info")
        # return redirect(request.referrer)  # to return to the same page after form submission
        return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password_input = request.form['password']
        user = get_user(username)
        if user and user.check_password(password_input):
            login_user(user)
            message = 'Hi '+current_user.username+', You have been Logged in!'
            return redirect(url_for('home'))
        else:
            message = 'Invalid Credentials. Failed to login!'
    return render_template('login.html', message=message)

    
@app.route('/signup', methods=['POST','GET'])
def signup():
    message = ""
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password_input = request.form['password']
        if(get_user(username)!=None):
            message = 'Username already exists! Please try a different username.'
            return render_template('signup.html', message=message) 
        else:
            save_user_info(username, email, password_input)
            return redirect(url_for('login'))
    else:
        return render_template('signup.html')

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    else:
        flash("You're not Logged in!")
    return redirect(url_for('home'))



@app.route('/save', methods=['POST','GET'])
@login_required
def save_portfolio():
    return redirect(url_for('about'))


@login_manager.user_loader
def load_user(username):
    return get_user(username)


# Running in debug mode
if __name__=='__main__':
    app.run(debug=True) 