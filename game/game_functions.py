import sys
import pygame

def check_events(ship):
    """responde ao pressionar mouse e teclado"""
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            # Mover a nave para a direita
                ship.rect.centerx += 1
            if event.key == pygame.K_LEFT:
            # Mover a nave para a esquerda
                ship.rect.centerx -= 1


def update_screen(minha_configuracao, screen, ship):
    screen.fill(minha_configuracao.bg_color) #redesenha a tela, cada vez que passa pelo loop
    ship.blitme()
    pygame.display.flip()    # fazendo o rabisco mais recente na tela
