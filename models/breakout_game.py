import time

class Game:
    def __init__(self, campo_de_jogo, raquete, bola):
        self.campo_de_jogo = campo_de_jogo
        self.raquete = raquete
        self.bola = bola
        self.pontuacao = 0
        self.vidas = 3

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
                    time.sleep(2)


            if self.bola.colide_com_raquete(self.raquete):
                print("Bola rebateu na raquete!\n")
                self.bola.rebater()
                time.sleep(2)


            if self.bola.perdeu_jogo():
                self.vidas -= 1
                print(f"A bola passou pela raquete! Vidas restantes: {self.vidas}\n")
                if self.vidas == 0:
                    print("Você perdeu o jogo! Fim de jogo.\n")
                    break
                else:
                    self.bola.resetar()
                    time.sleep(2)

            if all(tijolo.destruido for tijolo in self.campo_de_jogo.tijolos):
                print("Todos os tijolos foram destruídos! Você ganhou o jogo!\n")
                break

            time.sleep(2)
