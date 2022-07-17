import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# On average there are 252 trading days in a year
NUM_TRADING_DAYS = 252

NUM_PORTFOLIOS = 10000

start_date = '2011-01-01'
end_date = '2022-01-01'

def download_data(stocks):
  stock_data = {}
  for stock in stocks:
    ticker = yf.Ticker(stock)
    stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']
  return pd.DataFrame(stock_data)

def calculate_return(data):
  # Normalization - we want to measure all variables in comparable metric. So we use Logarithmic returns
  log_return = np.log(data/data.shift(1))     #Daily Logarithmic return
  return log_return[1:]   #Removing the first row of returns as it has NaN values

#--------------------Generating Portfolios---------------------
def generate_portfolios(returns, stocks):
  #we'll generate random weights w to generate different portfolios
  portfolio_means=[]   #list to store means(returns)
  portfolio_risks=[]   #list to store risks(volatility)
  portfolio_weights=[]

  for _ in range(NUM_PORTFOLIOS): 
    w = np.random.random(len(stocks)) #creating random 1D array for weights with len = no. of stocks
    w /= np.sum(w)   #normalising weights so that their sum is equal to 1
    portfolio_weights.append(w)
    portfolio_means.append(np.sum(returns.mean()* w) * NUM_TRADING_DAYS)
    portfolio_risks.append(np.sqrt(np.dot(w.T, np.dot(returns.cov() * NUM_TRADING_DAYS, w))))

  return np.array(portfolio_weights) , np.array(portfolio_means) , np.array(portfolio_risks)


def statistics(weights, returns):
  portfolio_return = np.sum(returns.mean()*weights) * NUM_TRADING_DAYS
  portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))
  return np.array([portfolio_return, portfolio_volatility, portfolio_return/portfolio_volatility])

#-----------------Optimizing the Portfolios-------------------- 

#scipy optimize module can find minimum of a given function
#We need to find portfolio with max sharpe ratio.
#Max of a f(x) is min of -f(x)
def min_function_sharpe(weights, returns):
  return -statistics(weights, returns)[2]

#Constraints: Sum of weights = 1
#Scipy optimize can optimize a function like: f(x)=0
#So, for our case f(x) = sum of weights (x) -1 = 0
def optimize_portfolio(weights, returns, stocks):
  #Sum of weights =1
  constraints = {'type' : 'eq', 'fun' : lambda x: np.sum(x)-1}
  #Weights can be in the range [0,1]
  bounds = tuple((0,1) for _ in range(len(stocks)))  #for each stock a tuple (0,1) will be created
  return optimization.minimize(fun=min_function_sharpe, x0 = weights[0], args = returns, method='SLSQP', bounds=bounds, constraints=constraints)

# To print the optimal portfolio weights, returns, risk and sharpe ratio
def print_optimal_portfolio(optimum, returns):
  print("Optimal Portflio: ", optimum['x'].round(3))   #printing the optimal weights
  print("Expected return, volatility and Sharpe Ratio: ", statistics(optimum['x'].round(3), returns)) 


def main(stocks):
  dataset = download_data(stocks)

  log_daily_returns = calculate_return(dataset)
 
  #Generating 10k portfolios
  pweights, means, risks = generate_portfolios(log_daily_returns, stocks)
 
  # Getting the optimal portfolio
  return optimize_portfolio(pweights, log_daily_returns, stocks)

if __name__ == '__main__':
  import sys
  main(sys.argv[1:])
