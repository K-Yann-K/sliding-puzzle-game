import pygame
from setting import *

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image=None, crop_rect=None):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((titlesize, titlesize))
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        if image and crop_rect:
            self.image = image.subsurface(crop_rect).copy()
        else:
            self.image.fill(black)
        
    def update(self):
        self.rect.x = self.x * titlesize
        self.rect.y = self.y * titlesize
        
    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom