class Paddle:
    def __init__(self, position, size=3, boundary=10):
        """
        Inicializa um paddle.
        :param position: Posição inicial do paddle (índice vertical).
        :param size: Tamanho do paddle.
        :param boundary: Limite máximo do campo.
        """
        self.position = position
        self.size = size
        self.boundary = boundary

    def move_up(self):
        """Move o paddle para cima, respeitando o limite."""
        if self.position > 0:
            self.position -= 1

    def move_down(self):
        """Move o paddle para baixo, respeitando o limite."""
        if self.position < self.boundary - self.size:
            self.position += 1

    def get_positions(self):
        """Retorna as posições ocupadas pelo paddle."""
        return list(range(self.position, self.position + self.size))
