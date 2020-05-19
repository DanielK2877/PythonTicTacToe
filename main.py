import random

class Cell:
  def __init__(self, down, across):
    self.content = " "
    self.down = down
    self.across = across
  def hasContent(self, content):
    return(self.content == content)
  @property
  def isFull(self):
    return(not(self.hasContent(" ")))
    return self.content != " "
    #if (self.content != " "):
    #  return True
    #else:
    #  return False
  @property
  def isXed(self):
    return(self.hasContent("X"))
    #if (self.content == "X"):
    #  return True
    #else:
    #  return False
  @property
  def isOed(self):
    if (self.content == "O"):
      return True
    else:
      return False
  def placeX(self):
    self.content = "X"
  def placeO(self):
    self.content = "O"
  def getContent(self):
    return self.content
  def printPos(self):
    print(self.down, self.across)

class Board:
  def __init__(self):
    self.spaces = [[Cell(1, 1), Cell(1, 2), Cell(1, 3)], [Cell(2, 1), Cell(2, 2), Cell(2, 3)], [Cell(3, 1), Cell(3, 2), Cell(3, 3)]]
  def winPaths(self):
    returnList = []
    possiblePath = []
    for i in range(3):
      possiblePath.append(self.spaces[i][i])
    returnList.append(possiblePath)
    possiblePath = []
    for i in range(3):
      possiblePath.append(self.spaces[i][2-i])
    returnList.append(possiblePath)
    possiblePath = []
    for i in range(3):
      for j in range(3):
        possiblePath.append(self.spaces[i][j])
      returnList.append(possiblePath)
      possiblePath = []
    for i in range(3):
      for j in range(3):
        possiblePath.append(self.spaces[j][i])
      returnList.append(possiblePath)
      possiblePath = []
    return returnList
  def printBoard(self):
    print("    1 2 3")
    for i in range(3):
      print("----------")
      print(str(i+1)+") |" + self.spaces[i][0].getContent() + "|"
                        + self.spaces[i][1].getContent() + "|"
                        + self.spaces[i][2].getContent() + "|")
    print("----------")
  def checkXVictor(self):
    xWins = False
    for path in self.winPaths():
      xWinsHere = True
      for space in path:
        if(not(space.isXed)):
          xWinsHere = False
      if(xWinsHere):
        xWins = True
    return xWins
  def checkOVictor(self):
    oWins = False
    for path in self.winPaths():
      oWinsHere = True
      for space in path:
        if(not(space.isOed)):
          oWinsHere = False
      if(oWinsHere):
        oWins = True
    return oWins
  def checkCatsGame(self):
    catsGame = True
    for row in self.spaces:
      for space in row:
        if(not(space.isFull)):
          catsGame = False
    return(catsGame)
  def isGameOver(self):
    if(self.checkOVictor()):
      print("---------------")
      print("Os Player Wins!")
      print("")
      return True
    if (self.checkXVictor()):
      print("---------------")
      print("Xs Player Wins!")
      print("")
      return True
    if(self.checkCatsGame()):
      print("---------------")
      print("Cat's Game.")
      print("")
      return True
    else:
      return False
  def xSpace(self, down, across):
    if(not(down in range(1, 4))):
      print("Row out of range!")
      return False
    elif(not(across in range(1, 4))):
      print("Column out of range!")
      return False
    elif(self.spaces[down-1][across-1].isFull):
      print("That space is already full.")
      return False
    else:
      self.spaces[down-1][across-1].placeX()
      return True
  def oSpace(self, down, across):
    if(not(down in range(1, 4))):
      print("Row out of range!")
      return False
    elif(not(across in range(1, 4))):
      print("Column out of range!")
      return False
    elif(self.spaces[down-1][across-1].isFull):
      print("That space is already full.")
      return False
    else:
      self.spaces[down-1][across-1].placeO()
      return True
  def AIOMove(self):
    legalSpaces = []
    for row in self.spaces:
      for space in row:
        if(not(space.isFull)):
          legalSpaces.append(space)
    haventPlacedO = True
    for path in self.winPaths():
      numOedSpaces = len([space for space in path if space.isOed])
      hasXSpace = any([space.isXed for space in path])
      #for space in path:
      #  if space.isXed:
      #    hasXSpace = True
      #  if space.isOed:
      #    numOedSpaces += 1
      if(numOedSpaces == 2 and not(hasXSpace)):
        for space in path:
          if(not(space.isFull)):
            spaceToGoIn = space
        if(haventPlacedO):
          spaceToGoIn.placeO()
          haventPlacedO = False
    for path in self.winPaths():
      numXedSpaces = len([space for space in path if space.isXed])
      hasOSpace = any([space.isOed for space in path])
      #for space in path:
      #  if space.isXed:
      #    hasXSpace = True
      #  if space.isOed:
      #    numOedSpaces += 1
      if(numXedSpaces == 2 and not(hasOSpace)):
        for space in path:
          if(not(space.isFull)):
            spaceToGoIn = space
        if(haventPlacedO):
          spaceToGoIn.placeO()
          haventPlacedO = False
    chosenSpace = random.choice(legalSpaces)
    if(haventPlacedO):
      chosenSpace.placeO()
      haventPlacedO = False

board = Board()
firstPlayersTurn = True
aiPlayer = True
while(not(board.isGameOver())):
  if(firstPlayersTurn):
    xUnfinished = True
    while(xUnfinished):
      board.printBoard()
      xDown = input("X player, choose a row to go in: ")
      xAcross = input("X player, choose a column to go in: ")
      if(xDown.isdigit() and xAcross.isdigit()):
        xDown = int(xDown)
        xAcross = int(xAcross)
        xUnfinished = not(board.xSpace(xDown, xAcross))
      else:
        print("Those don't seem to be numbers. Try again.")
    firstPlayersTurn = False
  else:
    if(aiPlayer):
      board.AIOMove()
    else:
      oUnfinished = True
      while(oUnfinished):
        board.printBoard()
        oDown = input("O player, choose a row to go in: ")
        oAcross = input("O player, choose a column to go in: ")
        if(oDown.isdigit() and oAcross.isdigit()):
          oDown = int(oDown)
          oAcross = int(oAcross)
          oUnfinished = not(board.oSpace(oDown, oAcross))
        else:
          print("Those don't seem to be numbers. Try again.")
    firstPlayersTurn = True
board.printBoard()