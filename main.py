import pygame
import random
# initilize the pygame 
pygame.init()
#creating a display for the game 
screen = pygame.display.set_mode((800,600))
# Convert (and scale once) to avoid per-frame blit slowdown.
raw_bg = pygame.image.load("icons_and_characters/background.png").convert()
background = pygame.transform.scale(raw_bg, (800, 600))
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
enemy_pos_x_cha = 0.1
enemy_pos_y_cha = 0.008

#bullet
bullet_img = pygame.image.load("icons_and_characters/bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_cha = 0
bullet_y_cha = -0.5
bullet_state = "ready"
#defining player
def player(pos_x,pos_y):
    screen.blit(player_img,(pos_x, pos_y))
#defining enemy
def enemy(enemy_pos_x,enemy_pos_y):
    screen.blit(enemy_img, (enemy_pos_x, enemy_pos_y))
#defining bullet
def bullet_fire(x,y):
    global bullet_y
    global bullet_state
    bullet_state = "fired"
    screen.blit(bullet_img,(x+16, y+10))

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
            if e.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_x = pos_x
                    bullet_fire(bullet_x,bullet_y)
                
        if e.type == pygame.KEYUP:
            pos_x_cha = 0
            pos_y_cha = 0
    #color
    screen.blit(background,(0,0))
    #player calling
    pos_x += pos_x_cha
    if pos_x <= 0 :
        pos_x = 0
    elif pos_x >= 736:
        pos_x = 736
    #bullet_movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fired":
        bullet_fire(bullet_x,bullet_y)
        bullet_y -= 0.5
    #emeny movement
    enemy_pos_x += enemy_pos_x_cha
    if enemy_pos_x <= 0 :
        enemy_pos_x_cha = 0.1
    elif enemy_pos_x >= 736:
        enemy_pos_x_cha = -0.1
    enemy_pos_y += enemy_pos_y_cha
    player(pos_x, pos_y)
    enemy(enemy_pos_x,enemy_pos_y)
    pygame.display.update()