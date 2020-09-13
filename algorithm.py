from game import Game
from Player import Player
from box import Box
from map import Map


def algorithm(filename):
  queue = [readGame(filename)]
  for i in queue:
    # also need to remove i. don't forget.
    queue.append(feedForward(queue[i]))


def readGame(filename):
  f = open(filename, "r")
  gameMap = Map()
  boxes = []
  for y, line in enumerate(f):
    for x, icon in enumerate(line[:-1]):
      if icon == '#':
        gameMap.walls.append([x, y])
      if icon == '@':
        playerCoords = [x, y]
      if icon == '$':
        boxes.append([x, y])
      if icon == '*':
        boxes.append([x, y])
        gameMap.goals.append([x, y])
      if icon == '.':
        gameMap.goals.append([x, y])
  startState = [playerCoords, boxes, [], 0]
  return startState


def feedForward():
  game = Game(queue[i], gameMap)
  game.play(1, 2, 3, 4)
  game.getGamestate(None)
  [valid, null, valid]

  # if game.isFinished():


print(readGame("sokoban.txt"))
