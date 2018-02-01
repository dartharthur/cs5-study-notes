comp = 'scissors'
user = 'scissors'

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
