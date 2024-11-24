from game import Game

if _name_ == "_main_":
    game = Game()
    game.start()
    # Exemplo de loop de jogo simplificado
    for _ in range(10): game.update()