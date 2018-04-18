# python 2
#
# Homework 9, Problem 1
# Game of Life
#
# Name: Kevin Amirdjanian
#

import random

def createOneRow(width):
  """ returns one row of zeros of width "width"...  
      You should use this in your
      createBoard(width, height) function
  """
  row = []
  for col in range(width):
    row += [0]
  return row

def createBoard(width, height):
  """ returns a 2d array with "height" rows and "width" cols """
  A = []
  for row in range(height):
    A.append(createOneRow(width))    # What do you need to add a whole row here?
  return A

def printBoard(A):
  for row in A:
    line = ''
    for col in row:
      line += str(col)
    print line

def diagonalize(width, height):
  """ creates an empty board and then modifies it
      so that it has a diagonal strip of "on" cells.
  """
  A = createBoard(width, height)

  for row in range(height):
    for col in range(width):
      if row == col:
        A[row][col] = 1
      else:
        A[row][col] = 0

  return A

def innerCells(width, height):
  """ creates an empty board and then modifies it
      so that all of the border cells are "off" and
      all of the inner cells are "on".
  """
  A = createBoard(width, height)

  for row in range(1, height - 1):
    for col in range(1, width - 1):
      A[row][col] = 1

  return A

def randomCells(width, height):
  """ creates an empty board and then modifies it
      so that all of the border cells are "off" and
      all of the inner cells are randomly set to 
      either be "on" or "off".
  """
  A = createBoard(width, height)

  for row in range(1, height - 1):
    for col in range(1, width - 1):
      A[row][col] = random.choice([0, 1])

  return A

def copy(A):
  """ returns a deep copy of 2d array A """
  width = len(A[0])
  height = len(A)

  C = createBoard(width, height)

  for row in range(1, height - 1):
    for col in range(1, width - 1):
      C[row][col] = A[row][col]

  return C

def innerReverse(A):
  """ returns a deep copy of 2d array A where each 
      internal position has been reversed 
  """
  width = len(A[0])
  height = len(A)

  C = createBoard(width, height)

  for row in range(1, height - 1):
    for col in range(1, width - 1):
      if A[row][col] == 1:
        C[row][col] = 0
      else:
        C[row][col] = 1

  return C

def countNeighbors(row, col, A):
  """ returns the number of live neighbors for a cell
      in the board A at a particular row and col
  """
  count = 0

  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if A[i][j] == 1:
        if i == row and j == col:
          count += 0
        else:
          count += 1

  return count

def next_life_generation(A):
  """ makes a copy of A and then advances one
      generation of Conway's game of life within
      the *inner cells* of that copy.
      The outer edge always stays at 0.
  """
  width = len(A[0])
  height = len(A)

  newA = copy(A)

  for row in range(1, height - 1):
    for col in range(1, width - 1):
      count = countNeighbors(row, col, A)
      if count < 2:
        newA[row][col] = 0
      elif count > 3:
        newA[row][col] = 0
      elif count == 3 and A[row][col] == 0:
        newA[row][col] = 1
      else:
        newA[row][col] = A[row][col]
  
  return newA

A = [
  [0,0,0,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,0,1,0,0],
  [0,0,0,0,0],
]
A2 = next_life_generation(A)
A3 = next_life_generation(A2)

# printBoard(A)
# print ''
# printBoard(A2)
# print ''
# printBoard(A3)
# print ''

B = randomCells(8, 8)
B2 = next_life_generation(B)
B3 = next_life_generation(B2)

printBoard(B)
print ''
printBoard(B2)
print ''
printBoard(B3)
print ''
