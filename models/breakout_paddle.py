class Paddle:
    def __init__(self):
        self.position_x = 50
        self.width = 10
        self.height = 2

    def move_left(self):
        self.position_x -= 5

    def move_right(self):
        self.position_x += 5
