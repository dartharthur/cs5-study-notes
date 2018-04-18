# python 2
#
# Homework 10, Problem 1
# Virtual Art
#
# Name: Kevin Amirdjanian
#

class Date:
  """ a user-defined data structure that
      stores and manipulates dates
  """

  # the constructor is always named __init__ !
  def __init__(self, month, day, year):
    """ the constructor for objects of type Date """
    self.month = month
    self.day = day
    self.year = year


  # the "printing" function is always named __repr__ !
  def __repr__(self):
    """ This method returns a string representation for the
        object of type Date that calls it (named self).

          ** Note that this _can_ be called explicitly, but
            it more often is used implicitly via the print
            statement or simply by expressing self's value.
    """
    s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
    return s


  # here is an example of a "method" of the Date class:
  def isLeapYear(self):
    """ Returns True if the calling object is
        in a leap year; False otherwise. """
    if self.year % 400 == 0: return True
    elif self.year % 100 == 0: return False
    elif self.year % 4 == 0: return True
    return False

  def copy(self):
    """ Returns a new object with the same month, day, year
        as the calling object (self).
    """
    dnew = Date(self.month, self.day, self.year)
    return dnew
  
  def equals(self, d2):
    """ Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.
    """
    if self.year == d2.year and self.month == d2.month and self.day == d2.day:
      return True
    else:
      return False

  def tomorrow(self):
    """ changes calling object so that it represents one calendar
        day AFTER the date it originally represented
    """
    if self.isLeapYear():
      fdays = 29
    else:
      fdays = 28

    DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    currentDay = self.day
    maxDay = DIM[self.month]

    if currentDay == maxDay and self.month == 12:
      self.year += 1
      self.month = 1
      self.day = 1
    elif currentDay == maxDay:
      self.month += 1
      self.day = 1
    else:
      self.day += 1
  
  def yesterday(self):
    """ changes calling object so that it represents one calendar
        day BEFORE the date it originally represented
    """
    if self.isLeapYear():
      fdays = 29
    else:
      fdays = 28

    DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    currentDay = self.day
    firstMonth = 1
    firstDay = 1

    if currentDay == firstDay and self.month == firstMonth:
      self.year -= 1
      self.month = 12
      self.day = 31
    elif currentDay == firstDay:
      self.month -= 1
      self.day = DIM[self.month]
    else:
      self.day -= 1

  def addNDays(self, N):
    """ changes the calling object so that it represents N
        calendar days AFTER the date it originally represented
    """
    print self
    for i in range(N):
      self.tomorrow()
      print self

  def subNDays(self, N):
    """ changes the calling object so that it represents N
        calendar days BEFORE the date it originally represented
    """
    print self
    for i in range(N):
      self.yesterday()
      print self

  def isBefore(self, d2):
    """ returns True if the calling object is a calendar date BEFORE
        the argument named d2 (an object of type Date)

        returns False is self and d2 represent the same day or if
        self is AFTER d2
    """
    if self.year < d2.year:
      return True
    elif self.year == d2.year and self.month < d2.month:
      return True
    elif self.year == d2.year and self.month == d2.month and self.day < d2.day:
      return True
    else:
      return False

  def isAfter(self, d2):
    """ returns True if the calling object is a calendar date AFTER
        the argument named d2 (an object of type Date)

        returns False is self and d2 represent the same day or if
        self is BEFORE d2
    """
    if self.equals(d2):
      return False
    elif self.isBefore(d2):
      return False
    else:
      return True

  def diff(self, d2):
    """ returns an integer representing the NUMBER OF DAYS
        between self and d2
    """
    copyD1 = self.copy()
    copyD2 = d2.copy()

    count = 0

    if copyD1.equals(copyD2):
      return count

    elif copyD1.isBefore(copyD2):
      while copyD1.isBefore(copyD2):
        count += 1
        copyD1.tomorrow()
      return -count

    else:
      while copyD1.isAfter(copyD2):
        count += 1
        copyD1.yesterday()
      return count

  def dow(self):
    """ returns a string that indicates the day of the week (dow)
        of the object (of type Date) that calls it
    """
    comparator = Date(11, 12, 2014) # known to be a 'Wednesday'
    DOW = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
    diff = self.diff(comparator)
    return DOW[diff % 7]
