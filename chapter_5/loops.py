import random

def power(b, p):
  """ loop-based power function
      inputs: numeric value (base) b, nonnegative integer (power) p
      output: the value b**p
  """
  result = 1
  for x in range(1, p + 1):
    result *= b
  return result

print "power(2,5): should be 32 ==", power(2,5)
print "power(5,2): should be 25 ==", power(5,2)
print "power(42,0): should be 1 ==", power(42,0)
print "power(0,42): should be 0 ==", power(0,42)
print "power(0,0): should be 1 ==", power(0,0)

def summedOdds(L):
  """ loop-based function to return the sum of all odd numbers in a list
      input: L, a list of integers
      output: the sum of all odd integers in list L
  """
  result = 0
  for num in L:
    if num % 2 != 0:
      result += num
  return result

print "summedOdds( [4,5,6] ): should be 5 ==", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be 24 ==", summedOdds( range(3,10) )

import random

def uniq( L ):
  """ returns whether all elements in L are unique
      input: L, a list of any elements
      output: True, if all elements in L are unique,
      or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return uniq( L[1:] ) # recursion is OK, too!

def untilARepeat(high):
  """ input: a number representing the range over which to guess, high
      output: the number of guesses needed until a guess was repeated
  """
  L = []
  count = 0
  while uniq(L):
    guess = random.choice( range(0, high) )
    L += [guess]
    count += 1
  return count

# print untilARepeat(365)
# print untilARepeat(365)
# print untilARepeat(365)
# print untilARepeat(365)

L = [ untilARepeat( 365 ) for i in range(10000) ]
print('Average num guesses until repeat is', sum(L)/10000.0)
print('Largest guess is', max(L))
print('Smallest guess is', min(L))
print('42 in L is', 42 in L)
