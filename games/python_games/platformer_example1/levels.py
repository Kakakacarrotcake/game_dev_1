import pygame
from pygame import *
from pygame import K_RETURN, K_UP, K_DOWN

def Level_1(screen):
    running = True
    while running:
        screen.fill((255, 255, 255))
        main_char = pygame.image.load("media/characters/main_char_sranding.png")
        screen.blit(main_char, (250,450))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_w or K_a or K_d or K_s:
                    Move_char(event.key)