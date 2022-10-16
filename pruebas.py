import pygame
from pygame import *
import sys
screen_width = 1000
screen_height = 800
FPS = 30
#--------------------COLORS-------------

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

def Quit_Me():
    print('goodbye')
    pygame.quit()
    sys.exit()

def Dissolve(first,second,speed):
    x = 1
    y = 255
    diss_1 = pygame.Surface((screen_width,screen_height))
    diss_1.fill(black)
    diss_2= pygame.Surface((screen_width,screen_height))
    diss_2.fill(black)
    diss_1.set_alpha(x)
    diss_2.set_alpha(y)
    diss_1.blit(first,(0,0))
    diss_2.blit(second,(0,0))
    while x <= 255:
        diss_1.set_alpha(x)
        diss_2.set_alpha(y)
        screen_display.blit(diss_1,(0,0))
        screen_display.blit(diss_2,(0,0))
        pygame.display.flip()
        clock.tick(FPS)
        pygame.event.pump()
        x += speed
        y -= speed

pygame.init()
screen_display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
IMAGE_1 = pygame.image.load('Images/starBackground.png').convert()
IMAGE_2 = pygame.image.load('Images/sun.png').convert_alpha()
IMAGE_2 = pygame.transform.scale(IMAGE_2,(screen_width,screen_height))
IMAGE_1 = pygame.transform.scale(IMAGE_1,(screen_width,screen_height))
screen_display.fill(black)
screen_display.blit(IMAGE_2,(0,0))
pygame.display.update()
clock.tick(FPS)

Get_OUT = False
#....................

while not Get_OUT:
    for event in pygame.event.get():
        if event.type == QUIT:
            Quit_Me()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #only for debugging
                Quit_Me()
            elif event.key == pygame.K_1:
                Dissolve(IMAGE_1,IMAGE_2,2)
                screen_display.fill(black)
            elif event.key == pygame.K_2:
                Dissolve(IMAGE_2,IMAGE_1,2)

'''if pl.Planet.TIMESTEP == velocity_0:
                if velocityForward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_1
                
                if velocityBackward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_0

            if pl.Planet.TIMESTEP == velocity_1:
                if velocityForward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_2
                
                if velocityBackward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_0
            
            if pl.Planet.TIMESTEP == velocity_2:
                if velocityForward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_3
                
                if velocityBackward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_2
            
            if pl.Planet.TIMESTEP == velocity_3:
                if velocityForward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_3
                
                if velocityBackward_button.draw(WND):
                    pl.Planet.TIMESTEP = velocity_2

            #velocity_0 = pl.Planet.TIMESTEP/2
            #velocity_1 = pl.Planet.TIMESTEP
            #velocity_2 = pl.Planet.TIMESTEP*2
            #velocity_3 = pl.Planet.TIMESTEP*6'''


'''if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:

                if event.button == 5:'''

def movingBackground():
    import pygame
    import random
    import sys

    screen = pygame.display.set_mode([1024, 768])
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w
    pygame.display.set_caption('Star field') # or rain
    clock = pygame.time.Clock()


    star_field_slow = []
    star_field_medium = []
    star_field_fast = []

    for slow_stars in range(70):
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_slow.append([star_loc_x, star_loc_y]) 

    for medium_stars in range(35):
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_medium.append([star_loc_x, star_loc_y])

    for fast_stars in range(15): #1000 en otro programa para hacer efecto de lluvia
        star_loc_x = random.randrange(0, width)
        star_loc_y = random.randrange(0, height)
        star_field_fast.append([star_loc_x, star_loc_y])


    WHITE = (255, 255, 255)
    LIGHTGREY = (192, 192, 192)
    DARKGREY = (128, 128, 128)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)                

    pygame.init()

    app_is_alive = True

    while app_is_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting... All hail the void!")
                app_is_alive = False #murderer!

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()


        screen.fill(BLACK)


        for star in star_field_slow:
            star[1] += 1
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, DARKGREY, star, 3)

        for star in star_field_medium:
            star[1] += 4
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, LIGHTGREY, star, 2)

        for star in star_field_fast:
            star[1] += 8
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, BLUE, star, 1)

    
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

