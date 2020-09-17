from game import Game
from Player import Player
from box import Box
from map import Map
from algorithm import algorithm, translate

# For two cans (simplified, removed the walls)
PUZZLE_FILE = "competition_map_1b_e.txt"
# # For three cans (simplified map, walls removed.)
# PUZZLE_FILE = "competition_map_3_e.txt"
# # For two cans (not simple)
# PUZZLE_FILE = "competition_map_2.txt"

solution_cardinal = algorithm(PUZZLE_FILE)
facing, directions = translate(solution_cardinal)

print("Facing: " + facing)
print("Move list: " + str(directions))
