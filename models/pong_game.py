from pong_paddle import Paddle


class Game:
    def __init__(self, boundary=10):
        """
        Inicializa o jogo.
        :param boundary: Altura do campo de jogo.
        """
        self.boundary = boundary
        self.paddle_left = Paddle(position=3, boundary=boundary)
        self.paddle_right = Paddle(position=3, boundary=boundary)
        self.ball_position = [boundary // 2, boundary // 2]  # Meio do campo
        self.ball_direction = [-1, 1]  # Direção da bola [vertical, horizontal]
        self.score = [0, 0]  # Pontuação [esquerda, direita]

    def move_ball(self):
        """Atualiza a posição da bola e verifica colisões."""
        next_position = [
            self.ball_position[0] + self.ball_direction[0],
            self.ball_position[1] + self.ball_direction[1]
        ]

        # Descreve o movimento da bola
        print(f"A bola se move de {self.ball_position} para {next_position}")

        # Verifica colisão com bordas verticais
        if next_position[0] < 0 or next_position[0] >= self.boundary:
            self.ball_direction[0] *= -1  # Inverte a direção vertical
            print("A bola atingiu a borda vertical e inverteu a direção.")

        # Verifica colisão com os paddles
        if next_position[1] == 1 and next_position[0] in self.paddle_left.get_positions():
            self.ball_direction[1] *= -1  # Inverte direção horizontal
            print("A bola atingiu o paddle esquerdo!")
        elif next_position[1] == self.boundary - 2 and next_position[0] in self.paddle_right.get_positions():
            self.ball_direction[1] *= -1  # Inverte direção horizontal
            print("A bola atingiu o paddle direito!")

        # Verifica pontuação
        if next_position[1] < 0:  # Jogador da direita marca ponto
            self.score[1] += 1
            print(f"Jogador direito marca ponto! Placar: {self.score[0]} - {self.score[1]}")
            self.reset_ball()
        elif next_position[1] >= self.boundary:  # Jogador da esquerda marca ponto
            self.score[0] += 1
            print(f"Jogador esquerdo marca ponto! Placar: {self.score[0]} - {self.score[1]}")
            self.reset_ball()
        else:
            self.ball_position = next_position

    def reset_ball(self):
        """Reinicia a posição da bola no centro e descreve."""
        print("A bola é reiniciada no centro!")
        self.ball_position = [self.boundary // 2, self.boundary // 2]
        self.ball_direction = [-1, 1]  # Reinicia a direção

    def render(self):
        """Exibe o estado atual do jogo e descreve."""
        print(f"Placar: {self.score[0]} - {self.score[1]}")
        print("-" * self.boundary)

        for i in range(self.boundary):
            row = [' '] * self.boundary

            # Descreve paddles
            if i in self.paddle_left.get_positions():
                row[0] = '|'
            if i in self.paddle_right.get_positions():
                row[-1] = '|'

            # Descreve a bola
            if i == self.ball_position[0]:
                row[self.ball_position[1]] = 'O'

            print(''.join(row))

        print("-" * self.boundary)

    def is_game_over(self):
        """Verifica se o jogo terminou (exemplo: limite de pontos)."""
        return max(self.score) >= 5
