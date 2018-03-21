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
    # print str(i), str(L[i])

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

    elif uc == '9': # we want to quit
      break

    else:
      print "That's not on the menu!"

  print
  print "Ta ta for now!"

if __name__ == '__main__':
  main()
