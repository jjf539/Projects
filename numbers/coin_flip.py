#!/usr/bin/python

import random
import sys

try:
	num_flips = int(raw_input("Enter number of times to flip coin: "))
except:
	print "Please try again and enter an integer"
	sys.exit()
heads = 0
tails = 0
while num_flips > 0:
	flip = random.randint(1,2)
	if flip == 1:
		print "Heads!"
		heads += 1
	else:
		print "Tails!"
		tails += 1
	num_flips -=1
print "Total heads: " + str(heads)
print "Total tails: " + str(tails)
