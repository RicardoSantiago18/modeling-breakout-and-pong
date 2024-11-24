from paddle import Paddle
from ball import Ball

class Game:
    def _init_(self):
        self.paddle1 = Paddle(position_x=0, position_y=50)  # Paddle do jogador 1
        self.paddle2 = Paddle(position_x=100, position_y=50)  # Paddle do jogador 2
        self.ball = Ball()

    def start(self):
        print("Pong Game started")

    def update(self):
        self.ball.move()
        self.check_collisions()

    def check_collisions(self):
        if self.ball.check_collision(self.paddle1):
            print("Ball hit Paddle 1!")
        if self.ball.check_collision(self.paddle2):
            print("BallhitPaddle2!")