#!/usr/bin/python

# If you do not know how basic right triangles work, read this article on wikipedia.
# MAIN GOAL
#  Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.
# SUBGOALS
#  If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side.
#  Loop the program so the user can use it more than once without having to restart the program.
import sys


print "---------- Pythagorean Triples Checker ----------"

try:
    a = int(raw_input("Please enter length of side 1: ")) 
    a2 = a*a
except:
    print "You didn't enter an integer... program exiting."
    sys.exit()
try:
    b = int(raw_input("Please enter length of side 2: "))
    b2 =b*b
except:
    print "You didn't enter an integer... program exiting."
    sys.exit()
try:
    c = int(raw_input("Please enter length of side 3: "))
    c2 = c*c
except:
    print "You didn't enter an integer... program exiting."
    sys.exit()

if a2 + b2 == c2:
    print "Right triangle"
else:
    print "not right triangle"
