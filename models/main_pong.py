from pong_game import Game
import time


def main():
    game = Game()
    print("Jogo iniciado!")
    print("Controles: (simulação sem interatividade, apenas descrição de movimentos)\n")

    # Simula algumas jogadas
    moves = ['left_up', 'right_down', 'left_down', 'right_up', 'left_up', 'right_down']

    while not game.is_game_over():
        game.render()
        for move in moves:
            if move == 'left_up':
                game.paddle_left.move_up()
                print("Jogador esquerdo moveu o paddle para cima.")
            elif move == 'left_down':
                game.paddle_left.move_down()
                print("Jogador esquerdo moveu o paddle para baixo.")
            elif move == 'right_up':
                game.paddle_right.move_up()
                print("Jogador direito moveu o paddle para cima.")
            elif move == 'right_down':
                game.paddle_right.move_down()
                print("Jogador direito moveu o paddle para baixo.")

            game.move_ball()  # Move a bola e descreve
            time.sleep(1)  # Simula o tempo de espera entre os movimentos

    print(f"Fim de jogo! Placar final: {game.score[0]} - {game.score[1]}")


if __name__ == "__main__":
    main()
