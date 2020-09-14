from game import Game
from Player import Player
from box import Box
from map import Map


def algorithm(filename):
  startState, gameMap = readGame(filename)
  queue = [startState]
  while True:  # Continue loop until a finished game state appears.
    for x in feedForward(queue.pop(0), gameMap):
      # Check if every new game state is finished. If so, close loop and return that gamestate.
      if x[-1] == 1:
        return x
      queue.append(x)


def readGame(filename):
  f = open(filename, "r")
  gameMap = Map()
  boxes = []
  for y, line in enumerate(f):
    for x, icon in enumerate(line[:-1]):
      if icon == '#':
        gameMap.walls.append((x, y))
      if icon == '@':
        playerCoords = (x, y)
      if icon == '$':
        boxes.append((x, y))
      if icon == '*':
        boxes.append((x, y))
        gameMap.goals.append((x, y))
      if icon == '.':
        gameMap.goals.append((x, y))
  startState = [playerCoords, boxes, [], 0]
  return startState, gameMap


def feedForward(gameState, gameMap):
  new_states = []
  for i in range(1, 5):
    game = Game(gameState, gameMap)
    game.play(i)
    if game.getGameState() != None:
      new_states.append(game.getGameState())
  return new_states


#print(algorithm("sokoban_E.txt"))
