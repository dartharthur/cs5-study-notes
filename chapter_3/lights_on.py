import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.

def mutate(i, oldL):
  """ Accepts an index (i) and an old list (oldL).
      mutate returns the ith element of a NEW list!
      * Note that mutate returns ONLY the ith element
        mutate thus needs to be called many times in evolve.
  """
  new_ith_element = 1 + oldL[i]
  return new_ith_element

def evolve(oldL, curgen = 0):
  """ This function should evolve oldL (a list)
      it starts at curgen, the "current" generation
      and it ends at generation #5 (for now)
      
      It works by calling mutate at each index i.
  """
  
  if allOnes(oldL):  # we're done!
    print ([i for i in range(len(oldL))]),
    print '\n',
    print oldL,                    # print the old list, L
    print "  (gen: " + str(curgen) + ")",  # and its gen.

    return curgen      # no return value... yet
  else:
    print ([i for i in range(len(oldL))]),
    print '\n',
    print oldL,                    # print the old list, L
    print "  (gen: " + str(curgen) + ")",  # and its gen.
    # user = input("Index? ") # uncomment for human input
    user = choice([i for i in range(len(oldL))]) # here is computer input
    print '\n'
    time.sleep(0.025)
    
    newL = [ mutate5(i,oldL,user) for i in range(len(oldL)) ]
    return evolve(newL, curgen + 1)

# Question 0 (given)
def mutate0(i, oldL):
  """ takes as input an index (i) and an old list (oldL)
      mutate returns the ith element of a NEW list!
      * note that mutate returns ONLY the ith element
        mutate thus needs to be called many times in evolve
  """
  new_ith_element = 2 * oldL[i]
  return new_ith_element

# Question 1
def mutate1(i, oldL):
  new_ith_element = oldL[i] ** 2
  return new_ith_element

# Question 2
def mutate2(i, oldL):
  return oldL[i - 1]

# Question 3
def mutate3(i, oldL):
  return choice([0, 1])

# evolve([1,2,3,42])

def allOnes(L):
  """ takes as input a list of numbers L
      and returns True if all of L's elements are 1
      and returns False otherwise
  """
  if L == []:
    return True
  
  if L[0] != 1:
    return False

  return allOnes(L[1:])

# print(allOnes([1,1,1]))
# print(allOnes([]))
# print(allOnes([ 0, 0, 2, 2 ]))
# print(allOnes([ 1, 1, 0 ]))

# evolve([0,0,0,0,1])
# evolve([0,1,0,1])

""" I would expect that the number of steps needed, over many trials,
    for a 5-element list to randomly generate all 1s is 32.

    At each position in the list, an element can either be 0 or 1.
    There are 5 elements in the list so the total number of permutations is
    2 ^ 5 or 32. There permutation we desire is where all elements are 1.

    On the average, I'd expect it would take 32 steps to hit this permutation.
"""

# (given)
def mutate4(i, oldL, user=0):
  """ takes as input an index (i) and an old list (oldL)
      mutate returns the ith element of a NEW list!
      * note that mutate returns ONLY the ith element
        mutate thus needs to be called many times in evolve
  """
  if i == user:
    new_ith_element = 1        # this makes the game easy!
  else:
    new_ith_element = oldL[i] # the new is the same as the old
  return new_ith_element

def mutate5(i, oldL, user=0):
  """ takes as input an index (i) and an old list (oldL)
      mutate returns the ith element of a NEW list!
      * note that mutate returns ONLY the ith element
        mutate thus needs to be called many times in evolve
  """
  if i == user or i == user - 1 or i == user + 1:
    new_ith_element = 1 - oldL[i]       # this makes the game easy!
  else:
    new_ith_element = oldL[i] # the new is the same as the old
  return new_ith_element

# evolve([1,0,0,1,0,0,1,1])
# evolve([0,0,0,0,0,0,0,0])

def randBL(N):
  """ outputs a random binary list
      (a random list of N zeroes and ones)
      input N is a nonnegative integer
      returned list should be of length N
  """
  return [ choice([0,1]) for i in range(N) ]

# print(randBL(5))
# print(randBL(9))

evolve(randBL(8))
