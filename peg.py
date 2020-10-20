import pygame
import game_objects


class Peg:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw_peg(self):
        pygame.draw.rect(game_objects.screen, self.color, (self.x, self.y, self.width, self.height))
