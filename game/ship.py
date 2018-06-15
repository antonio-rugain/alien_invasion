import pygame
class Ship():
    def __init__(self, minha_configuracao, screen):
        """Inicializar a nave e settar sua posicao inicial"""
        self.screen = screen
        self.minha_configuracao = minha_configuracao

        # Carrega a imagem da nave e pega o seu retangulo(rect)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  #refere-se a navinha
        self.screen_rect = screen.get_rect() #refere-se a tela


        # Inicia cada nave nova no centro , e no fim da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom



        # Guarda um valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        self.moving_right = False #flag de movimento
        self.moving_left = False



    def blitme(self):
        """Desenha a nave na sua posicao atual"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Atualiza a posicao da nave baseado na flag de movimento"""
        #Atualiza o centro da nave, nao do retangulo
        if self.moving_right and self.rect.right < self.screen_rect.right: #muda a posicao da nave se ela nao ultra
        #passa o tamanho da tela

            self.center += self.minha_configuracao.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.minha_configuracao.ship_speed_factor

        # Atualiza o retangulo pelo self.center
        self.rect.centerx = self.center
