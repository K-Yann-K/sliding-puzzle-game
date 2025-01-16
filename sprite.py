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


class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text
        
    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 50)
        text = font.render(self.text, True, white)
        screen.blit(text, (self.x, self.y))
        
class Button:
    def __init__(self, x, y, width, height, text, colour, text_colour):
        self.colour, self.text_colour = colour, text_colour
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.text = text
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Consolas", 30)
        text = font.render(self.text, True, self.text_colour)
        self.font_size = font.size(self.text)
        draw_x = self.x + (self.width / 2) - self.font_size[0] / 2
        draw_y = self.y + (self.height / 2) - self.font_size[1] / 2
        screen.blit(text, (draw_x, draw_y))
        
    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
