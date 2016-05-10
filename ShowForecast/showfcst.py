### Forecast.py 
from urllib.request import urlopen

class Forecast(object):
	city = None 
	state = None
	def __init__(self,city,state):
		self.city = city.upper()
		self.state = state.lower()
		self.descTemp = []
		self.highsTemp = []
		self.lowsTemp = []
		self.overall = None

	def lows(self):
		return list(self.lowsTemp)

	def highs(self):
		return list(self.highsTemp)

	def descriptions(self):
		return list(self.descTemp)

	def overallInfo(self):
		print(self.overall)

	def getWeather(self):
		HOST = 'http://weather.noaa.gov/'
		FCST = '/pub/data/forecasts/state/'

		URL = HOST + FCST + '/' + self.state + '/' + self.state + 'z013.txt'

		try : 
			DATA = urlopen(URL)
			while True:
			    LINE = DATA.readline().decode()
			    if LINE == '':
			        break
			    LINE = LINE.replace('\n', ' ')
			    L = LINE.split(' ')
			    if 'FCST' in L:
			        LINE = DATA.readline().decode()
			        self.overall = LINE + DATA.readline().decode()
			    if self.city in L:

			        LINE = DATA.readline().decode()
			        self.overall = self.overall + LINE
			        self.desc = LINE.split(' ')
			        self.descTemp = filter(None, self.desc)
			        LINE = DATA.readline().decode()
			        self.overall = self.overall + LINE
			        temperatures = LINE.split(' ')
			        temperatures = filter(None, temperatures)
			        if temperatures is not None : 
				        for item in temperatures:
				            temp = item.split('/')
				            if len(temp) == 2: 
				                if temp[0] is not None : 
				                    self.lowsTemp.append(temp[0])

				                if temp[1] is not None : 
				                    self.highsTemp.append(temp[1])
		except : 
			print("No data found")
		
        		
