from breakout_game import Game

if __name__ == "__main__":
    game = Game()
    game.start()
    for _ in range(10):
        game.update()
