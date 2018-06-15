import pygame
class Ship():
    def __init__(self, screen):
        """Inicializar a nave e settar sua posicao inicial"""
        self.screen = screen

        # Carrega a imagem da nave e pega o seu retangulo(rect)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  #refere-se a navinha
        self.screen_rect = screen.get_rect()
        # Inicia cada nave nova no centro , e no fim da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False #flag de movimento
        self.moving_left = False



    def blitme(self):
        """Desenha a nave na sua posicao atual"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Atualiza a posicao da nave baseado no movimento da flag"""
        if self.moving_right:
            self.rect.centerx += 3

        if self.moving_left:
            self.rect.centerx -= 3
