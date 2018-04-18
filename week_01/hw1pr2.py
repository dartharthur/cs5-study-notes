# python 2
#
# Homework 1, Problem 2
# Rock, Paper, Scissors
#
# Name: Kevin Amirdjanian
#


import random

user = raw_input('Choose your weapon: ')
comp = random.choice( ['rock', 'paper', 'scissors'] )

print 'the user (you) chose', user
print 'the comp (I) chose', comp

my_win_conditions = {
    'paper': 'rock',
    'rock': 'scissors',
    'scissors': 'paper'
}

if comp == user:
    print 'Tie.'
elif comp == my_win_conditions[user]:
    print 'You win!'
else:
    print 'I win!'
