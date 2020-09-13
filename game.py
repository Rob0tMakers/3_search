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
    self.moveHistory = gameState[2]
    self.isFinished = False
    self.invalidMove = False

  def checkWallCollision(self, obj):
    for wall in self.gameMap.walls:
      if [obj.player.x, obj.player.y] == wall:
        return True
    return False

  def checkIfFinished(self):
    for box in self.boxes:
      if [box.x, box.y] not in self.gameMap.goals:
        return
    self.isFinished = 1

  def checkBoxCollision(self):
    return None

  def updateBoxes(self):

  def play(self, move):
    # 1 = "north", 2 = "east", 3 = "south", 4 = "west"
    player.move(move)
    self.moveHistory.append(move)

    # checks
    checkWallCollision()
    checkIfFinished()

  def getGameState(self):
    if self.invalidMove == True:
      return None
    # player, boxes, move history, isFinished(0=notFinished, 1=finished)
    return [[2, 1], [[1, 2], [2, 2], [4, 2], [4, 3], [3, 5]], [1, 2, 3, 3, 4, 5, 1, 0], 0]

 # [1 = "n", 2 = "e", 3 = "s", 4 = "w"]

 # up down left right
