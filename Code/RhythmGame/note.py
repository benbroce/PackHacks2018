import pygame

red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Note:
    def __init__(self, screen, x, y, speed, size, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color

    def draw(self):
        self.y += self.speed
        pygame.draw.ellipse(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

    def getY(self):
        return self.y - (self.size / 2)
