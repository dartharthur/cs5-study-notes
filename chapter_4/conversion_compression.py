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
  baseTen = baseBToNum(s_in_B1, B1)
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

# def addB(S, T):
#   """ takes two string representations of binary numbers S and T
#       returns a string representing the sum of the two input strings
#   """
#   if not len(S) or not len(T):
#     return ''

#   sum = int(S[-1]) + int(T[-1])

#   if sum == 0 or sum == 1:
#     return addB(S[:-1], T[:-1]) + str(sum)
#   else:
#     return str(sum - 1) + addB(S[:-1], T[:-1]) + '0'

# print addB('1', '0'), 'is "1"'
# print addB('11', '00'), 'is "11"'
# print addB('1', '1'), 'is "10"'
# print addB('11', '11'), 'is "110"'
# print addB('10101', '10101'), 'is "101010"'

def computeRunLength(S):
  """ takes a binary string S where all bits are the same
      outputs the run-length encoding for that string
  """
  numBitsBase10 = len(S)
  numBitsBase2 = numToBaseB(numBitsBase10, 2)
  return S[0] + ( (7 - len(numBitsBase2)) * '0' ) + numBitsBase2

# def compress(S):
#   """ takes a binary string S of length less than or equal to 64 as input
#       outputs a binary string that is the run-length encoding of the input string
#   """
#   compression = ''
#   built = ''
#   for i in range(len(S) - 1):
#     if S[i] == S[i + 1]:
#       built += S[i]
#     else:
#       print built
#       built += S[i]
#       compression += computeRunLength(built)
#       built = ''
#   return compression

# print compress('00000000'), 'is "00001000"'
# print compress('11111'), 'is "10000101"'
# Stripes = '0'*16 + '1'*16 + '0'*16 + '1'*16
# print compress(Stripes), 'is "00010000100100000001000010010000"'

def translateRunLength(C):
  """ takes a binary string C that is 8 bits long and has been compressed
      outputs the uncompressed version of that string
  """
  bit = C[0]
  num = baseBToNum(C[1:], 2)
  return num * bit

def uncompress(C):
  """ takes a binary string C which has been compressed
      and returns an uncompressed version of the string C
  """
  if not C:
    return ''
  else:
    return translateRunLength(C[:8]) + uncompress(C[8:])

print uncompress('10000101'), 'is "11111"'
print uncompress('00010000100100000001000010010000'), 'is "0000000000000000111111111111111100000000000000001111111111111111"'
