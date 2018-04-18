# python 2
#
# Homework 10, Problem 3
# Markov Text Generation
#
# Name: Kevin Amirdjanian
#
import random 

def createDictionary(filename):
  """ takes in a string, the name of a text file containing sample text.
      returns a dictionary whose keys are words encountered in the text
      file and whose entries are a list of words that may legally follow
      the key word.
  """
  legalWords = {}
  endChar = ['.', '?', '!']

  f = open(filename)
  text = f.read()
  f.close()

  words = text.split()
  
  for i in range(len(words) - 1):
    if i == 0:
      legalWords['$'] = [ words[i] ]
      legalWords[ words[i] ] = [ words[i + 1] ]
    elif words[i][-1] in endChar:
      legalWords['$'] += [ words[i + 1] ]
    elif words[i] not in legalWords:
      legalWords[ words[i] ] = [ words[i + 1] ]
    else:
      legalWords[ words[i] ] += [ words[i + 1] ]
  
  return legalWords

def generateText(d, n):
  """ takes in a dictionary of word transitions d and a positive
      integer n and returns a string of n words
  """
  lenBeginningWords = len(d['$'])
  endChar = ['.', '?', '!']

  words = []
  words += [ d['$'][random.choice(range(0, lenBeginningWords))] ]

  count = 1

  while count < n:
    currentWord = words[count - 1]
    if currentWord[-1] in endChar or currentWord not in d:
      nextWord = d['$'][random.choice(range(0, lenBeginningWords))]
    else:
      lenCurrentWord = len(d[currentWord])
      nextWord = d[currentWord][random.choice(range(0, lenCurrentWord))]
    words += [ nextWord ]
    count += 1
  print len(words)
  return ' '.join(words)

hp = createDictionary('hp.txt')
t = generateText(hp, 500)

"""
Dursley drove toward town he have a cat standing on the sign; cats couldn’t read maps or mysterious, 
because her good-for-nothing husband were the first sign of a small son called Dudley good-bye but 
they were proud to say that strange or mysterious, because her sister and stared back. The Dursleys 
had a tabby cat standing on the Potters. Mr. As Mr. Mr. Dursley picked out his head around the window. 
This boy was possible to say that somebody would say that said Privet Drive, but they wanted, but they 
could he drove toward town he left the Potters away; they were the director of them noticed a little 
shake and backed out about the Potters had a secret, and Mrs. When Mr. Potter was the corner of number 
four’s drive. They didn’t have been a cat standing on the last people you’d expect to look again. Dursley 
gave himself a firm called Dudley into his briefcase, pecked Mrs. It was no finer boy anywhere. Mr. Mr. Mr. 
The Dursleys had a trick of the cat. Dursley drove toward town he drove toward town he had a trick of nothing 
except a big, beefy man with such nonsense. It must have been thinking of? As Mr. Mr. Potter was Mrs. Dursley 
picked up the Potters. The Dursleys had a screaming Dudley good-bye but they could he left the street. 
He got into his car and stared back. and put the corner and Mrs. Dursley was a large order of drills he drove
toward town he jerked his high chair. Dursley’s sister, because Dudley good-bye but missed, because Dudley into 
his most boring tie for several years; in their greatest fear was on the sign of the walls. There was Mrs. Dursley 
was on the corner of number four’s drive. Potter was now reading the road, he had a map in their opinion there 
wasn’t a child like that. The Dursleys knew that they wanted, but missed, because they had everything they just
didn’t realize what the corner and Mrs. The Dursleys knew that they didn’t realize what the cloudy sky outside to be. 
Dursley gossiped away happily as he left the walls. Potter was thin and her good-for-nothing husband were perfectly 
normal, thank you very much. The Dursleys had a firm called Dudley was another good reason for several years; in their
greatest fear was a big, beefy man with hardly any neck, which came in his briefcase, pecked Mrs. They didn’t have a 
large, tawny owl flutter past eight, Mr. Dursley blinked and Mrs. He got into his car and throwing his briefcase, pecked 
Mrs. Dursley hummed as he drove toward town he had a child like that. Dursley woke up his most boring tie for keeping 
the cat. Dursley gave himself a map in their opinion there was possible to look again. Mr. It must have been a small son 
called Dudley and Mrs. For a tabby cat reading the walls. It stared back. He got into his
"""
