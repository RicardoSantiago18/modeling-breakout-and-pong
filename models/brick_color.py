from brick import Bricks

class CampoDeJogo:
    def __init__(self):
        self.tijolos = [
            Bricks(1, 1, "amarelo", 1), Bricks(2, 1, "amarelo", 1), Bricks(3, 1, "amarelo", 1), Bricks(4, 1, "amarelo", 1),
            Bricks(1, 2, "verde", 3), Bricks(2, 2, "verde", 3), Bricks(3, 2, "verde", 3), Bricks(4, 2, "verde", 3),
            Bricks(1, 3, "laranja", 5), Bricks(2, 3, "laranja", 5), Bricks(3, 3, "laranja", 5), Bricks(4, 3, "laranja", 5),
            Bricks(1, 4, "vermelho", 7), Bricks(2, 4, "vermelho", 7), Bricks(3, 4, "vermelho", 7), Bricks(4, 4, "vermelho", 7),
        ]

    def mostrar_tijolos(self):
        print("Tijolos no campo de jogo:\n")
        for tijolo in self.tijolos:
            if not tijolo.destruido:
                print(f"Tijolo na posição ({tijolo.posicao_x}, {tijolo.posicao_y}) de cor {tijolo.cor}\n")
