import turtle       
import random
import math
import makeFreq
from operator import itemgetter

counts = {}
def main(numberOfItems, maximumNumber, sort):

	generateCountDict(numberOfItems, maximumNumber)
	generateCircularTable(sort)

def generateCountDict(numberOfItems, maximumNumber):

	for val in range(0,numberOfItems):
		## Taking Random Value
		randValue = random.randint(1,maximumNumber)

		if(randValue in counts):
			counts[randValue] = counts[randValue] + 1
		else:
			counts[randValue] = 1

def generateCircularTable(sort):
	window = turtle.Screen() # creates a graphics window
	trtle = turtle.Turtle() # Name of the turtle
	trtle.radians()
	k = 0

	if(sort == 'y'):
		sorted_list = sorted(list(counts.values()))
		print(sorted_list)
		length = len(sorted_list)
		for i in sorted_list:
			## Get turtle back home
			trtle.home()
			## Calculate radian
			val = (2*math.pi*k/length)
			## turn left for the specific radian
			trtle.left(val)
			## Move forward proportional count
			trtle.forward(2*i)
			k = k + 1
	elif(sort == 'n') : 

		length = len(counts)
		for i in counts:
			## Get turtle back home
			trtle.home()
			
			val = (2*math.pi*k/length)
			## turn left for the specific radian
			trtle.left(val)
			## Move forward proportional count
			trtle.forward(2*counts[i])
			k = k + 1

	trtle.hideturtle
	### Exit on Click 
	window.exitonclick() 

##
# Main Function to get arguments 
##
if __name__=="__main__":
	infile = input("Give a file name : ")
	if(infile == ""):
		numberOfItems = int(input("Give the number of items  : "))
		maximumNumber = int(input("Give the largest value : "))
		sort = input("Sort the data ? (y/n) ")
		main(numberOfItems,maximumNumber,sort)
	else:
		makeFreq.get_file_data(infile)
	
	