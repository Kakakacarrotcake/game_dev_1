from asyncio.format_helpers import _format_args_and_kwargs
import pygame
from pygame import *
from pygame import K_RETURN, K_UP, K_DOWN
from levels import Level_1

def Move_char(pressed_key,char):
    if pressed_key == K_w:
        char.pos += 10


def Game_start(screen):
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
                    Level_1(screen)
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

        

def main_menu(screen,res_x,res_y):

    running = True
    while running:
        screen.fill((255, 255, 255))

        main_menu = pygame.image.load("media/backgrounds/main_menu.jpg")
        main_menu = pygame.transform.rotozoom(main_menu, 0, res_x/1600)
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
                    Game_start(screen)

                if options_button.collidepoint(pos):
                    Game_options(screen)
                    
                if quit_button.collidepoint(pos):
                    Game_quit(screen)
                    
        pygame.display.update()

def set_game_resolution():
    
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    
    height_input_active = False
    width_input_active = False
    resolution_values = ''
    resolution_width = 0
    resolution_height = 0

    running = True
    while running:

        screen.fill((255, 255, 255))
        if width_input_active == False: 
            res_width_input_rect = pygame.draw.rect(screen, (139, 0, 0), (150, 250, 200, 50), 3)
        if height_input_active == False:    
            res_height_input_rect = pygame.draw.rect(screen, (139, 0, 0), (150, 380, 200, 50), 3)

        done_rect = pygame.draw.rect(screen, (139, 0, 0), (350, 450, 100, 40), 3)
        
        font = pygame.font.SysFont(None, 30)
        text = font.render('Done', True, (128, 0, 0))
        screen.blit(text, (375, 460))
        text = font.render('Enter 16:9 resolution:', True, (128, 0, 0))
        screen.blit(text, (145, 170))
        text = font.render('Enter width:', True, (128, 0, 0))
        screen.blit(text, (190, 220))
        text = font.render('Enter height:', True, (128, 0, 0))
        screen.blit(text, (190, 345))
        font = pygame.font.SysFont(None, 27)
        if resolution_width != 0:
            text = font.render(str(resolution_width), True, (128, 0, 0))
            screen.blit(text, (370, 270))
        if resolution_height != 0:
            text = font.render(str(resolution_height), True, (128, 0, 0))
            screen.blit(text, (370, 400))


        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if res_width_input_rect.collidepoint(pos):
                    width_input_active = True
                    height_input_active = False
                elif res_height_input_rect.collidepoint(pos):
                    width_input_active = False
                    height_input_active = True
                elif done_rect.collidepoint(pos):
                    running = False
                else:
                    width_input_active = False
                    height_input_active = False 
            
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if height_input_active == True:
                        resolution_height = int(resolution_values)
                        resolution_values = ''
                        height_input_active = False
                    else:
                        resolution_width = int(resolution_values)
                        resolution_values = ''
                        width_input_active = True
                elif event.key == K_BACKSPACE:
                    resolution_values = resolution_values[:-1]
                else: 
                    resolution_values += event.unicode

        if width_input_active == True:
            res_width_input_rect = pygame.draw.rect(screen, (0, 210, 0), (150, 250, 200, 50), 3)
            text = font.render(resolution_values, True, (128, 0, 0))
            screen.blit(text, (160, 270))
        if height_input_active == True:
            res_height_input_rect = pygame.draw.rect(screen, (0, 210, 0), (150, 380, 200, 50), 3)
            text = font.render(resolution_values, True, (128, 0, 0))
            screen.blit(text, (160, 400))
        
        pygame.display.update()

    screen = pygame.display.set_mode([resolution_width, resolution_height])
    main_menu(screen,resolution_width, resolution_height)

set_game_resolution()

pygame.quit()



