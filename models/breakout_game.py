import time

class Jogo:
    def __init__(self, campo_de_jogo, raquete, bola):
        self.campo_de_jogo = campo_de_jogo
        self.raquete = raquete
        self.bola = bola
        self.pontuacao = 0

    def iniciar_jogo(self):
        print("Jogo iniciado!\n")
        self.campo_de_jogo.mostrar_tijolos()
        self.bola.iniciar()
        self.raquete.move_paddle()
        self.simular_jogo()

    def simular_jogo(self):
        while True:
            print(f"\nPosição da bola: ({self.bola.posicao_x}, {self.bola.posicao_y})")
            print(f"Posição da raquete: ({self.raquete.posicao_x}, {self.raquete.posicao_y})\n")


            for tijolo in self.campo_de_jogo.tijolos:
                if self.bola.colide_com_tijolo(tijolo):
                    print(f"Bola acerta tijolo de cor {tijolo.cor}!")
                    self.pontuacao += tijolo.pontuacao
                    tijolo.destruir()
                    self.bola.rebater()
                    print(f"Tijolo destruído! Pontuação: {self.pontuacao}\n")


            if self.bola.colide_com_raquete(self.raquete):
                print("Bola rebate na raquete!\n")
                self.bola.rebater()


            time.sleep(2)
