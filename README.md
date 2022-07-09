# Sharp-Optimizer
This project is a Web application that uses Harry Markowiitz's [Portfolio Optimization model](https://en.wikipedia.org/wiki/Markowitz_model) to generate optimal portfolios.
It is built using Flask.

The user can enter the tickers of the companies they wish to invest in, and the tool will generate an optimal portfolio; it'll show you what percentage of your total capital you should invest in which company.

The main portfolio optimizing algorithm is written in `PortfolioOptimizer.py` and the script for the Flask application is written in `app.py`.