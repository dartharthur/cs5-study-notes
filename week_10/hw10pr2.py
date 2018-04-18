# python 2
#
# Homework 10, Problem 2
# The Board Class
#
# Name: Kevin Amirdjanian
#

class Board:
  """ a datatype representing a C4 board
      with an arbitrary number of rows and cols
  """
  
  def __init__( self, width, height ):
    """ the constructor for objects of type Board """
    self.width = width
    self.height = height
    W = self.width
    H = self.height
    self.data = [ [' ']*W for row in range(H) ]

    # we do not need to return inside a constructor!
      

  def __repr__(self):
    """ this method returns a string representation
        for an object of type Board
    """
    H = self.height
    W = self.width
    s = ''   # the string to return
    for row in range(0,H):
      s += '|'   
      for col in range(0,W):
        s += self.data[row][col] + '|'
      s += '\n'

    s += (2*W+1) * '-'    # bottom of the board
    
    s += '\n'
    for i in range(W):
      s += ' '
      if i > 9:
        s += str(i % 10)
      else:
        s += str(i)
    
    return s       # the board is complete, return it

  def addMove(self, col, ox):
    """ adds a 1-character string representing the checker (ox) to the board
    """
    currentRow = self.height - 1

    while currentRow >= 0:
      if self.data[currentRow][col] == ' ':
        self.data[currentRow][col] = ox
        break
      currentRow -= 1

  def clear(self):
    """ clears the board that calls it """
    self.__init__(self.width, self.height)
  
  def setBoard( self, moveString ):
    """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.

        moveString must be a string of integers
    """
    nextCh = 'X'   # start by playing 'X'
    for colString in moveString:
      col = int(colString)
      if 0 <= col <= self.width:
        self.addMove(col, nextCh)
      if nextCh == 'X': nextCh = 'O'
      else: nextCh = 'X'

  def allowsMove(self, c):
    """ returns True if the calling object (of type Board) DOES allow
        a move into column c

        returns False if column is full or is out of bounds
    """
    if c < 0 or c > len(self.data[0]) - 1 or self.data[0][c] != ' ':
      return False
    else:
      return True

  def isFull(self):
    """ returns True if the calling object (of type Board)
        is completely full of checkers and False if not full
    """
    columnsOpen = 0
    for c in range(self.width):
      if self.allowsMove(c):
        columnsOpen += 1
    
    return columnsOpen == 0

  def delMove(self, c):
    """ removes the top checker from column c
    """
    maxRow = self.height - 1
    currentRow = 0

    while currentRow <= maxRow:
      if self.data[currentRow][c] != ' ':
        self.data[currentRow][c] = ' '
        break
      currentRow += 1

  def winsFor(self, ox):
    """ returns True if there are four checkers
        of type ox in a row on the board, False if otherwise
    """
    H = self.height
    W = self.width
    D = self.data
    # check for horizontal wins
    for row in range(0, H):
      for col in range(0, W-3):
        if D[row][col] == ox and \
          D[row][col+1] == ox and \
          D[row][col+2] == ox and \
          D[row][col+3] == ox:
          return True
    # check for vertical wins
    for row in range(0, H-3):
      for col in range(0, W):
        if D[row][col] == ox and \
          D[row+1][col] == ox and \
          D[row+2][col] == ox and \
          D[row+3][col] == ox:
          return True
    # check for south-east diagonal wins
    for row in range(0, H-3):
      for col in range(0, W-3):
        if D[row][col] == ox and \
          D[row+1][col+1] == ox and \
          D[row+2][col+2] == ox and \
          D[row+3][col+3] == ox:
          return True
    # check for north-west diagonal wins
    for row in range(0, H-3):
      for col in range(0, W-3):
        if D[row+3][col] == ox and \
          D[row+2][col+1] == ox and \
          D[row+1][col+2] == ox and \
          D[row][col+3] == ox:
          return True
    return False

  def hostGame(self):
    """ hosts a full game of Connect Four """
    print 'Welcome to Connect Four!'
    print ''
    print self
    player = 'X'
    while True:
      users_col = -1
      while self.allowsMove( users_col ) == False:
        print ''
        users_col = input("Player %s, choose a column: " % player)
      print ''
      print player, "'s choice: ", users_col
      self.addMove(users_col, player)
      print ''
      print self
      if self.winsFor(player):
        print ''
        print player, 'wins-Congratulations!'
        print ''
        print self
        self.clear()
        break
      if player == 'X':
        player = 'O'
      else:
        player = 'X'
