from pong_paddle import Paddle
from pong_ball import Ball

class Game:
    def __init__(self, boundary=10):
        """
        Inicializa o jogo.
        :param boundary: Altura e largura do campo de jogo.
        """
        self.boundary = boundary
        self.paddle_left = Paddle(position=3, boundary=boundary)
        self.paddle_right = Paddle(position=3, boundary=boundary)
        self.ball = Ball(position=[boundary // 2, boundary // 2], direction=[-1, 1], boundary=boundary)
        self.score = [0, 0]  # Pontuação [esquerda, direita]

    def move_ball(self):
        """Move a bola, verifica colisões e atualiza o placar."""
        self.ball.move()
        print(f"A bola está na posição {self.ball.position}")

        # Verifica colisão com os paddles
        if self.ball.check_collision(self.paddle_left):
            print("A bola colidiu com o paddle esquerdo!")
        elif self.ball.check_collision(self.paddle_right):
            print("A bola colidiu com o paddle direito!")

        # Verifica colisão com as paredes
        self.ball.check_wall_collision()

        # Verifica se alguém marcou ponto
        if self.ball.position[1] < 0:  # Jogador da direita marca ponto
            self.score[1] += 1
            print(f"Jogador direito marcou ponto! Placar: {self.score[0]} - {self.score[1]}")
            self.ball.reset()
        elif self.ball.position[1] >= self.boundary:  # Jogador da esquerda marca ponto
            self.score[0] += 1
            print(f"Jogador esquerdo marcou ponto! Placar: {self.score[0]} - {self.score[1]}")
            self.ball.reset()

    def describe_game_state(self):
        """Descreve o estado atual do jogo no terminal."""
        print(f"Placar: Jogador Esquerdo {self.score[0]} - {self.score[1]} Jogador Direito")
        print(f"Posição da Bola: {self.ball.position}")
        print(f"Paddle Esquerdo: {self.paddle_left.get_positions()}")
        print(f"Paddle Direito: {self.paddle_right.get_positions()}")

    def is_game_over(self):
        """Verifica se o jogo terminou."""
        return max(self.score) >= 5
