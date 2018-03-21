import random
import math

def dartThrow():
  """ generates random x and y coordinates between -1.0 and 1.0
      input: none
      output: True if coordinates are within a circle of radius one, false if not
  """
  x = random.uniform(-1.0, 1.0)
  y = random.uniform(-1.0, 1.0)

  distToOrigin = math.sqrt(x**2 + y**2)

  if distToOrigin > 1:
    return False
  else:
    return True

# print('Dart thrown is within circle of radius 1', dartThrow())
# print('Dart thrown is within circle of radius 1', dartThrow())
# print('Dart thrown is within circle of radius 1', dartThrow())
# print('Dart thrown is within circle of radius 1', dartThrow())

def forPi(n):
  """ throws n darts at a 1 x 1 square using the throwDart() function.
      at each iteration prints the:
        - number of darts thrown so far
        - number of darts thrown so far that have hit the circle
        - the resulting estimate of pi
      input: positive integer n
      output: final resulting estimate of pi after n throws
  """
  numhits = 0
  numthrows = 0
  espit = 4
  for i in range(n):
    numthrows += 1
    if dartThrow():
      numhits += 1
    estpi = (4.0 * numhits) / numthrows
    print(str(numhits) + ' hits out of ' + str(numthrows) + ' so that pi is ' + str(estpi))
  return estpi

# print forPi(10)
# print forPi(100)
# print forPi(1000)
# print forPi(10000)
# print forPi(100000)

def whilePi(maxerror):
  """ throws darts at the dartboard (the square) until the absolute difference
      between the function's estimate of pi and the real value of pi is less
      than maxerror
      input: positive floating-point value (maxerror)
      output: number of darts thrown in order to reach the desired input accuracy
  """
  numhits = 0
  numthrows = 0
  estpi = 4
  while(abs(estpi - math.pi) > maxerror):
    numthrows += 1
    if dartThrow():
      numhits += 1
    estpi = (4.0 * numhits) / numthrows
    print(str(numhits) + ' hits out of ' + str(numthrows) + ' so that pi is ' + str(estpi))
  return numthrows

# print(whilePi(0.1))
# print(whilePi(0.01))
