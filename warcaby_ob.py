# Author: [Sebastian Kalla]
# Date: [13.01.2025]
# Course: Python I, Lab 3
# Assignment: [Gra - warcaby]
# Description: [Program]
# Version: [Wersja 1.0/nieukończona]
# Dificulty: [Trudne]
# The level of motivation to learn Python: [Wysokie]
# Expected mark: [4]
# Own ideas for modifying tasks, suggestions of your own: […]
# Other notes, own observations: [Nie ma]

import pygame
import sys

class Constants:
    BOARD_SIZE = 8
    SQUARE_SIZE = 100
    WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE
    FPS = 60
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (105, 105, 105)
    LINEN = (255, 240, 245)
    RED = (255, 0, 0)

class TextBox:
    def __init__(self, text, x, y, width, height, text_color, box_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.box_color = box_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, self.box_color,
                            (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(
            center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

