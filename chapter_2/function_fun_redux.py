# Problem 0
def mult(n, m):
  """ 
  mult returns the product of its two inputs
  input: n and m are both integers
  output: the result upon multiplying n and m
  """
  if (m == 0):
    return 0
  
  if (m > 0):
    return n + mult(n, m - 1)
  else:
    return -(n - mult(n, m + 1))
  
#
# Tests
#
print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)

# Problem 1
def dot(list1, list2):
  """
  returns the dot product of two vectors/lists
  input: list1, list2 List[integer]
  output: integer
  """
  len1 = len(list1)
  len2 = len(list2)

  if len1 != len2:
    return 0.0
  elif len1 == len2 and len1 == 0:
    return 0.0
  else:
    return list1[0] * list2[0] + dot(list1[1:], list2[1:])

#
# Tests
#
print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] ) 
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] ) 
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] ) 
print "dot( [], [6] )           0.0 ==", dot( [], [6] ) 
print "dot( [], [] )            0.0 ==", dot( [], [] )

# Problem 2
def ind(e, L):
  """
  given a sequence L and an element e, returns the index where e is first found in L
  input: e string/integer -- L List[integer/string]
  output: integer
  """
  if not len(L) or e == L[0]:
    return 0
  else:
    return 1 + ind(e, L[1:])

#
# Tests
#
print "ind( 42, [ 55, 77, 42, 12, 42, 100 ])  2 ==", ind( 42, [ 55, 77, 42, 12, 42, 100 ])
print "ind(42, range(0,100))                  42 ==", ind(42, range(0,100))
print "ind('hi', [ 'hello', 42, True ])       3 ==", ind('hi', [ 'hello', 42, True ])
print "ind('hi', [ 'well', 'hi', 'there' ])   1 ==", ind('hi', [ 'well', 'hi', 'there' ])
print "ind('i', 'team')                       4 ==", ind('i', 'team')
print "ind(' ', 'outer exploration')          5 ==", ind(' ', 'outer exploration')

# Problem 3
def letterScore(let):
  """
  converts individual letter to scrabble score
  input: let string
  output: integer
  """
  scores = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10    
  }

  if let in scores:
    return scores[let]
  else:
    return 0

#
# Tests
#
print "letterScore('a')  1 ==", letterScore('a')
print "letterScore('f')  4 ==", letterScore('f')
print "letterScore('%')  0 ==", letterScore('%')
print "letterScore('y')  4 ==", letterScore('y')
print "letterScore('0')  0 ==", letterScore('0')
print "letterScore(' ')  0 ==", letterScore(' ')

# Problem 4
def scrabbleScore(S):
  """
  converts scrabble word to scrabble score
  input: S string
  output: integer
  """
  if len(S) == 0:
    return 0
  else:
    return letterScore(S[0]) + scrabbleScore(S[1:])

#
# Tests
#
print "scrabbleScore('quetzal'):  25 ==", scrabbleScore('quetzal')
print "scrabbleScore('jonquil'):  23 ==", scrabbleScore('jonquil')
print "scrabbleScore('syzygy'):   25 ==", scrabbleScore('syzygy')
print "scrabbleScore('abcdefghijklmnopqrstuvwxyz'):  87 ==", scrabbleScore('abcdefghijklmnopqrstuvwxyz')
print "scrabbleScore('?!@#$%^&*()'):  0 ==", scrabbleScore('?!@#$%^&*()')
print "scrabbleScore(''):          0 ==", scrabbleScore('')

# Problem 5
def one_dna_to_rna( c ):
  """ 
  converts a single-character c from DNA
  nucleotide to complementary RNA nucleotide 
  """
  nuc = {
    'A': 'U',
    'C': 'G',
    'G': 'C',
    'T': 'A'
  }

  if c in nuc:
    return nuc[c]
  else:
    return ''

def transcribe(S):
  """
  transcribes DNA sequence to complementary RNA sequence
  input: S string
  output: string
  """
  if len(S) == 0:
    return ''
  else:
    return one_dna_to_rna(S[0]) + transcribe(S[1:])

#
# Tests
#
print "transcribe('ACGT TGCA'):  'UGCAACGU' ==", transcribe('ACGT TGCA')
print "transcribe('GATTACA'):     'CUAAUGU' ==", transcribe('GATTACA')
print "transcribe('cs5') :               '' ==", transcribe('cs5')
print "transcribe('') :                  '' ==", transcribe('')
