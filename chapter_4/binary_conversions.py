def isOdd(n):
  """ accepts single argument n and returns False is n is even
      and True is n is odd
  """
  return n % 2 == 1

# print(isOdd(42))
# print(isOdd(43))

def numToBinary(N):
  """ takes a number N and returns a string that represents that number in binary
  """
  if N == 0:
    return ''
  elif N%2 == 1:
    return numToBinary(((N - 1) / 2)) + '1'
  else:
    return numToBinary((N / 2)) + '0'

# print numToBinary(0), "is ''"
# print numToBinary(1), "is '1'"
# print numToBinary(4), "is '100'"
# print numToBinary(10), "is '1010'"
# print numToBinary(42), "is '101010'"
# print numToBinary(100), "is '1100100'"

def binaryToNum(S):
  """ takes a string S and returns a number that represents that string in decimal
  """
  if S == '':
    return 0

  # if the last digit is a '1'
  elif S[-1] == '1': 
    return (2 * binaryToNum(S[:-1])) + 1

  else: # last digit must be '0'
    return (2 * binaryToNum(S[:-1])) + 0

# print binaryToNum('100'), 'is 4'
# print binaryToNum('1011'), 'is 11'
# print binaryToNum('00001011'), 'is 11'
# print binaryToNum(''), 'is 0'
# print binaryToNum('0'), 'is 0'
# print binaryToNum('1100100'), 'is 100'
# print binaryToNum('101010'), 'is 42'

def increment(S):
  """ takes an 8-character string S of 0's and 1's and
      returns the next largest number in base 2
  """
  if S == '11111111':
    return '00000000'
  
  n = binaryToNum(S)
  x = n + 1
  y = numToBinary(x)
  return ('0' * (8 - len(y))) + y

# print increment('00000000'), "is '00000001'"
# print increment('00000001'), "is '00000010'"
# print increment('00000111'), "is '00001000'"
# print increment('11111111'), "is '00000000'"

def count(S, n):
  """ accepts an 8-character binary input string S and
      then counts n times upward from S, printing each count
  """
  print S
  if n == 0:
    return
  else:
    count(increment(S), n - 1)

# count('00000000', 4)
# count('11111110', 5)
