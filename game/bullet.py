import pygame
from pygame.sprite import Sprite
import pdb


class Bullet(Sprite):
    """Classe que manipula as balas atiradas pela nave"""
    def __init__(self, minha_configuracao, screen, ship):
        """Cria um objeto bala na posicao atual da nave"""
        super(Bullet, self).__init__()
        self.screen = screen
        #Cria um retangulo da bala em (0,0) e entao setta a posicao correta
        self.rect = pygame.Rect(0, 0, minha_configuracao.bullet_width, minha_configuracao.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


        # Guarda a posicao da bala com valor decimal
        self.y = float(self.rect.y)
        self.color = minha_configuracao.bullet_color
        self.speed_factor = minha_configuracao.bullet_speed_factor


    def update(self):
        """Move a bala para cima na tela"""
        # Atualiza a posicao decimal da bala
        self.y -= self.speed_factor
        # Atualiza a posicao do retangulo
        self.rect.y = self.y


    def draw_bullet(self):
        """Desenha a bala na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
