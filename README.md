# Sharp-Portfolio 

## About the project
This project is a Web application that uses Harry Markowiitz's [Portfolio Optimization model](https://en.wikipedia.org/wiki/Markowitz_model) to generate optimal portfolios. The user can enter the tickers of the companies they wish to invest in, and the tool will generate an optimal portfolio; it'll show you what percentage of your total capital you should invest in which company.

Some of the **key features** are:

- Users can calculate the optimal portfolio by simply entering the stock tickers.
- Users can create an account by signing up and can login if they have an existing account.
- Users can save a particular portfolio and can later view all the saved portfolios in their account.

## Tech stack used:
- Flask (Backend framework) - for handling all the application logic
- MongoDB Atlas - to store user information and portfolio data
- HTML
- CSS

The project is [deployed](https://sharp-portfolio.herokuapp.com/) on Heroku.


## Project Structure


The main portfolio optimizing algorithm is written in `PortfolioOptimizer.py` and the script for the Flask application is written in `app.py`.