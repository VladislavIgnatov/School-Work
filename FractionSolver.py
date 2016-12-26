# Author: Vladislav Ignatov
# Date: 10/29/2016
# Class: CIS 4930 Advanced Python

import re
import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
patt = '(\D\d*|\d*)/(\d*) (\D) (\D\d*|\d*)/(\d*)'

while True:
	reuslt = 0
	sList = []
	x = 0
	y = 0
	s = input("Enter Operation:")
	try:
		if s == '':
			break
		sList = re.findall(patt, s)
		op_func = ops[sList[0][2]]
		x = int(sList[0][0]) / int(sList[0][1])
		y = int(sList[0][3]) / int(sList[0][4])
		reuslt = op_func(x, y)
		print(s + ' = ' + str(reuslt))
	except IndexError as ex1:
		print("!IndexError! ", ex1)
	except KeyError as ex2:
		print("!KeyError! Wrong operator : ", ex2)
	except ValueError as ex3:
		print("!ValueError! ",ex3)
	except TypeError as ex4:
		print("!TypeError! ", ex4)
	except ZeroDivisionError as ex5:
		print("!ZeroDivisionError! ", ex5)