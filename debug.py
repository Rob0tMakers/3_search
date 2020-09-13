from game import Game
from Player import Player
from box import Box
from map import Map
from algorithm import algorithm, readGame, feedForward

startState, gameMap = readGame("sokoban.txt")
print(startState)
print()
print("East")
game = Game(startState, gameMap)
print(game.moveHistory)
game.play(2)
print(game.getGameState())
print()
print("South")
game1 = Game(startState, gameMap)
print(game1.moveHistory)
game1.play(3)
print(game1.getGameState())
print()
