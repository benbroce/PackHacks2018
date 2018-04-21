import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
done = False

class Note:
    def __init__(self, x, y, speed, size, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color

    def draw(self):
        self.y += self.speed
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

note = Note(30, 0, 5, 60, (255, 255, 255))
note2 = Note(100, 0, 5, 60, (255, 0, 255))

clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill((0, 0, 0))
        note.draw()
        note2.draw()

        pygame.display.flip()
        clock.tick(30)
