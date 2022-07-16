def format_output(tickers, y):
	tickers = tickers.split()
	output=""
	for i in range (len(y)-1):
		y[i]*=100
		y[i]= round(y[i],3)
		str1 = str(y[i]) + "% in " + tickers[i] + ", "
		output+=str1
	y[len(y)-1]*=100	
	y[len(y)-1]= round(y[len(y)-1],3)
	str1 = "and " + str(y[len(y)-1]) + "% in " + tickers[len(y)-1]
	output+=str1
	return output

def create_dict(tickers, weights):
	res = dict(zip(tickers, weights))
	return res