import PortfolioOptimizer as PortOpt

def Calculate_portfolio(tickers):
	tickers = tickers.split()
	optimum = PortOpt.main(tickers)
	weights = optimum.x
	return weights