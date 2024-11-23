from breakout_paddle import Paddle
from ball import Ball
from brick import Brick

class Game:
    def __init__(self):
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = [Brick(x, y) for x in range(5) for y in range(3)]

    def start(self):
        print("Game started")

    def update(self):
        self.ball.move()
        self.check_collisions()

    def check_collisions(self):
        if self.ball.check_collision(self.paddle):
            print("Ball hit the paddle!")

        for brick in self.bricks:
            if self.ball.check_collision(brick):
                brick.hit()
