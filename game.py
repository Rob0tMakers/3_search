from Player import Player
from box import Box


class Game:
  def __init__(self, gameState, gameMap):
    # instantiate player
    self.player = Player(gameState[0])
    # instantiate boxes
    self.boxes = []
    for boxCoords in gameState[1]:
      self.boxes.append(Box(boxCoords))
    # save gameMap
    self.gameMap = gameMap
    # game status
    self.moveHistory = gameState[2].copy()
    self.isFinished = 0

  def checkIfFinished(self):
    if set(self.getBoxCoords()) == set(self.gameMap.goals):
      return 1
    else:
      return 0

  def isGameOver(self):
    for box in self.getBoxCoords():
      adjacentWallCount = 0
      for wall in self.gameMap.walls:
        if wall[0] == (box[0] + 1 or box[0] - 1):
          adjacentWallCount += 1
        if wall[1] == (box[1] + 1 or box[1] - 1):
          adjacentWallCount += 1
      if adjacentWallCount > 1 and box not in self.gameMap.goals:
        return True

    return False

  def checkWallCollision(self):
    for wall in self.gameMap.walls:
      if self.player.getCoords() == wall:
        return True
      for box in self.boxes:
        if box.getCoords() == wall:
          return True
    return False

  def checkBoxCollision(self):
    uniqueBoxes = set(self.getBoxCoords())
    if len(uniqueBoxes) < len(self.boxes):
      return True
    return False

  def moveBoxes(self):
    for box in self.boxes:
      if self.player.getCoords() == box.getCoords():
        box.move(self.moveHistory[-1])

  def getBoxCoords(self):
    boxes = []
    for box in self.boxes:
      boxes.append(box.getCoords())
    return boxes

  def play(self, move):
    # player moves
    self.player.move(move)
    self.moveHistory.append(move)

    # box gets pushed
    self.moveBoxes()

    self.isFinished = self.checkIfFinished()

  def getGameState(self):
    # or self.isGameOver() == True:
    if self.checkWallCollision() == True or self.checkBoxCollision() == True:
      return None
    # player, boxes, move history, isFinished(0=notFinished, 1=finished)
    return [self.player.getCoords(), self.getBoxCoords(), self.moveHistory, self.isFinished]
