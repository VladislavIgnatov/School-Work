# Author: Vladislav Ignatov
# Advenced Python 8/26/16 

import random

articles = ["the ", "a ", "another "]
subjects = ["cat ", "dog ", "man ", "woman "]
verbs = ["sang", "ran", "jumped", "hoped", "laughed"]
adverbs = ["loudly ", "quietly ", "well ", "badly "] 

count = 0
while count < 5:
	if random.randint(0,1) == 0:
		print (articles[random.randint(0,2)], subjects[random.randint(0,3)], verbs[random.randint(0,4)], adverbs[random.randint(0,3)])
	else: 
		print (articles[random.randint(0,2)], subjects[random.randint(0,3)], verbs[random.randint(0,4)])
	count += 1