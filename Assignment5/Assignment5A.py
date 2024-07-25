#treasure puzzle
import pygame, sys
from pygame.locals import *
# Initialie
pygame.init()
#set resolution and screen
resolution = (800, 600)
screen = pygame.display.set_mode(resolution)
# define colors
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
# define player
player = pygame.Rect(0, 0, 50,50)
playersurf = pygame.Surface((player.width, player.height))
playersurf.fill(blue)
# Define treasure
treasure = pygame.Rect(750, 550, 50, 50)
treasure_surf = pygame.Surface((treasure.width, treasure.height))
treasure_surf.fill(green)
#define endgoal
endgoal = pygame.Rect(0, 0, 50,50)

#obsticles
vert_wall = pygame.Rect(195, 200, 5, 100)
vert_wall2 = pygame.Rect(200, 500, 350, 5)
vert_wall3 = pygame.Rect(500, 100, 5, 100)
vert_wall1 = pygame.Rect(300, 100, 5, 100)
long_wall1 = pygame.Rect(200, 200, 300, 5)
long_wall2 = pygame.Rect(300, 300, 300, 5)
longwall3 = pygame.Rect(600, 250, 5, 200)
longwall4 = pygame.Rect(600, 100, 200, 5)
block1 = pygame.Rect(100, 0, 100, 200)
block2 = pygame.Rect(100, 500, 200, 100)
block3 = pygame.Rect(0, 300, 100, 100)
block4 = pygame.Rect(200, 400, 100, 100)
#surfaces
block_surf = pygame.Surface((100, 100))
block_surf1 = pygame.Surface((block1.width, block1.height))
block_surf1.fill(white)
block_surf2 = pygame.Surface((block2.width, block2.height))
block_surf2.fill(white)
block_surf.fill(white)
vert_surf = pygame.Surface((vert_wall.width, vert_wall.height))
vert_surf1 = pygame.Surface((vert_wall1.width, vert_wall1.height))
vert_surf1.fill(white)
vert_surf2 = pygame.Surface((vert_wall2.width, vert_wall2.height))
vert_surf2.fill(white)
vert_surf3 = pygame.Surface((vert_wall3.width, vert_wall3.height))
vert_surf3.fill(white)
wall_surf = pygame.Surface((long_wall1.width, long_wall1.height))
wall_surf2 = pygame.Surface((long_wall2.width, long_wall2.height))
wall_surf2.fill(white)
wall_surf3 = pygame.Surface((longwall3.width, longwall3.height))
wall_surf3.fill(white)
wall_surf4 = pygame.Surface((longwall4.width, longwall4.height))
wall_surf4.fill(white)
wall_surf.fill(white)
vert_surf.fill(white)
#list of walls


def maze1():
    screen.blit(block_surf1, (block1.x, block1.y))
    screen.blit(block_surf2, (block2.x, block2.y))
    screen.blit(block_surf, (block3.x, block3.y))
    screen.blit(block_surf, (block4.x, block4.y))
    screen.blit(vert_surf, (vert_wall.x, vert_wall.y))
    screen.blit(vert_surf2, (vert_wall2.x, vert_wall2.y))
    screen.blit(wall_surf, (long_wall1.x, long_wall1.y))
    screen.blit(vert_surf1, ( vert_wall1.x, vert_wall1.y))
    screen.blit(wall_surf2, (long_wall2.x, long_wall2.y))
    screen.blit(wall_surf3, (longwall3.x, longwall3.y))
    screen.blit(vert_surf3, (vert_wall3.x, vert_wall3.y))
    screen.blit(wall_surf4, (longwall4.x, longwall4.y))

def maze2():
    #locally defining player
    player = pygame.Rect(originx, originy, 50,50)
    playersurf = pygame.Surface((player.width, player.height))
    playersurf.fill(blue)
    counter = 1800
    seconds = 30
    while endgoal.colliderect(player) != True:
        keys = pygame.key.get_pressed()
        screen.fill(black)
        screen.blit(playersurf, (player.x, player.y))
    
    #obsticles
        vert_wall = pygame.Rect(600, 200, 5, 300)
        vert_wall1 = pygame.Rect(500, 200, 5, 100)
        vert_wall2 = pygame.Rect(0, 300, 350, 5)
        vert_wall3 = pygame.Rect(250, 100, 5, 100)
        long_wall1 = pygame.Rect(200, 200, 300, 5)
        long_wall2 = pygame.Rect(400, 200, 300, 5)
        longwall3 = pygame.Rect(400, 400, 200, 5)
        block1 = pygame.Rect(450, 50, 100, 150)
        block2 = pygame.Rect(100, 500, 200, 100)
        block3 = pygame.Rect(0, 300, 100, 100)
        block4 = pygame.Rect(200, 400, 100, 100)
    #surfaces
        block_surf = pygame.Surface((100, 100))
        block_surf1 = pygame.Surface((block1.width, block1.height))
        block_surf1.fill(white)
        block_surf2 = pygame.Surface((block2.width, block2.height))
        block_surf2.fill(white)
        block_surf.fill(white)
        vert_surf = pygame.Surface((vert_wall.width, vert_wall.height))
        vert_surf1 = pygame.Surface((vert_wall1.width, vert_wall1.height))
        vert_surf1.fill(white)
        wall_surf = pygame.Surface((long_wall1.width, long_wall1.height))
        wall_surf2 = pygame.Surface((long_wall2.width, long_wall2.height))
        wall_surf2.fill(white)
        wall_surf3 = pygame.Surface((longwall3.width, longwall3.height))
        wall_surf3.fill(white)
        vert_surf2 = pygame.Surface((vert_wall2.width, vert_wall2.height))
        vert_surf2.fill(white)
        vert_surf3 = pygame.Surface((vert_wall3.width, vert_wall3.height))
        vert_surf3.fill(white)
        wall_surf.fill(white)
        vert_surf.fill(white)
