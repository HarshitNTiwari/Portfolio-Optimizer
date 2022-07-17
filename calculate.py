import PortfolioOptimizer as PortOpt

# Function to calculate portfolio 
def Calculate_portfolio(tickers):
	tickers = tickers.split()
	optimum = PortOpt.main(tickers)
	weights = optimum.x
	return weights