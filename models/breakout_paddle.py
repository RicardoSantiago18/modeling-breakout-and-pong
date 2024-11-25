class Paddle:
    def __init__(self, posicao_x, posicao_y, largura):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.largura = largura

    def move_paddle(self):
        print(f"Raquete se move para posição ({self.posicao_x}, {self.posicao_y})")