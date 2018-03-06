# Given the number 0 and the following four consecutive powers of two:
# 2**0 
# 2**1 
# 2**2
# 2**3
# Write as many of the numbers 0, 1, 2, and so forth as you can.False

zero = 0
one = 2**0
two = 2**1
three = 2**1 + 2**0
four = 2**2
five = 2**2 + 2**0
six = 2**2 + 2**1
seven = 2**2 + 2**1 + 2**0
eight = 2**3
nine = 2**3 + 2**0
ten = 2**3 + 2**1
eleven = 2**3 + 2**1 + 2**0
twelve = 2**3 + 2**2
thirteen = 2**3 + 2**2 + 2**0
fourteen = 2**3 + 2**2 + 2**1
fifteen = 2**3 + 2**2 + 2**1 + 2**0

print zero, 'is 0'
print one, 'is 1'
print two, 'is 2'
print three, 'is 3'
print four, 'is 4'
print five, 'is 5'
print six, 'is 6'
print seven, 'is 7'
print eight, 'is 8'
print nine, 'is 9'
print ten, 'is 10'
print eleven, 'is 11'
print twelve, 'is 12'
print thirteen, 'is 13'
print fourteen, 'is 14'
print fifteen, 'is 15'

def printASCII():
  """prints all 256 ASCII symbols"""
  for i in range(256):
    print chr(i)

printASCII()
