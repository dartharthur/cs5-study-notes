# this gives us functions like sin and cos
from math import *

# two more functions (not in the math library above)
def dbl(x):
  """ doubler!  input: x, a number """
  return 2*x

def sq(x):
  """ squarer!  input: x, a number """
  return x**2

# examples for getting used to list comprehensions
def lc_mult( N ):
  """ this example takes in an int N
      and returns a list of integers
      from 0 to N-1, **each multiplied by 2**
  """
  return [ 2*x for x in range(N) ]

def lc_idiv( N ):
  """ this example takes in an int N
      and returns a list of integers
      from 0 to N-1, **each divided by 2**
      WARNING: this is INTEGER division...!
  """
  return [ x/2 for x in range(N) ]

def lc_fdiv( N ):
  """ this example takes in an int N
      and returns a list of integers
      from 0 to N-1, **each divided by 2**
      NOTE: this is floating-point division...!
  """
  return [ float(x)/2 for x in range(N) ]


# Here is where your functions start for the homework:

def unitfracs( N ):
  """ returns a list of evenly-spaced left-hand endpoints
      in the interval [0, 1)
  """
  return [ float(x)/N for x in range(N) ]

# print(unitfracs(2))
# print(unitfracs(4))
# print(unitfracs(5))
# print(unitfracs(3))
# print(unitfracs(10))

def scaledfracs(low, hi, N):
  return [ low + ((hi - low) * x) for x in unitfracs(N) ]

# print(scaledfracs(10, 30, 5))
# print(scaledfracs(41, 43, 8))
# print(scaledfracs(0, 10, 4))

def sqfracs(low, hi, N):
  """ returns a list of scaled fractions that have been squared
  """
  return [ sq(x) for x in scaledfracs(low, hi, N) ]

# print(sqfracs(4, 10, 6))
# print(sqfracs(0, 10, 5))

def f_of_fracs(f, low, hi, N):
  """ returns a list of scaled fractions, f has been applied to each fraction
  """
  return [ f(x) for x in scaledfracs(low, hi, N) ]

# print(f_of_fracs(dbl, 10, 20, 5))
# print(f_of_fracs(sq, 4, 10, 6))
# print(f_of_fracs(sin, 0, pi, 4))

def integrate(f, low, hi, N):
  """ integrate returns an estimate of the definite integral
      of the function f (the first input)
      with lower limit low (the second input)
      and upper limit hi (the third input)
      where N steps are taken (the fourth input)

      integrate simply returns the sum of the areas of rectangles
      under f, drawn at the left endpoints of N uniform steps
      from low to hi
  """
  interval = (hi - low * 1.0) / N
  return sum(f_of_fracs(f, low, hi, N)) * interval

# print(integrate(dbl, 0, 10, 4))
# print(integrate(dbl, 0, 10, 1000))
# print(integrate(sq, 0, 3, 1000000))
# print(integrate(sin, 0, pi, 1000))

""" Question 1
     
    Integrate will always underestimate the correct value of this particular
    interval because no matter how small the interval, there will always be a
    small triangle of uncalculated area between the curve and the calculated rectangles.

    A function whose integral will always be overestimated on the same interval
    is -2x because now the calculated rectangles include area that extends beyond
    the curve.
"""

def c(x):
  """ c is a semicircular function of radius two """
  return (4-x**2)**0.5

# print(integrate(c,0,2,2))
# print(integrate(c,0,2,20))
# print(integrate(c,0,2,200))
# print(integrate(c,0,2,2000))
# print(integrate(c,0,2,20000))

""" Question 2

    As N goes to infinity, the value of this integral becomes PI.
"""
