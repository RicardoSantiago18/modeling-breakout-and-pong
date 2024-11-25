class Ball:
    def __init__(self, position, direction, boundary):
        """
        Inicializa a bola.
        :param position: Posição inicial da bola [linha, coluna].
        :param direction: Direção inicial [vertical, horizontal].
        :param boundary: Limites do campo de jogo.
        """
        self.position = position
        self.direction = direction
        self.boundary = boundary

    def move(self):
        """Atualiza a posição da bola com base na direção."""
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]

    def reset(self):
        """Reinicia a posição da bola no centro do campo."""
        self.position = [self.boundary // 2, self.boundary // 2]
        self.direction = [-1, 1]

    def check_collision(self, paddle):
        """
        Verifica se a bola colidiu com o paddle.
        :param paddle: Instância de Paddle.
        :return: True se houve colisão, False caso contrário.
        """
        if self.position[1] == 1 and self.position[0] in paddle.get_positions():
            self.direction[1] *= -1
            return True
        elif self.position[1] == self.boundary - 2 and self.position[0] in paddle.get_positions():
            self.direction[1] *= -1
            return True
        return False

    def check_wall_collision(self):
        """Verifica colisão com as bordas verticais do campo."""
        if self.position[0] < 0 or self.position[0] >= self.boundary:
            self.direction[0] *= -1
