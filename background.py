import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self, image_file, location):
        super(Background, self).__init__()
        self.image = pygame.image.load('images/space.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        