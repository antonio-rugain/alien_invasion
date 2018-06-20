import sys
import pygame
from bullet import Bullet

def check_events(minha_configuracao, screen, ship, bullets):
    """responde ao pressionar mouse e teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, minha_configuracao, screen, ship, bullets)
            check_keydown_events(event, minha_configuracao, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)




def update_screen(minha_configuracao, screen, ship, bullets):
    screen.fill(minha_configuracao.bg_color) #redesenha a tela, cada vez que passa pelo loop
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()    # fazendo o rabisco mais recente na tela




def check_keydown_events(event, minha_configuracao, screen, ship, bullets):

    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        fire_bullet(minha_configuracao, screen, ship, bullets)

def fire_bullet(minha_configuracao, screen, ship, bullets):
    """Atira a bala apenas se o limite nao tiver sido atingido"""
    if (len(bullets)-2) < minha_configuracao.bullets_allowed:
        new_bullet = Bullet(minha_configuracao, screen, ship)
        bullets.add(new_bullet)



def check_keyup_events(event, ship):
    """Responde ao soltar da tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    """Atualiza a posicao das balas e da fim as antigas"""
    # Update bullet positions.
    bullets.update()
    # Dar fim as balas que ja desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
