class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self, x, y):
    self.x = x
    self.y = y

  def checkWallCollision(self):
    return None
