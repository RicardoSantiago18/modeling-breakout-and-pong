from breakout_game import Jogo
from breakout_paddle import Paddle
from ball import Ball
from brick_color import CampoDeJogo

# Configuração inicial
campo_de_jogo = CampoDeJogo()
raquete = Paddle(2, 3, 3)
bola = Ball(2, 2, 1)

# Inicia o jogo
jogo = Jogo(campo_de_jogo, raquete, bola)
jogo.iniciar_jogo()
