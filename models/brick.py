class Bricks:
    def __init__(self, posicao_x, posicao_y, cor, pontuacao):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.cor = cor
        self.pontuacao = pontuacao
        self.destruido = False

    def destruir(self):
        self.destruido = True
        print(f"Tijolo na posição ({self.posicao_x}, {self.posicao_y}) de cor {self.cor} foi destruído!\n")
