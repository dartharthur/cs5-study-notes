import random
import time

def rs():
  """ 
  rs chooses a random step and returns it 
  note that a call to rs() requires parentheses
  inputs: none at all!
  """
  return random.choice([-1,1])

def rwpos(start, nsteps):
  """
  returns the random walker's position after nsteps
  inputs: start - integer, nsteps - integer
  output: integer
  """
  if nsteps == 0:
    return start
  else:
    print "start is", start
    return rwpos(start + rs(), nsteps - 1)

# rwpos(40, 4)

def rwsteps(start, low, hi):
  """
  simulates a random walk that stops when sleepwalker reaches the low or hi value
  inputs: start - integer, low - integer, hi - integer
  output: integer representing number of steps taken
  """
  if start >= hi or start <= low:
    print '|' + (start - low) * ' ' + 'T.T' + (hi - start) * ' ' + '|'
    return 0
  else:
    print '|' + (start - low) * ' ' + 'T.T' + (hi - start) * ' ' + '|'
    time.sleep(0.1)
    return 1 + rwsteps(start + rs(), low, hi)

rwsteps(10, 5, 15)
rwsteps(10, 7, 20)