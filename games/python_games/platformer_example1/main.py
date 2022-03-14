from asyncio.format_helpers import _format_args_and_kwargs
import pygame
from pygame import *
from pygame import K_RETURN, K_UP, K_DOWN

def Move_char(pressed_key,char):
    if pressed_key == K_w:
        char.pos += 10
        


def Level_1():
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


def Game_start():
    running = True
    while running:
        screen.fill((255, 255, 255))
        main_menu = pygame.image.load("media/backgrounds/main_menu.jpg")
        screen.blit(main_menu, (0,0))

        level_1_button = pygame.draw.rect(screen, (255, 255, 255), (50, 50, 100, 50), 3)
        level_2_button = pygame.draw.rect(screen, (255, 255, 255), (200, 50, 100, 50), 3)
        level_3_button = pygame.draw.rect(screen, (255, 255, 255), (350, 50, 100, 50), 3)
        level_4_button = pygame.draw.rect(screen, (255, 255, 255), (50, 150, 100, 50), 3)
        level_5_button = pygame.draw.rect(screen, (255, 255, 255), (200, 150, 100, 50), 3)
        level_6_button = pygame.draw.rect(screen, (255, 255, 255), (350, 150, 100, 50), 3)
        level_7_button = pygame.draw.rect(screen, (255, 255, 255), (50, 250, 100, 50), 3)
        level_8_button = pygame.draw.rect(screen, (255, 255, 255), (200, 250, 100, 50), 3)
        level_9_button = pygame.draw.rect(screen, (255, 255, 255), (350, 250, 100, 50), 3)

        go_back = pygame.draw.rect(screen, (255, 255, 255), (300, 400, 150, 50), 3)

        font = pygame.font.SysFont(None, 30)
        text = font.render('Level 1', True, (255, 255, 255))
        screen.blit(text, (60, 65))
        text = font.render('Level 2', True, (255, 255, 255))
        screen.blit(text, (210, 65))
        text = font.render('Level 3', True, (255, 255, 255))
        screen.blit(text, (360, 65))
        text = font.render('Level 4', True, (255, 255, 255))
        screen.blit(text, (60, 165))
        text = font.render('Level 5', True, (255, 255, 255))
        screen.blit(text, (210, 165))
        text = font.render('Level 6', True, (255, 255, 255))
        screen.blit(text, (360, 165))
        text = font.render('Level 7', True, (255, 255, 255))
        screen.blit(text, (60, 265))
        text = font.render('Level 8', True, (255, 255, 255))
        screen.blit(text, (210, 265))
        text = font.render('Level 9', True, (255, 255, 255))
        screen.blit(text, (360, 265))
        text = font.render('Go back!', True, (255, 255, 255))
        screen.blit(text, (320, 415))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if level_1_button.collidepoint(pos):
                    Level_1()
                if level_2_button.collidepoint(pos):
                    Level_2()
                if level_3_button.collidepoint(pos):
                    Level_3()
                if level_4_button.collidepoint(pos):
                    Level_4()
                if level_5_button.collidepoint(pos):
                    Level_5()
                if level_6_button.collidepoint(pos):
                    Level_6()
                if level_7_button.collidepoint(pos):
                    Level_7()
                if level_8_button.collidepoint(pos):
                    Level_8()
                if level_9_button.collidepoint(pos):
                    Level_9()

                if go_back.collidepoint(pos):
                    running = False
                    return 0

        pygame.display.update()

def Game_quit():
    pygame.quit()

def Game_options():
    running = True
    while running:
        screen.fill((255, 255, 255))
        main_menu = pygame.image.load("media/backgrounds/main_menu.jpg")
        screen.blit(main_menu, (0,0))
        
        text_bubble = pygame.image.load("media/assets/text_bubble.png").convert_alpha()
        text_bubble = pygame.transform.rotozoom(text_bubble, 0, 0.5)
        screen.blit(text_bubble, (0,0))
        pygame.display.flip()

        font = pygame.font.SysFont(None, 30)
        text = font.render('NO Options for you! Go back!', True, (255, 255, 255))
        screen.blit(text, (10, 50))
        text = font.render('Go back!', True, (255, 255, 255))
        screen.blit(text, (320, 415))

        go_back = pygame.draw.rect(screen, (255, 255, 255), (300, 400, 150, 50), 3)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if go_back.collidepoint(pos):
                        running = False
                        return 0

        

def main_menu():

    running = True
    while running:
        screen.fill((255, 255, 255))

        main_menu = pygame.image.load("media/backgrounds/main_menu.jpg")
        screen.blit(main_menu, (0,0))

        start_game_button = pygame.draw.rect(screen, (255, 255, 255), (150, 250, 200, 50), 3)
        options_button = pygame.draw.rect(screen, (255, 255, 255), (150, 320, 200, 50), 3)
        quit_button = pygame.draw.rect(screen, (255, 255, 255), (150, 390, 200, 50), 3)
        
        font = pygame.font.SysFont(None, 24)
        text = font.render('Get out of my swamp!', True, (255, 255, 255))
        screen.blit(text, (20, 40))
        text = font.render('Start game', True, (255, 255, 255))
        screen.blit(text, (210, 270))
        text = font.render('Options', True, (255, 255, 255))
        screen.blit(text, (220, 340))
        text = font.render('Quit', True, (255, 255, 255))
        screen.blit(text, (230, 410))

        text_bubble = pygame.image.load("media/assets/text_bubble.png").convert_alpha()
        text_bubble = pygame.transform.rotozoom(text_bubble, 0, 0.33)
        screen.blit(text_bubble, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_game_button.collidepoint(pos):
                    Game_start()

                if options_button.collidepoint(pos):
                    Game_options()
                    
                if quit_button.collidepoint(pos):
                    Game_quit()
                    
        pygame.display.update()



pygame.init()
screen = pygame.display.set_mode([500, 500])

main_menu() 

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()



