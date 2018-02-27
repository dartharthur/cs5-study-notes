def rot(c, n):
  """ rotates a single alphabetic character by n spots
      in the alphabet
  """
  # converted value
  con = ord(c)
  # position to shift to
  pos = con + n

  isLower = (con >= 97 and con <= 122)
  isUpper = (con >= 65 and con <= 90)

  if isLower or isUpper:
    if isLower and pos > 122:
      return chr(pos % 122 + 96)
    elif isUpper and pos > 90:
      return chr(pos % 90 + 64)
    else:
      return chr(pos)
  else:
    return c

# print(rot('a', 2))
# print(rot('y', 2))
# print(rot('A', 3))
# print(rot('Y', 3))
# print(rot(' ', 4))

# given
def list_to_str( L ):
  """ L must be a list of characters; then,
      this returns a single string from them
  """
  if len(L) == 0: return ''
  return L[0] + list_to_str(L[1:])

def encipher(S, n):
  """ takes as input string S and a non-negative integer n
      between 0 and 25

      returns a new string in which the letters in S have been
      "rotated" by n characters forward in the alphabet, wrapping
      around as needed
  """
  return list_to_str([ rot(i, n) for i in S ])

print(encipher('xyza', 1))
print(encipher('Z A', 1))
print(encipher('*ab?', 1))
print(encipher('This is a string!', 1))
print(encipher('Caesar cipher? I prefer Caesar salad.', 25))
