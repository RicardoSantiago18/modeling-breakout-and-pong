class Brick:
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.width = 10
        self.height = 5

    def hit(self):
        print("Brick hit!")
