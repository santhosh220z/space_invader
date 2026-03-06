import pygame
import random
# initilize the pygame 
pygame.init()
#creating a display for the game 
screen = pygame.display.set_mode((800,600))
#setting icon and displayname for the game
pygame.display.set_caption("Space_Invaders!")
icon = pygame.image.load("icons_and_characters/spaceship.png")
pygame.display.set_icon(icon)
#player_image
player_img = pygame.image.load("icons_and_characters/Adobe Express - file.png")
#default player position
pos_x = 370
pos_y = 480
pos_x_cha = 0
pos_y_cha = 0
#enemy attribute
enemy_img = pygame.image.load("icons_and_characters/alien.png")

enemy_pos_x = random.randint(0,736)
enemy_pos_y = random.randint(50,150)
enemy_pos_x_cha = 0
enemy_pos_y_cha = 0
#defining player
def player(pos_x,pos_y):
    screen.blit(player_img,(pos_x, pos_y))
#defining enemy
def enemy(enemy_pos_x,enemy_pos_y):
    screen.blit(enemy_img, (enemy_pos_x, enemy_pos_y))
#game loop (for the screen to not close after running completed)
running = True
while running:
    # the game main code will bw written in here otherwise the game would break
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                pos_x_cha = -0.3
            if e.key == pygame.K_RIGHT:
                pos_x_cha = 0.3
        if e.type == pygame.KEYUP:
            pos_x_cha = 0
            pos_y_cha = 0
    #color
    red = 0
    green = 0
    blue = 30
    screen.fill((red,green,blue))
    #player calling
    pos_x += pos_x_cha
    if pos_x <= 0 :
        pos_x = 0
    elif pos_x >= 736:
        pos_x = 736
    player(pos_x, pos_y)
    enemy(enemy_pos_x,enemy_pos_y)
    pygame.display.update()