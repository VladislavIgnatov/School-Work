# Author: Vladislav Ignatov
# Advenced Python 8/26/16 

import random
import sys

articles = ["the ", "a ", "another "]
subjects = ["cat ", "dog ", "man ", "woman "]
verbs = ["sang", "ran", "jumped", "hoped", "laughed"]
adverbs = ["loudly ", "quietly ", "well ", "badly "] 
number = 5

def fullprint(x):
	count = 0
	while count < x:
		if random.randint(0,1) == 0:
			print (articles[random.randint(0,2)], subjects[random.randint(0,3)], verbs[random.randint(0,4)], adverbs[random.randint(0,3)])
		else: 
			print (articles[random.randint(0,2)], subjects[random.randint(0,3)], verbs[random.randint(0,4)])
		count += 1

try:
	if int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 10:
		number = int(sys.argv[1])
		fullprint(number)
	else:
		print("Error number must be between 1-10 inclusive.")
except IndexError:
	fullprint(number)
except ValueError as err:
    print(err)