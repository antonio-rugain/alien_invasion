import sys
import pygame

def check_events():
"""responde ao pressionar mouse e teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(minha_configuracao, screen, ship):
    screen.fill(minha_configuracao.bg_color) #redesenha a tela, cada vez que passa pelo loop
    ship.blitme()
    pygame.display.flip()    # fazendo o rabisco mais recente na tela
