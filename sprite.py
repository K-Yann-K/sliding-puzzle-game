import pygame
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tilesize, tilesize))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect()
        self.update_image()

    def update_image(self):
        if self.text != "empty":
            tile_x = (self.text - 1) % game_size
            tile_y = (self.text - 1) // game_size
            tile_rect = pygame.Rect(tile_x * tilesize, tile_y * tilesize, tilesize, tilesize)
            self.image.blit(self.game.image, (0, 0), tile_rect)
        else:
            self.image.fill(bgcolour)

    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize

    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    def right(self):
        return self.rect.x + tilesize < game_size * tilesize

    def left(self):
        return self.rect.x - tilesize >= 0

    def up(self):
        return self.rect.y - tilesize >= 0

    def down(self):
        return self.rect.y + tilesize < game_size * tilesize
