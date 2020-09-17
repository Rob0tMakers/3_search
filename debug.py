from game import Game
from Player import Player
from box import Box
from map import Map
from algorithm import algorithm, readGame, feedForward

# Player can move
# Player cannot move into walls
# Player can push blocks
# Move history is transferred correctly
# Win state works.
# TO DO: double check if blocks can be pushed into walls?

startState, gameMap = readGame("sokoban_E.txt")
print(startState)
print()
print("North")
game = Game(startState, gameMap)
print(game.moveHistory)
game.play(1)
print(game.getGameState())
print()
print("East")
print("Start" + str(startState))
game1 = Game(startState, gameMap)
print(game1.moveHistory)
game1.play(2)
print(game1.getGameState())
print()
