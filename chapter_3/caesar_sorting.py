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

# print(encipher('xyza', 1))
# print(encipher('Z A', 1))
# print(encipher('*ab?', 1))
# print(encipher('This is a string!', 1))
# print(encipher('Caesar cipher? I prefer Caesar salad.', 25))

def add(x, y):
  """ Returns the sum of the two arguments. """
  return x + y

# table of probabilities for each letter (given)
def letProb(c):
  """ if c is the space character or an alphabetic character,
    we return its monogram probability (for english),
    otherwise we return 1.0 We ignore capitalization.
    Adapted from
    http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
  """
  if c == ' ': return 0.1904
  if c == 'e' or c == 'E': return 0.1017
  if c == 't' or c == 'T': return 0.0737
  if c == 'a' or c == 'A': return 0.0661
  if c == 'o' or c == 'O': return 0.0610
  if c == 'i' or c == 'I': return 0.0562
  if c == 'n' or c == 'N': return 0.0557
  if c == 'h' or c == 'H': return 0.0542
  if c == 's' or c == 'S': return 0.0508
  if c == 'r' or c == 'R': return 0.0458
  if c == 'd' or c == 'D': return 0.0369
  if c == 'l' or c == 'L': return 0.0325
  if c == 'u' or c == 'U': return 0.0228
  if c == 'm' or c == 'M': return 0.0205
  if c == 'c' or c == 'C': return 0.0192
  if c == 'w' or c == 'W': return 0.0190
  if c == 'f' or c == 'F': return 0.0175
  if c == 'y' or c == 'Y': return 0.0165
  if c == 'g' or c == 'G': return 0.0161
  if c == 'p' or c == 'P': return 0.0131
  if c == 'b' or c == 'B': return 0.0115
  if c == 'v' or c == 'V': return 0.0088
  if c == 'k' or c == 'K': return 0.0066
  if c == 'x' or c == 'X': return 0.0014
  if c == 'j' or c == 'J': return 0.0008
  if c == 'q' or c == 'Q': return 0.0008
  if c == 'z' or c == 'Z': return 0.0005
  return 1.0

def stringScore(S):
  """ given a string S, returns a tuple
      the first position is the original string
      the second position is the sum of probabilites for all
      letters/characters in the string
  """
  return ( S, reduce(add, [ letProb(s) for s in S ]) )

def decipher(S):
  """ given a string S already shifted by some amount,
      returns, to the best of its ability, the original
      English string, which has been rotated by some amount
  """
  L = [ encipher(S, n) for n in range(26) ]
  # List of Tuples
  LoT = [ stringScore(x) for x in L ]
  return max(LoT, key=lambda elem:elem[1])[0]

print(decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'))
print(decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla '\
       'lclyfaopun dl ohcl slhyulk.'))
print(decipher('Onyx balks'))
