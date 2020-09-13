from player import Player
from box import Box


class Game:
  def __init__(self, playerCoords):
    player = Player(playerCoords[0], playerCoords[1])
    boxes = []
    isFinished = 0

  def checkWallCollision(self):
    return None

  def play(self, move):
    # 1 = "north", 2 = "east", 3 = "south", 4 = "west"
    return None

  def getGameState(self):
    # player, boxes, move history, isFinished(0=notFinished, 1=finished)
    return [[2, 1], [[1, 2], [2, 2], [4, 2], [4, 3], [3, 5]], [1, 2, 3, 3, 4, 5, 1, 0], 0]

  [1 = "n", 2 = "e", 3 = "s", 4 = "w"]

  up down left right
