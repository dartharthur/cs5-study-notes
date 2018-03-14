def numToBaseB(N, B):
  """ takes a number N and returns a string that represents that number in base B
  """
  mod = N%B

  if N == 0:
    return ''
  elif mod != 0:
    return numToBaseB( ( (N - mod)/ B ), B ) + str(mod)
  else:
    return numToBaseB( ( (N - mod)/ B ), B ) + '0'

# print numToBaseB(42, 8), 'is "52"'
# print numToBaseB(42, 5), 'is "132"'
# print numToBaseB(42, 10), 'is "42"'
# print numToBaseB(42, 2), 'is "101010"'
# print numToBaseB(4, 2), 'is "100"'
# print numToBaseB(4, 3), 'is "11"'
# print numToBaseB(4, 4), 'is "10"'
# print numToBaseB(0, 4), 'is ""'
# print numToBaseB(0, 2), 'is ""'

def baseBToNum(S, B):
  """ takes a string S and base B where S represents a number in base B
      and returns a number that represents that string in base 10
  """
  if S == '':
    return 0
  
  elif S[-1] != 0: # last digit is anything but '0'
    return (B * baseBToNum(S[:-1], B)) + int(S[-1])

  else: # last digit must be '0'
    return (B * baseBToNum(S[:-1], B)) + int('0')

# print baseBToNum('222', 4), 'is 42'
# print baseBToNum('101010', 2), 'is 42'
# print baseBToNum('101010', 3), 'is 273'
# print baseBToNum('101010', 10), 'is 101010'
# print baseBToNum('11', 2), 'is 3'
# print baseBToNum('11', 3), 'is 4'
# print baseBToNum('11', 10), 'is 11'
# print baseBToNum('', 10), 'is 0'

def baseToBase(B1, B2, s_in_B1):
  """ takes a base B1, a base B2, and a string s_in_B1 representing a number in base B1
      returns a string representing the same number in base B2
  """
  # need to convert string in B1 to num in base 10
  # baseBToNum
  baseTen = baseBToNum(s_in_B1, B1)

  # need to convert base 10 num to string in B2
  # numToBaseB
  return numToBaseB(baseTen, B2)

# print baseToBase(2, 10, '11'), 'is "3"'
# print baseToBase(10, 2, '3'), 'is "11"'
# print baseToBase(3, 5, '11'), 'is "4"'
# print baseToBase(2, 3, '101010'), 'is "1120"'
# print baseToBase(2, 4, '101010'), 'is "222"'
# print baseToBase(2, 10, '101010'), 'is "42"'
# print baseToBase(5, 2, '4321'), 'is "1001001010"'
# print baseToBase(2, 5, '1001001010'), 'is "4321"'

def add(S, T):
  """ takes two binary strings S and T and returns their sum in binary
  """
  a = baseToBase(2, 10, S)
  b = baseToBase(2, 10, T)
  sumBaseTen = int(a) + int(b)
  return numToBaseB(sumBaseTen, 2)

# print add('11', '1'), 'is "100"'
# print add('11', '100'), 'is "111"'
# print add('110', '11'), 'is "1001"'
# print add('11100', '11110'), 'is "111010"'
# print add('10101', '10101'), 'is "101010"'
