import pygame
import time
import random 
from sprite import *
from setting import *


class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        
        self.image = pygame.image.load("Image/source.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (game_size * titlesize, game_size * titlesize))

        
    def create_game(self):
        grid = []
        number = 1
        for x in range(game_size):
            grid.append([])
            for y in range(game_size):
                grid[x].append(number)
                number += 1
        grid[-1][-1] = 0
        return grid
        
    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile != 0:
                    # Calculer le rectangle de la portion d'image
                    crop_rect = pygame.Rect(
                        col * titlesize,
                        row * titlesize,
                        titlesize,
                        titlesize
                    )
                    self.tiles[row].append(Tile(self, col, row, self.image, crop_rect))
                else:
                    self.tiles[row].append(Tile(self, col, row))  # Tuile vide

                
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.create_game()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        self.all_sprites.update()
    
    def draw_grid(self):
        for row in range (-1, game_size * titlesize, titlesize):
            pygame.draw.line(self.screen, lightgrey, (row, 0), (row, game_size*titlesize))
        for col in range (-1, game_size * titlesize, titlesize):
            pygame.draw.line(self.screen, lightgrey, (0, col), (game_size*titlesize, col))
    
    def draw(self):
        self.screen.fill(bgcolour)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        self.draw_tiles()
        pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
    
game = Game()
while True:
    game.new()
    game.run()