from pong_game import Game
import time

def main():
    game = Game()
    print("Jogo PONG iniciado!")
    print("Descrição de eventos no terminal:\n")

    # Simula o jogo até alguém atingir 5 pontos
    while not game.is_game_over():
        game.describe_game_state()
        game.move_ball()
        time.sleep(1)  # Pausa para simular tempo de jogo

    print(f"Fim de jogo! Placar final: Jogador Esquerdo {game.score[0]} - {game.score[1]} Jogador Direito")

if __name__ == "__main__":
    main()
