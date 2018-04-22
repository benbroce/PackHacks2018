import pygame
from pygame.locals import *
from pygame import mixer
import sys
import song
from time import sleep

screen_width = 420
screen_height = 800
score = 0
score_inc = 100

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
musicStarted = False

#pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
mixer.music.load('twinkle_star_instrumental.ogg')
mixer.music.set_volume(1)

thisSong = song.Song(screen, sys.argv[1], 5)
pygame.time.set_timer(USEREVENT+1, thisSong.tempo)

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == USEREVENT+1:
            if thisSong.next() == 0:
                done = True
        if event.type == pygame.QUIT:
            done = True

    if (pygame.time.get_ticks() > 1700 and not musicStarted):
        musicStarted = True
        mixer.music.play(0)

    pressed = pygame.key.get_pressed()
    if thisSong.isCollided(screen_height - 60, screen_height - 20):
        if pressed[pygame.K_d]:
            if thisSong.hit(0):
                score += score_inc
        if pressed[pygame.K_f]:
            if thisSong.hit(1):
                score += score_inc
        if pressed[pygame.K_SPACE]:
            if thisSong.hit(2):
                score += score_inc
        if pressed[pygame.K_j]:
            if thisSong.hit(3):
                score += score_inc
        if pressed[pygame.K_k]:
            if thisSong.hit(4):
                score += score_inc

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(0, screen_height - 60, screen_width, 40))
    thisSong.draw()

    pygame.display.flip()
    clock.tick(60)
print("Score: " + score)
