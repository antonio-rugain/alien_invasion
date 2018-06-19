
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():    # Inicializa o jogo, cria um objeto tela, e as configuracoes
    pygame.init()
    minha_configuracao = Settings()
    screen = pygame.display.set_mode((minha_configuracao.screen_width, minha_configuracao.screen_height))
    pygame.display.set_caption("Alien Invasion do Rugas")

    ship = Ship(minha_configuracao, screen) #constroi uma instancia de nave
    # Cria um grupo para guardar balas
    bullets = Group()



    # Iniciando o loop principal do jogo

    while True:  # Aguardando eventos do mouse/teclado

        gf.check_events(minha_configuracao, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(minha_configuracao, screen, ship, bullets)


run_game()
