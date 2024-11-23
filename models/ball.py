class Ball:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.direction_x = 1
        self.direction_y = 1

    def move(self):
        self.position_x += self.direction_x
        self.position_y += self.direction_y

    def check_collision(self, obj):
        if (self.position_x == obj.position_x and
                self.position_y == obj.position_y):
            return True
        return False
