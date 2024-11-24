class Paddle:
    def _init_(self, position_x=0, position_y=0):
        self.position_x = position_x
        self.position_y = position_y
        self.width = 2
        self.height = 10

    def move_up(self):
        self.position_y -= 5

    def move_down(self):
        self.position_y+=5