#list of walls
        screen.blit(block_surf1, (block1.x, block1.y))
        screen.blit(block_surf2, (block2.x, block2.y))
        screen.blit(block_surf, (block3.x, block3.y))
        screen.blit(block_surf, (block4.x, block4.y))
        screen.blit(vert_surf, (vert_wall.x, vert_wall.y))
        screen.blit(vert_surf2, (vert_wall2.x, vert_wall2.y))
        screen.blit(wall_surf, (long_wall1.x, long_wall1.y))
        screen.blit(vert_surf1, ( vert_wall1.x, vert_wall1.y))
        screen.blit(wall_surf2, (long_wall2.x, long_wall2.y))
        screen.blit(wall_surf3, (longwall3.x, longwall3.y))
        screen.blit(vert_surf3, (vert_wall3.x, vert_wall3.y))
        Quitcheck()
        keys = pygame.key.get_pressed()
        list1 = [vert_wall, block1, block2, block3, block4, long_wall1, vert_wall1, long_wall2, vert_wall2, longwall3, vert_wall3]
        if player.collidelist(list1) != -1:
            player.x = originx
            player.y = originy
            screen.blit(playersurf, (originx, originy))
        else:
            if keys[pygame.K_w] and (player.y >=0):
                player = player.move(0, -5)
            if keys[pygame.K_s] and (player.y <=550):
                player = player.move(0, 5)
            if keys[pygame.K_a] and (player.x >= 0):
                player = player.move(-5, 0)
            if keys[pygame.K_d] and (player.x <= 750):
                player = player.move(5, 0)
            if keys[pygame.K_r]:
                player.x = originx
                player.y = originy
                screen.blit(playersurf, (originx, originy))
        #timer funtion
        
        if counter % 60 == 0:
            seconds -= 1
        if seconds == 0:
            sys.exit()
        counter -= 1
        text = str(seconds)
        pygame.display.set_caption(text)
        clock.tick(60)
        Quitcheck()
        pygame.display.flip()


def Quitcheck():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit(0) 
        if keys[pygame.K_ESCAPE]: 
            sys.exit(0)

screen.fill(black)
clock = pygame.time.Clock()
originx = 0
originy = 0
running = True
while running:
    #collision, movement, and restart
    keys = pygame.key.get_pressed()
    Quitcheck()
    list1 = [vert_wall, block1, block2, block3, block4, long_wall1, vert_wall1, long_wall2, vert_wall2, longwall3, vert_wall3, longwall4]
    if player.collidelist(list1) != -1:
        player.x = originx
        player.y = originy
        screen.blit(playersurf, (0, 0))
    else:
        if keys[pygame.K_w] and (player.y >=0):
            player = player.move(0, -5)
        if keys[pygame.K_s] and (player.y <=550):
            player = player.move(0, 5)
        if keys[pygame.K_a] and (player.x >= 0):
            player = player.move(-5, 0)
        if keys[pygame.K_d] and (player.x <= 750):
            player = player.move(5, 0)
        if keys[pygame.K_r]:
            player.x = originx
            player.y = originy
            screen.blit(playersurf, (0, 0))
        


        
    #display the maze
    screen.fill(black)
    screen.blit(playersurf, (player.x, player.y))
    if treasure.colliderect(player) == True:
        notif_sound = pygame.mixer.Sound('notification.mp3')
        pygame.mixer.Sound.play(notif_sound)
        originx = 740
        originy = 540
        keys = pygame.key.get_pressed()
        screen.fill(black)
        screen.blit(playersurf, (player.x, player.y))
        maze2()
        running = False
        pygame.display.flip()
        clock.tick(60)
        sys.exit()
    else:
        screen.blit(treasure_surf, (treasure.x, treasure.y))
        maze1()
    pygame.display.flip()
    clock.tick(60)