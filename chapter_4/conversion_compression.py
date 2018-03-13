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

print numToBaseB(42, 8), 'is "52"'
print numToBaseB(42, 5), 'is "132"'
print numToBaseB(42, 10), 'is "42"'
print numToBaseB(42, 2), 'is "101010"'
print numToBaseB(4, 2), 'is "100"'
print numToBaseB(4, 3), 'is "11"'
print numToBaseB(4, 4), 'is "10"'
print numToBaseB(0, 4), 'is ""'
print numToBaseB(0, 2), 'is ""'
