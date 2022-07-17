# Sharp-Portfolio :chart_with_upwards_trend:

![Sharp-portfolio-gif](https://github.com/HarshitNTiwari/Portfolio-Optimizer/blob/main/Sharp-portfolio-gif.gif?raw=true)

## About the project :page_facing_up:
This project is a Web application that uses Harry Markowitz's [Portfolio Optimization model](https://en.wikipedia.org/wiki/Markowitz_model) to generate optimal portfolios. The user can enter the tickers of the companies they wish to invest in, and the tool will generate an optimal portfolio; it'll show you what percentage of your total capital you should invest in which company.

Some of the **key features** are:

- Users can calculate the optimal portfolio by simply entering the stock tickers.
- Users can create an account by signing up and can login if they have an existing account.
- Users can save a particular portfolio and can later view all the saved portfolios in their account.

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
Entire code for the application is inside the `application` directory.
The main portfolio optimizing algorithm is written in `PortfolioOptimizer.py` and the script for the Flask application is written in `app.py`.
`database.py` contains the logic to interact with the database.
