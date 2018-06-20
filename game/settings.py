class Settings():   #classe que guarda as configuraçoes do jogo

    def __init__(self):
        self.screen_width = 1300
        self.screen_height =700
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # Configs da bala
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
