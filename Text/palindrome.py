#!/usr/bin/python

user_str = raw_input("Please enter a string: ").upper()
rev_str = user_str[::-1]
if user_str == rev_str:
	print "Palindrome"
else:
	print "Not palindrome"

print user_str
print rev_str
