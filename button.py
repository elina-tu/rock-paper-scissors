import pygame

class Button():

    def __init__(self, rps_settings, screen, msg):
        "Initialize button attributes."
        self.screen  = screen
        self.screen_rect = screen.get_rect()

        #dimentions and properties of the button
        self.width, self.height = 170, 50
        self.button_color = (255, 255, 255)
        self.text_color = (49, 47, 48)
        self.font = pygame.font.Font('Prototype.ttf', 25)

        #build the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 9/10*rps_settings.screen_height

        #text
        self.text_button = self.font.render(msg, True, self.text_color)
        self.text_buttonRect = self.text_button.get_rect()
        self.text_buttonRect.centerx = self.screen_rect.centerx
        self.text_buttonRect.centery = 9/10*rps_settings.screen_height

    def blitme(self):
        #draw button
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_button, self.text_buttonRect)
