# Sharp-Portfolio :chart_with_upwards_trend:

![Sharp-portfolio-gif](https://github.com/HarshitNTiwari/Portfolio-Optimizer/blob/main/Sharp-portfolio-gif.gif?raw=true)

## About the project :page_facing_up:
This project is a Web application that uses Harry Markowitz's Nobel-Prize winning [Portfolio Optimization model](https://en.wikipedia.org/wiki/Markowitz_model) to generate optimal portfolios[^1]. The user can enter the tickers of the companies they wish to invest in, and the tool will generate an optimal portfolio; it'll show you what percentage of your total capital you should invest in which company.

Some of the **key features** are:

- Users can calculate the optimal portfolio by simply entering the stock tickers.
- Users can create an account by signing up and can login if they have an existing account.
- Users can save a particular portfolio and can later view all the saved portfolios in their account.

## Using the API :left_right_arrow:

I've created an API through which you can get access to the results of the portfolio optimizer alogorithm in your application.
The response schema will be as follows:
```json
{
    "weights": array
    "returns": number 
    "volatillity": number
    "sharpe ratio": number
}
```
An example code to make a GET request in your python application:
```python
import requests, json

BASE = "http://127.0.0.1:5000/"
tickers = "MSFT NFLX INFY AMZN"
response = requests.get(BASE + "api/" + tickers)
```
The `tickers` is a space separated string of stock tickers. 
The `response` generated is a JSON object, and in this case will return a list of weights corresponding to the respective stocks.

You can get access to additional data by passing parameters in the GET request, like so:
```python
response = requests.get(BASE + "api/" + tickers, {"returns": True, "volatility": True, "sharpe_ratio": True})
```
The three additional parameters will return the percentage return, percentage risk and the [sharpe ratio](https://en.wikipedia.org/wiki/Sharpe_ratio) respectively, for the particular set of stocks. 

## Tech stack used :technologist:
- Flask (Backend framework) - for handling all the application logic
- MongoDB Atlas - to store user information and portfolio data
- HTML
- CSS

The project is [deployed](https://sharp-portfolio.herokuapp.com/) on Heroku.


## Project Structure :file_folder:
```
.
└── Portfolio-Optimizer/
    ├── application/
    │   ├── static/
    │   │   └── main.css
    │   ├── templates/
    │   │   ├── about.html
    │   │   ├── account.html
    │   │   ├── home.html
    │   │   ├── layout.html
    │   │   ├── login.html
    │   │   └── signup.html
    │   ├── app.py
    │   ├── calculate.py
    │   ├── database.py
    │   ├── format.py
    │   ├── PortfolioOptimizer.py
    │   └── user.py
    ├── .gitignore
    ├── LICENSE.md
    ├── Procfile
    ├── README.md
    └── requirements.txt
```
All the dependencies are listed inside `requirements.txt`.

Entire code for the application is inside the `application` directory.
The main portfolio optimizing algorithm is written in `PortfolioOptimizer.py` and the script for the Flask application is written in `app.py`.
`database.py` contains all the logic to interact with the database.

## Scope of Improvements :gear:
- In future I plan to make the application more interactive. Especially the 'account' section, for the users to be able to manage their protfolios more interactively.
- I also plan to make the user interface more appealing adding more javascript and possibly using React.js.
- For any feature request create an [issue](https://github.com/HarshitNTiwari/Portfolio-Optimizer/issues)

[^1]: Markowitz, H. (1952). [Portfolio Selection](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1952.tb01525.x). The Journal of Finance, 7(1), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
