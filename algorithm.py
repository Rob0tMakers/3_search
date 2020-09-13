from game import Game
from Player import Player
from box import Box
from map import Map


def algorithm(filename):
  startState, gameMap = readGame(filename)
  #queue = [startState]
  queue = ['h', 'e', 'l']
  for x in feedForward(queue.pop(0)):
    queue.append(x)
  return queue


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
  return startState, gameMap


def feedForward(gameState):
  return [0, 1]
  # game = Game(gameState, gameMap)
  # for i in range(1,5):
  #   game.play(i)
  # game.getGamestate(None)
  # [valid, null, valid]

  # if game.isFinished():


print(algorithm("sokoban.txt"))
