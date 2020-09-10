class Map:
    walls = []
    goals = []


class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Game:
    def __init__(self, playerCoords):
        player = Player(playerCoords[0], playerCoords[1])
        boxes = []

    gameMap = Map()
    startState = GameState()
    game
