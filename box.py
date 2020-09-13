class Box:
  def __init__(self, coords):
    self.x = coords[0]
    self.y = coords[1]

  def getCoords(self):
    return (self.x, self.y)

  def move(self, move):
    # 1 = north
    if move == 1:
      self.y -= 1

    # 2 = east
    if move == 2:
      self.x += 1

    # 3 = south
    if move == 3:
      self.y += 1

    # 4 = west
    if move == 4:
      self.x -= 1
