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
      English string
  """
  L = [ encipher(S, n) for n in range(26) ]
  # List of Tuples
  LoT = [ stringScore(x) for x in L ]
  return max(LoT, key=lambda elem:elem[1])[0]

# print(decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'))
# print(decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla '\
#        'lclyfaopun dl ohcl slhyulk.'))
# print(decipher('Onyx balks'))

def count(e, L):
  """returns the number of times that e appears in L"""
  return len([ x for x in L if e == x ])

def blsort(L):
  """ takes in a list L and outputs a list
      with the same elements as L, but in ascending order
      blsort only needs to handle lists of binary digits
  """
  numZeroes = count(0, L)
  numOnes = count(1, L)
  return [ 0 for i in range(numZeroes) ] + [ 1 for i in range(numOnes) ]

# print(blsort( [1, 0, 1] ))
# L = [1, 0, 1, 0, 1, 0, 1]
# print(blsort(L))

def remOne(i, L):
  """ given an index and a list (or string),
      removes an element from the list at the given index
      and returns a list (or string) of the remaining elements
  """
  return L[:i] + L[i + 1:]

def gensort(L):
  """ general-purpose sorting function
      takes in a list L and should output a list
      with the same elements as L, but in ascending order
  """
  if not L:
    return []
  
  maxNum = max(L)

  return gensort(remOne(L.index(maxNum), L)) + [ maxNum ]

# print(gensort( [42, 1, 3.14] ))
# L = [7, 9, 4, 3, 0, 5, 2, 6, 1, 8]
# print(gensort(L))

def jscore(S, T):
  """ takes in two strings, S and T.
      outputs the "jotto score" of S compared with T.
      the "jotto score" is the number of characters in S that
      are shared by T.
  """
  if not S or not T:
    return 0
  
  if S[0] in T:
    i = T.index(S[0])
    return 1 + jscore(S[1:], remOne(i, T))
  else:
    return jscore(S[1:], T)

# print jscore( 'diner', 'syrup' ), 'is 1'
# print jscore( 'geese', 'elate' ), 'is 2'
# print jscore( 'gattaca', 'aggtccaggcgc' ), 'is 5'
# print jscore( 'gattaca', '' ), 'is 0'

def exact_change(target_amount, L):
  """ input target_amount is a single non-negative integer value
      input L is a list of positive integer values
      exact_change returns True if it's possible to create target_amount
      by adding up some-or-all of the values in L, and False if it's not possible
  """
  if target_amount == 0:
    return True
  elif target_amount < 0:
    return False
  elif not L:
    return False

  useit = exact_change(target_amount - L[0], L[1:])
  loseit = exact_change(target_amount, L[1:])

  return useit or loseit

# print exact_change( 42, [25, 1, 25, 10, 5, 1] ), 'is True'
# print exact_change( 42, [25, 1, 25, 10, 5] ), 'is False'
# print exact_change( 42, [23, 1, 23, 100] ), 'is False'
# print exact_change( 42, [23, 17, 2, 100] ), 'is True'
# print exact_change( 42, [25, 16, 2, 15] ), 'is True'
# print exact_change( 0, [4, 5, 6] ), 'is True'
# print exact_change( -47, [4, 5, 6] ), 'is False'
# print exact_change( 0, [] ), 'is True'
# print exact_change( 42, [] ), 'is False'

def LCS(S, T):
  """ takes in two strings S and T.
      LCS outputs the longest common subsequence (LCS) that S and T share.
      the LCS will be a string whose letters are a subsequence of S and
      a subsequence of T (they must appear in the same order, though not
      necessarily consecutively, in those input strings).
  """
  if not S or not T:
    return ''

  if S[0] == T[0]:
    return S[0] + LCS( S[1:], T[1:] )
  else:
    result1 = LCS( S[1:], T )
    result2 = LCS( S, T[1:] )

    len1 = len(result1)
    len2 = len(result2)

    if len1 > len2:
      return result1
    else:
      return result2

# print LCS( 'human', 'chimp' ), 'is hm'
# print LCS( 'gattaca', 'tacgaacta' ), 'is gaaca'
# print LCS( 'wow', 'whew' ), 'is ww'
# print LCS( '', 'whew' ), 'is '   # first input is the empty string
# print LCS( 'abcdefgh', 'efghabcd' ), 'is abcd'

def make_change(target_amount, L):
  """ input target_amount is a single non-negative integer value
      input L is a list of positive integer values
      make_change returns a list of coins that add up to the target amount,
      assuming it's possible to create target_amount,
      by adding up some-or-all of the values in L, and False if it's not possible
  """
  if target_amount == 0:
    return []
  elif target_amount < 0:
    return [ False ]
  elif not L:
    return [ False ]
  
  useit = [ L[0] ] + make_change(target_amount - L[0], L[1:])
  loseit = make_change(target_amount, L[1:])

  if useit[-1]:
    return useit
  elif loseit[-1]:
    return loseit
  else:
    return [ False ]

# solutions are generally correct however in the false cases,
# I am returning a list with a single value False when I should really
# just return False

print sorted( make_change( 42, [25, 1, 25, 10, 5, 1] ) ), 'is [1, 1, 5, 10, 25]'
print make_change( 42, [25, 1, 25, 10, 5] ), 'is False'
print make_change( 42, [23, 1, 23, 100] ), 'is False'
print sorted( make_change( 42, [23, 17, 2, 100] ) ), 'is [2, 17, 23]'
print sorted( make_change( 42, [25, 16, 2, 15] ) ), 'is [2, 15, 25]'
print make_change( 0, [4, 5, 6] ), 'is []'
print make_change( -47, [4, 5, 6] ), 'is False'
print make_change( 0, [] ), 'is []'
print make_change( 42, [] ), 'is False'
