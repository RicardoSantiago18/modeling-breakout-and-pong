class Ball:
    def __init__(self, posicao_x, posicao_y, velocidade):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade

    def iniciar(self):
        print(f"Bola iniciada na posição ({self.posicao_x}, {self.posicao_y})\n")

    def rebater(self):
        print("Bola rebateu!\n")

    def colide_com_tijolo(self, tijolo):
        return True

    def colide_com_raquete(self, raquete):
        return True
