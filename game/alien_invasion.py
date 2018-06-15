
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():    # Inicializa o jogo, cria um objeto tela, e as configuracoes
    pygame.init()
    minha_configuracao = Settings()
    screen = pygame.display.set_mode((minha_configuracao.screen_width, minha_configuracao.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen) #constroi uma instancia de nave



    # Iniciando o loop principal do jogo

    while True:  # Aguardando eventos do mouse/teclado

        gf.check_events(ship)
        ship.update()
        gf.update_screen(minha_configuracao, screen, ship)


run_game()
