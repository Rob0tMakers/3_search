from game import Game
from Player import Player
from box import Box
from map import Map


def algorithm(filename):
  startState, gameMap = readGame(filename)
  print("Map read.")
  queue = [startState]
  while True:  # Continue loop until a finished game state appears.
    for x in feedForward(queue.pop(0), gameMap):
      # Check if every new game state is finished. If so, close loop and return that gamestate.
      if x[-1] == 1:
        return x[2]
      queue.append(x)


def readGame(filename):
  f = open(filename, "r")
  gameMap = Map()
  boxes = []
  for y, line in enumerate(f):
    for x, icon in enumerate(line[:-1]):
      if icon == 'X':
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


def translate(directions):
  move_1 = directions.pop(0)
  start = {
      1: "North",
      2: "East",
      3: "South",
      4: "West"
  }[move_1]
  prev_move = move_1
  moves = []
  push = False
  while directions:  # While there are still more directions
    move_next = directions.pop(0)  # Look at next direction
    if move_next == -1:
      push = True
      continue
    if move_next == prev_move:
      moves.append(0)  # go straight
    # Change in direction
    elif move_next == prev_move + 1 or (move_next == 1 and prev_move == 4):
      #   if push == True:
      #     moves.append(0)
      #     # If it just pushed something, first reverse back into the last intersection
      #     moves.append(3)
      #     push = False
      #     moves.append(2)  # reverse turn
      moves.append(1)  # turn right
    elif move_next == prev_move - 1 or (move_next == 4 and prev_move == 1):
      #   if push == True:
      #     moves.append(0)
      #     # If it just pushed something, first reverse back into the last intersection
      #     moves.append(3)
      #     push = False
      #     moves.append(1)  # reverse turn
      moves.append(2)  # turn left
    elif abs(move_next - prev_move) == 2:
      # if push == True:
      #   moves.append(0)
      #   moves.append(3)
      #   moves.append(0)
      #   push = False
      # else:
      moves.append(3)  # turn 180 deg
    prev_move = move_next
  return start, moves
