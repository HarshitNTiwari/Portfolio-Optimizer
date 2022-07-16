from flask import Flask, request, render_template, url_for, flash, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from user import User

from calculate import Calculate_portfolio
from format import format_output, create_dict
from database import get_user, save_user_info, save_portfolio_info

app = Flask(__name__)
app.secret_key = b'hdhcbchhh'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

ticker = []
weigh = []

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
        weights = Calculate_portfolio(tickers)
        weigh.append(weights)
        ticker.append(tickers)
        output = format_output(tickers, weights)
        flash("Portfolio generated successfully!", "info")
        flash( "Your optimal portfolio distribution is: "+output, "info")
        # return redirect(request.referrer)  # to return to the same page after form submission
        return redirect(url_for('home'))
def give_list():
    return tickers, weights


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
    weights = weigh.pop()
    tickers = ticker.pop()
    username = current_user.get_id()
    print(username)
    print(weights)
    print(tickers)
    if(len(weights)!=0):
        tickers = tickers.split()
        portfolio_dict = create_dict(tickers, weights)
        print(portfolio_dict)
        save_portfolio_info(username, portfolio_dict)
        flash('Portfolio saved Successfully!')
    else:
        flash('Please create a portfolio first!')
    return redirect(url_for('home'))

@app.route('/account', methods=['POST','GET'])
@login_required
def account():
    return render_template('account.html')


@login_manager.user_loader
def load_user(username):
    return get_user(username)


# Running in debug mode
if __name__=='__main__':
    app.run(debug=True) 