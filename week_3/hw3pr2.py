# python 2
#
# Homework 3, Problem 2
# The Sleepwalking Student
#
# Name: Kevin Amirdjanian
#

import random
import time
import sys
sys.setrecursionlimit(20000)

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

# rwsteps(10, 5, 15)
# rwsteps(10, 7, 20)

# Simulations to Analyze Random Walks

def rwposPlain(start, nsteps):
  """
  returns the random walker's position after nsteps
  inputs: start - integer, nsteps - integer
  output: integer
  """
  if nsteps == 0:
    return start
  else:
    return rwposPlain(start + rs(), nsteps - 1)

# print(rwposPlain(40, 4))

def ave_signed_displacement(numtrials, N):
  """ returns the average signed displacement for a random walker after making
      N random steps and repeated numtrials times
  """
  signed_dis = [ rwposPlain(0, N) for x in range(numtrials) ]
  return sum(signed_dis) / numtrials

print "A list of 10 signed displacements, each taken after 100 steps averaged over 5 trials is", [ave_signed_displacement(5, 100) for x in range(0, 10)]
print "A list of 10 signed displacements, each taken after 100 steps averaged over 50 trials is", [ave_signed_displacement(50, 100) for x in range(0, 10)]
print "A list of 10 signed displacements, each taken after 100 steps averaged over 500 trials is", [ave_signed_displacement(500, 100) for x in range(0, 10)]
print "A list of 10 signed displacements, each taken after 100 steps averaged over 5000 trials is", [ave_signed_displacement(5000, 100) for x in range(0, 10)]

print "A list of 10 signed displacements, each taken after 1000 steps averaged over 5 trials is", [ave_signed_displacement(5, 1000) for x in range(0, 10)]
print "A list of 10 signed displacements, each taken after 1000 steps averaged over 50 trials is", [ave_signed_displacement(50, 1000) for x in range(0, 10)]
print "A list of 10 signed displacements, each taken after 1000 steps averaged over 500 trials is", [ave_signed_displacement(500, 1000) for x in range(0, 10)]
print "A list of 10 signed displacements, each taken after 1000 steps averaged over 5000 trials is", [ave_signed_displacement(5000, 1000) for x in range(0, 10)]

def ave_squared_displacement(numtrials, N):
  """ returns the average squared displacement for a random walker after making
      N random steps and repeated numtrials times
  """
  squared_dis = [ rwposPlain(0, N)**2 for x in range(numtrials) ]
  return sum(squared_dis) / numtrials

print "A list of 10 squared displacements, each taken after 100 steps averaged over 5 trials is", [ave_squared_displacement(5, 100) for x in range(0, 10)]
print "A list of 10 squared displacements, each taken after 100 steps averaged over 50 trials is", [ave_squared_displacement(50, 100) for x in range(0, 10)]
print "A list of 10 squared displacements, each taken after 100 steps averaged over 500 trials is", [ave_squared_displacement(500, 100) for x in range(0, 10)]
print "A list of 10 squared displacements, each taken after 100 steps averaged over 5000 trials is", [ave_squared_displacement(5000, 100) for x in range(0, 10)]

print "A list of 10 squared displacements, each taken after 1000 steps averaged over 5 trials is", [ave_squared_displacement(5, 1000) for x in range(0, 10)]
print "A list of 10 squared displacements, each taken after 1000 steps averaged over 50 trials is", [ave_squared_displacement(50, 1000) for x in range(0, 10)]
print "A list of 10 squared displacements, each taken after 1000 steps averaged over 500 trials is", [ave_squared_displacement(500, 1000) for x in range(0, 10)]
print "A list of 10 squared displacements, each taken after 1000 steps averaged over 5000 trials is", [ave_squared_displacement(5000, 1000) for x in range(0, 10)]

""" In order to compute the average signed displacement for
    a random walker after 100 random steps, 
    I computed the signed displacement after 100 random steps numtrials times 
    and took the average of all of these.

    I found that as both N steps and numtrials trials increased, the average signed displacement
    is approximately equal to 0. At any given time you have a 50/50 chance of either moving left or right.
    Given enough steps and trials, you should make approximately as many left movements as right movements which will leave you
    at or near your starting point.
"""
""" In order to compute the average squared displacement for
    a random walker after 100 random steps,
    I computed the squared displacement after 100 random steps numtrials times 
    and took the average of all of these.

    I found that as both N steps and numtrials trials increased, the average squared displacement
    is approximately equal to N steps. Following the logic above, at any given time you have a 
    50/50 chance of either moving left or right. Each time you move left or right, you square the distance from the start.
    Whether our current position is to the left or right of start, our squared displacement will be a positive number.

    Given enough steps and trials, our signed displacement will average to around 0.

    If over time the average signed displacement is at or near zero, then it follows that the
    average squared displacement is at or near N steps because each time we take a step, our average movement
    away from the origin is 1 or -1, which squares to 1, and the sum of all of these movements will be approximately
    N steps.
"""
