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
                ship.moving_right = True
                ship.rect.centerx += 2

            elif event.key == pygame.K_LEFT:
                # Mover a nave para a esquerda
                ship.rect.centerx -= 2
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False





def update_screen(minha_configuracao, screen, ship):
    screen.fill(minha_configuracao.bg_color) #redesenha a tela, cada vez que passa pelo loop
    ship.blitme()
    pygame.display.flip()    # fazendo o rabisco mais recente na tela
