#!/usr/bin/python


# Goal
# I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:
#  Allow the user to enter their question
#  Display an in progress message( i.e. "thinking")
#  Create 20 responses, and show a random response
#  Allow the user to ask another question or quit
# Bonus Using whatever module you like, add a gui. Your gui must have:
#  A box for users to enter the question
#  At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

import time
import random

responses = ["Yes", "No", "Maybe", "I don't think so", "Ask again later..."]

while True:
    rand = random.randint(0,len(responses))

    question = raw_input("What is your question? ")
    print "Hmmm.... I'm thinking..."
    time.sleep(3)

    print responses[rand]

    again = raw_input("Would you like to ask another question? (Y/N): ")
    if again.upper() == "Y":
        continue
    else:
        break
