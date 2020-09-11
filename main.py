from game import Game

file = open("sokevo.txt", "r")

game = Game()

y = 0
for i, line in enumerate(file):
  if i > 0 and i < 8:
    for x, icon in enumerate(line[:-1]):
      if icon == '#':
        game.gameMap.walls.append([x, y])
      if icon == '@':
        game.startState.playerCoords = [x, y]
      if icon == '$':
        game.startState.boxes.append([x, y])
      if icon == '*':
        game.startState.boxes.append([x, y])
        game.gameMap.goals.append([x, y])
      if icon == '.':
        game.gameMap.goals.append([x, y])
  y += 1

print(game.startState.playerCoords)


def wrapperFunction(game):
  gameStates = [game.startState]


def checkGameFinished():


def pushToQueue():
