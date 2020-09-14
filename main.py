from game import Game
from Player import Player
from box import Box
from map import Map
from algorithm import algorithm, translate

PUZZLE_FILE = "sokoban_E.txt"

solution_cardinal = algorithm(PUZZLE_FILE)
facing, directions = translate(solution_cardinal)

print("Facing: " + facing)
print("Move list: " + str(directions))
