from game import Game

file = open("sokevo.txt", "r")


def clean(file):
    lines = []
    for line in file:
        if line.startswith(';') == True or line == ' ':
            continue
        lines.append(line[:-1])
    print(f"Outputting {len(lines)} lines")
    return lines


def readLines(lines):
    games = []

    for i, line in enumerate(lines):
        if i % 8 == 0:
            game = Game()
            for y, gameLine in enumerate(lines[i:i+8]):
                for x, icon in enumerate(gameLine):
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
            games.append(game)
    return games[:5]


file1 = clean(file)
games = readLines(file1)

print(games[0].startState.playerCoords)
print(games[0].gameMap.walls)
print()
for j in range(8):
    for i in range(8):
        if [i, j] in games[0].gameMap.walls:
            print('#', end='')
        elif [i, j] == games[0].startState.playerCoords:
            print('@', end='')
        else:
            print(' ', end='')
    print()

# y = 0
# for i, line in enumerate(file):
#     if i > 0 and i < 8:
#         for x, icon in enumerate(line[:-1]):
#             if icon == '#':
#                 walls.append([x, y])
#             if icon == '@':
#                 playerCoords = [x, y]
#             if icon == '$':
#                 boxes.append([x, y])
#             if icon == '*':
#                 boxes.append([x, y])
#                 goals.append([x, y])
#             if icon == '.':
#                 goals.append([x, y])
#         y += 1

# for y in range(8):
#     for x in range(8):
#         if [x, y] in walls:
#             print('#', end='')
#         else:
#             print(' ', end='')
#     print()
