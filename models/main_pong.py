from pong_game import Game

if __name__ == "_main_":
    game = Game()
    game.start()
    for _ in range(10): game.update()