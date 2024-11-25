from breakout_game import Game
from breakout_paddle import Paddle
from ball import Ball
from brick_color import CampoDeJogo


campo_de_jogo = CampoDeJogo()
raquete = Paddle(2, 3, 3)
bola = Ball(2, 2, 1)


jogo = Game(campo_de_jogo, raquete, bola)
jogo.iniciar_jogo()
