import sys
import pygame
from settings import Settings


def run_game():    # Inicializa o jogo, cria um objeto tela, e as configuracoes
    pygame.init()
    minha_configuracao = Settings()
    screen = pygame.display.set_mode((minha_configuracao.screen_width, minha_configuracao.screen_height))
    pygame.display.set_caption("Alien Invasion")



# Iniciando o loop principal do jogo

    while True:  # Aguardando eventos do mouse/teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(minha_configuracao.bg_color) #redesenha a tela, cada vez que passa pelo loop



        pygame.display.flip()    # fazendo o rabisco mais recente na tela

run_game()
