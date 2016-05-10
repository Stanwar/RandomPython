from showfcst import Forecast

def weather(city,state):
	c = Forecast(city,state)
	c.getWeather()
	print("weather forecast for " + city)
	c.overallInfo()
	print('the lows : ')
	lows = c.lows()
	print(lows)
	print('the highs : ')
	highs = c.highs()
	print(highs)
	print('descriptions of the forecast : ')
	descriptions = c.descriptions()
	print(descriptions)

if __name__=="__main__":
	city = input("Give the name of a place : ")
	state = input("Give the name of a state : ")
	weather(city,state)
	
