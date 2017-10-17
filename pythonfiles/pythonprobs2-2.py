#!/usr/bin/env python3

import sys

num=float(sys.argv[1])

if num>0:
	print(num, "is non-zero positive")
	if num>50:
		print(num, "is greater than 50")
		if not num%3:
			print(num, "is divisible by 3")
		else:
			print(num, "is not divisible by 3")
	elif num<50:
		print(num, "is less than 50")
		if not num%2:
			print(num, "is even")
		else:
			print(num, "is odd")
elif num<0:
	print(num, "is negative")
else:
	print(num, "is zero")
