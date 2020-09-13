class Box:
  def __init__(self, coords):
    self.x = coords[0]
    self.y = coords[1]

  def move(self, x, y):
    self.x = x
    self.y = y
