import pygame

class Action():
    "describe rock, paper, scissors"

    def __init__(self, screen, image_path, position, fight, rps_settings):
        #screen surface
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #image
        if fight & position == 1:
            self.image = pygame.transform.flip(pygame.image.load(image_path), True, False)
        elif  fight == 0:
            self.image = pygame.transform.flip(pygame.image.load(image_path), True, False)
        else:
            self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        #position of image
        self.position = position - 1
        if fight: #fight - play the round after choosing
            self.rect.centerx = (1/4 + 1/2*self.position)*rps_settings.screen_width
            self.rect.centery = 1/2 * rps_settings.screen_height
        else:
            self.rect.centerx = (1/6 + 1/3*self.position)*rps_settings.screen_width
            self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """draw on screen"""
        self.screen.blit(self.image, self.rect)
