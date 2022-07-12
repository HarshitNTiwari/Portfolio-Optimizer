from flask import Flask, request, render_template, url_for, flash, redirect
import PortfolioOptimizer as PortOpt
import numpy as np

app = Flask(__name__)
app.secret_key = b'hdhcbchhh'

# list of dictionaries

@app.route('/')   #decorator for home page
def hello():
    return render_template('home.html')
 
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/predict', methods=['POST','GET'])
def calculate():
    if request.method == "POST":
        t = request.form["tickers"]
        #if input field is blank:
        # if(t==""):
        #     flash("Input field cannot be blank!", "warning")
        #     return redirect(request.referrer)
        tickers = t.split()
        print(tickers)
        optimum = PortOpt.main(tickers)
        print(optimum.x)
        y = optimum.x
        output=""
        for i in range (len(y)):
            y[i]*=100
            y[i]= round(y[i],3)
            str1 = str(y[i])
            str1+= "% in " + tickers[i] + ", "
            output+=str1
        flash("Portfolio generated successfully!", "info")
        flash("Your optimal portfolio distribution is: " + output, "info")
        return redirect(request.referrer)  # to return to the same page after form submission
    else:
        return render_template('home.html')
    


# Running in debug mode
if __name__=='__main__':
    app.run(debug=True) 