#!/usr/bin/python
# GOAL
# Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

# RULES
# If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# Put a blank line between each verse of the song.


import sys

bottles = 10
while bottles > 0:
    if bottles == 1:
        print "%s bottle of beer on the wall... %s bottle of beer!" % (bottles,bottles)
        print "Take one down and pass it around... no more bottles of beer on the wall!"
        print "Program finished..."
        sys.exit()
    elif bottles == 2:
        print "%s bottles of beer on the wall... %s bottles of beer!" % (bottles,bottles)
        bottles -= 1
        print "Take one down and pass it around %s bottle of beer on the wall!\n" % (bottles)

    else:
        print "%s bottles of beer on the wall... %s bottles of beer!" % (bottles,bottles)
        bottles -= 1
        print "Take one down and pass it around... %s bottles of beer on the wall!\n" % (bottles)
