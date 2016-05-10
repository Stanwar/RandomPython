# MCS 260 Project Three by Amanda
import sys,getopt
from collections import Counter

def get_file_data(infile):
	with open(infile, encoding='utf-8') as my_file:
		## Initialize dictionary
		wordMap = {}
		for line in my_file:
			try:
				### Split by a single space
				frequency = Counter(line.split(" "))

				for word in frequency:
					## If the key doesnt exists
					if(word in wordMap):
						wordMap[word] = int(wordMap[word]) + frequency[word]
					## if exists add frequency
					else:
						wordMap[word] = int(frequency[word])
			
			except UnicodeDecodeError:
				print("xml error")
		## Printing frequency and length
		print(wordMap)
		print("number of words : " + str(len(wordMap)))
##
# Main Function to get arguments 
##
if __name__=="__main__":
	infile = input("Give a file name : ")
	get_file_data(infile)

