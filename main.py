import pygame   
import math
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time 
    score_surf = test_font.render(f'{current_time}',False,(64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
game_active = True
start_time = 0

#Load font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#load sky and ground texture
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#Create text surface and rectangle from surface
text_surface = test_font.render('My game', False, 'Black')
text_rect = text_surface.get_rect(midtop = (400,50))

#Create snail surface and create rect
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))


player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
jump_force = 21

def sys_fps():
    fps = str(int(clock.get_fps()))
    print(fps)

while True:
    #sys_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
            #if player_rect.collidepoint(event.pos): 
                player_gravity = -jump_force

            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -jump_force
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)


    #main game loop
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen, 'Pink', text_rect)
        #screen.blit(text_surface,text_rect)
        display_score()

        snail_rect.x -= 4
        screen.blit(snail_surface,snail_rect)
        if snail_rect.right < 0: snail_rect.x  = 805

        #draw the player
        player_gravity += 1
        player_rect.y += player_gravity 
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #snail collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("yellow")

    pygame.display.update()
    clock.tick(60)
