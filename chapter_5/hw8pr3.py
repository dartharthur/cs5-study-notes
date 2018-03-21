import math

def menu():
  """ a function that simply prints the menu """
  print
  print "(0) Input a new list"
  print "(1) Print the current list"
  print "(2) Find the average price"
  print "(3) Find the standard deviation"
  print "(4) Find the min and its day"
  print "(5) Find the max and its day"
  print "(6) Your TT investment plan"
  print "(9) Quit"
  print

def makeList(numString):
  """ a function that turns list represented by a string in a python list """
  numString = numString.replace('[', '')
  numString = numString.replace(']', '')
  numList = numString.split(',')
  L = []
  for x in numList:
    L.append(float(x.strip()))
  return L

def printList(L):
  """ input: a list of stock prices (L)
      output: no output, simply prints the list
  """
  print
  print '   Day    Price   '
  print '   ---    -----   '
  for i in range(len(L)):
    print ("%7.2f" % i), ("%7.2f" % L[i])

def sumList(L):
  """ a function that sums numbers in a list and returns the total sum """
  total = 0
  for num in L:
    total += num
  return total

def averagePrice(L):
  """ a function that returns the average price of a list of stock prices """
  return sumList(L) / len(L)

def standardDev(L):
  """ a function that returns the standard deviation of the input list of prices """
  squares = 0
  avg = averagePrice(L)
  for num in L:
    squares += (num - avg)**2
  return math.sqrt(squares / len(L))

def minDay(L):
  """ input: list of integers (L)
      output: list containing min price, and day price occurred, in that order
  """
  minPrice = None
  minDay = None

  for i in range(len(L)):
    if not minPrice:
      minPrice = L[i]
      minDay = i
    elif L[i] < minPrice:
      minPrice = L[i]
      minDay = i
  return [minPrice, minDay]

def maxDay(L):
  """ input: list of integers (L)
      output: list containing max price, and day price occurred (in that order)
  """
  maxPrice = None
  maxDay = None

  for i in range(len(L)):
    if not maxPrice:
      maxPrice = L[i]
      maxDay = i
    elif L[i] > maxPrice:
      maxPrice = L[i]
      maxDay = i
  return [maxPrice, maxDay]

def TTPlan(L):
  """ input: list of integers representing stock prices (L)
      output: list containing the day to buy on, day to sell on, and the profit (in that order)
  """
  if len(L) < 2:
    return 0
  elif L[0] > L[1]:
    minPriceDay = 1
    maxPriceDay = 1
  else:
    minPriceDay = 0
    maxPriceDay = 1
  
  maxProfitSoFar = L[maxPriceDay] - L[minPriceDay]

  for i, price in enumerate(L[2:], 2):
    if price < L[minPriceDay]:
      maxProfitSoFar = max(maxProfitSoFar, L[maxPriceDay] - L[minPriceDay])
      minPriceDay = i
      maxPriceDay = i
    elif price > L[maxPriceDay]:
      maxPriceDay = i
      maxProfitSoFar = max(maxProfitSoFar, L[maxPriceDay] - L[minPriceDay])
  
  return [ minPriceDay, maxPriceDay, maxProfitSoFar ]

def main():
  """ the main user-interaction loop """

  L = [12.00, 22.00, 32.00] # an initial list

  while True:   # the user-interaction loop
    menu()
    uc = raw_input( "Choose an option: " )

    if uc == '0': # we want to enter a new list
      numString = raw_input("Enter a new list: ")
      L = makeList(numString)

    elif uc == '1': # we want to print the current list
      printList(L)

    elif uc == '2': # we want to find the average price of the list prices
      avg = averagePrice(L)
      print 'The average price is', avg

    elif uc == '3': # we want to find the standard deviation of the list prices
      stdev = standardDev(L)
      print 'The st. deviation is', stdev

    elif uc == '4': # we want the min price and the day the price occurred
      minData = minDay(L)
      print 'The min is ', minData[0], ' on day ', minData[1]

    elif uc == '5': # we want the max price and the day the price occurred
      maxData = maxDay(L)
      print 'The max is ', maxData[0], ' on day ', maxData[1]
    
    elif uc == '6': # we want to show the day to buy, the day to sell, and the profit
      plan = TTPlan(L)
      print '** Your TTS investment strategy is to:'
      print '** '
      print '** Buy on day ' + str(plan[0]) + ' at price ' + str(L[plan[0]])
      print '** Sell on day ' + str(plan[1]) + ' at price ' + str(L[plan[1]])
      print '** '
      print '** For a total profit of ' + str(plan[2])

    elif uc == '9': # we want to quit
      break

    else:
      print "That's not on the menu!"

  print
  print "Ta ta for now!"

if __name__ == '__main__':
  main()
