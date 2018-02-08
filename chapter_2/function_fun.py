# Problem 0 (given):
def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x

# Problem 1
def sq(x):
  """
  output: square of its input
  input x: a number (int or float)
  """
  return x ** x

# Problem 2
def interp(low, hi, fraction):
  """
  output: floating-point value that is fraction of the way between low and hi
  input low: number
  input hi: number
  input fraction: floating-point value
  """
  return low + ((hi - low) * fraction)

# Problem 3
def checkends(s):
  """
  output: boolean indicating whether first and last characters are the same
  input s: string
  """
  return s[0] == s[-1]

# Problem 4
def flipside(s):
  """
  output: string whose first half is s's second half and whose second half if s's first half
  input s: string
  """
  x = len(s) / 2
  return s[x:] + s[:x]

# Problem 5
def convertFromSeconds(s):
  """
  output: list of four nonnegative integers that represent the input in conventional units of time
  input s: nonnegative integer representing number of seconds
  """
  days = s / (24*60*60)  # # of days
  s = s % (24*60*60)     # the leftover
  hours = s / (60 * 60)
  s = s % (60 * 60)
  minutes = s / 60
  seconds = s % 60
  return [days, hours, minutes, seconds]

# Problem 6
def front3(str):
  """
  output: 3 copies of first 3 chars in str
  input str: string
  """
  return str[:3] * 3
