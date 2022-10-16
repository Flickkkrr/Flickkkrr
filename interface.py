import pygame
import planet as pl
import sprite as sp
import button as btn
import sys
#import glfw #OpenGl
#import logging

pygame.display.set_caption("Cosmos")
WND = pygame.display.set_mode((1366, 768), pygame.RESIZABLE) #1366, 768

monitor_resolution = [pygame.display.Info().current_w, pygame.display.Info().current_h]
FULLSCREEN = False

mainMFont = pygame.font.Font('Fonts/ExtrosBackstage.ttf', 55)
mainMFont2 = pygame.font.Font('Fonts/Dogica/dogica.ttf', 10)
mainMFont3 = pygame.font.Font('Fonts/pixeldust/pixeldue.ttf', 17)
systemFont = pygame.font.Font('Fonts/pixeldust/pixeldue.ttf', 18)
systemFont2 = pygame.font.Font('Fonts/pixeldust/pixeldue.ttf', 19)

#Valores RGB 
WHITE = (255, 255, 255) #¿Se puede agregar valores alpha? (255, 255, 255, 128)
YELLOW = (255, 255, 0)
BLUE = (40, 53, 147)
DARKBLUE = (12, 25, 109)
RED = (188, 39, 50)
DARK_GREY = (80, 71, 81)
BLACK = (0, 0, 0)
BROWN = (118, 85, 27)
BEAGE = (197, 161, 98)
LIGHTBLUE = (123, 157, 164)

OCRE = (151, 152, 59)
ORANGE = (212, 69, 27)
LIGHT_GREY = (154, 149, 149)
GREEN = (42, 143, 78)

#Usar sprite sheet*
zoomIn_img = pygame.image.load('Images/Icons/zoomIn.png').convert_alpha() 
zoomOut_img = pygame.image.load('Images/Icons/zoomOut.png').convert_alpha()
pause_img = pygame.image.load('Images/Icons/pause.png').convert_alpha()
play_img = pygame.image.load('Images/Icons/play.png').convert_alpha()
velocityForward_img = pygame.image.load('Images/Icons/velocity1.png').convert_alpha()
velocityBackward_img = pygame.image.load('Images/Icons/velocity2.png').convert_alpha()
backButton_img = pygame.image.load('Images/Icons/back.png').convert_alpha()
anotherSystem_img = pygame.image.load('Images/Icons/anotherSystem.png').convert_alpha()
solarSystem_img = pygame.image.load('Images/Icons/solarSystem.png').convert_alpha()
starBackground_img = pygame.image.load('Images/Icons/starBackground.png').convert()
menuBackground_img = pygame.image.load('Images/Icons/menuBackground.png').convert()
subScaleIcon1_img = pygame.image.load('Images/Icons/subScaleIcon1.png').convert_alpha()
subScaleIcon2_img = pygame.image.load('Images/Icons/subScaleIcon2.png').convert_alpha()
play_img = pygame.image.load('Images/Icons/play.png').convert_alpha()

sunBtn_img = pygame.image.load('Images/Icons/sun.png').convert_alpha()
mercuryBtn_img = pygame.image.load('Images/Icons/mercury.png').convert_alpha()
venusBtn_img = pygame.image.load('Images/Icons/venus.png').convert_alpha()
earthBtn_img = pygame.image.load('Images/Icons/earth.png').convert_alpha()
moonBtn_img = pygame.image.load('Images/Icons/moon.png').convert_alpha()
marsBtn_img = pygame.image.load('Images/Icons/mars.png').convert_alpha()
asteroidsBBtn_img = pygame.image.load('Images/Icons/asteroidsB.png').convert_alpha()
jupiterBtn_img = pygame.image.load('Images/Icons/jupiter.png').convert_alpha()
saturnBtn_img = pygame.image.load('Images/Icons/saturn.png').convert_alpha()
uranusBtn_img = pygame.image.load('Images/Icons/uranus.png').convert_alpha()
neptuneBtn_img = pygame.image.load('Images/Icons/neptune.png').convert_alpha()
kuiperBBtn_img = pygame.image.load('Images/Icons/kuiperB.png').convert_alpha()
oortCBtn_img = pygame.image.load('Images/Icons/oortC.png').convert_alpha()

zoom_in_button = btn.Button(1286, 650, zoomIn_img, 0.09)
zoom_out_button = btn.Button(1216, 650, zoomOut_img, 0.09)
pause_button = btn.Button(1286, 570, pause_img, 0.09)
velocityForward_button = btn.Button(1150, 570, velocityForward_img, 0.09)
velocityBackward_button = btn.Button(1070, 570, velocityBackward_img, 0.09)
back_button = btn.Button(1070, 570, backButton_img, 0.09)
anotherSystem_button = btn.Button(1290, 26, anotherSystem_img, 0.11)
solarSystem_button = btn.Button(1290, 26, solarSystem_img, 0.11)
subScaleIn_button = btn.Button(180, 13, subScaleIcon1_img, 0.03)
subScaleOut_button = btn.Button(165, 13, subScaleIcon2_img, 0.03)
play_button = btn.Button(1000, 570, play_img, 0.09)

# --------------------------------------------------------------------------------- #

sun_button  = venus_button = btn.Button(20, 350, sunBtn_img, 0.16)
mercury_button = btn.Button(39, 231, mercuryBtn_img, 0.06)
venus_button = btn.Button(36, 291, venusBtn_img, 0.08)
earth_button = btn.Button(33, 362, earthBtn_img, 0.09)
moon_button = btn.Button(83, 376, moonBtn_img, 0.023)
mars_button =  btn.Button(38, 461, marsBtn_img, 0.07)
asteroidsB_button = btn.Button(17, 350, asteroidsBBtn_img, 0.2)
jupiter_button = btn.Button(32, 271, jupiterBtn_img, 0.12)
saturn_button = btn.Button(34, 361, saturnBtn_img, 0.11)
uranus_button = btn.Button(37, 461, uranusBtn_img, 0.09)
neptune_button = btn.Button(38, 561, neptuneBtn_img, 0.08)
kuiperB_button = btn.Button(39, 361, kuiperBBtn_img, 0.09)
oortC_button = btn.Button(20, 350, oortCBtn_img, 0.16)

def zoomIn(): #Revisar
    scaleMin = int(pl.Planet.SCALE/0.2)
    scaleMax = int(pl.Planet.SCALE*0.005)

    for scale in range(scaleMin, scaleMax):
        pl.Planet.SCALE = scale
    
def fadeIn(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0)) #Negro
    
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        WND.blit(fade, (0, 0))
        pygame.display.update()

def fadeOut():
    #fade = pygame.Surface((width, height))
    #fade.fill((0, 0, 0))
    alpha = 300

    for alpha in range(0, 300):
        WND.blit(starBackground_img, (0, 0))
        alpha -=1
        WND.set_alpha(alpha)
            
        pygame.display.update()

def fadeOutText(welcome):
    alpha = 300

    for alpha in range(0, 300):
        WND.blit(menuBackground_img, (0, 0))
        alpha -=1
        welcome.set_alpha(alpha)
            
        pygame.display.update()

def screenSave(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0)) #Negro
    
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        WND.blit(fade, (0, 0))
        pygame.display.update()

def mainMenu():
    run = True
    firstT = False
    clock = pygame.time.Clock()
    camera_x = 0
    camera_y = 0

    star = pl.Planet(-0.7 * pl.Planet.AU, 0, RED, 1.98892 * 10**30)
    star.sun = True
    star.radius = 350

    planet = pl.Planet(0.023 * pl.Planet.AU, 0, DARK_GREY, 4.8685 * 10**24)
    planet.y_vel = -35.02 * 1000
    planet.radius = 7

    planet2 = pl.Planet(-1.7 * pl.Planet.AU, 0, BLUE, 5.9742 * 10**24)
    planet2.y_vel = 29.78 * 1000

    planet2.radius = 7

    menuS = [star, planet, planet2]
    pl.Planet.TIMESTEP = 2000
    pl.Planet.SCALE = (200 / pl.Planet.AU)/0.2 #+0.001
    
    pygame.init()

    while run:
        global WND, FULLSCREEN
        clock.tick(60) #FPS
        
        WND.fill(BLACK)
        WND.blit(menuBackground_img, (camera_x, camera_y))

        title = mainMFont.render('COSMOS', False, WHITE)
        WND.blit(title, (1000, 250))

        if firstT == False:
            welcome = mainMFont3.render('PULSA EL NUMERO UNO (1)', False, WHITE)
            WND.blit(welcome, (1000, 350))  
  
        if firstT == True:                
            fadeIn(1366, 768)
            pl.Planet.TIMESTEP = 3600 * 24
            pl.Planet.SCALE = (200 / pl.Planet.AU)
            simulation()
            run = False

        for planet in menuS:
            planet.update_position(menuS)
            planet.draw(WND)            
            
        for event in pygame.event.get():      
            if event.type == pygame.VIDEORESIZE:
                if not FULLSCREEN:
                    WND = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                
            elif event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_f:
                    FULLSCREEN = not FULLSCREEN

                    if FULLSCREEN:
                        WND = pygame.display.set_mode(monitor_resolution, pygame.FULLSCREEN)
                    else:
                        WND = pygame.display.set_mode(monitor_resolution, pygame.RESIZABLE)

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if event.key == pygame.K_1:
                    alpha = 600

                    for alpha in range(0, 600):
                        alpha -=1
                        welcome.set_alpha(alpha)
                        pygame.display.update()
                        
                    firstT = True

            elif event.type == pygame.QUIT:
                run = False         
        
        pygame.display.update()

    pygame.quit()

def simulation():
    run = True
    clock = pygame.time.Clock()
    paused = False

    solarSystem = True
    anotherSystem = False

    ceresSubScale = False
    jupiterFlyOverSubScale = False #Que rote (subescala en movimiento)
    earthMoonSystemSubScale = False
    jupiterMoonsSystemSubScale = False
    plutoSubScale = False

    planetDetail = False
    sunDetail = False
    mercuryDetail = False
    venusDetail = False
    earthDetail = False
    moonDetail = False
    marsDetail = False
    asteroidsBDetail = False
    jupiterDetail = False
    saturnDetail = False
    uranusDetail = False
    neptuneDetail = False
    kuiperBDetail = False
    oortCDetail = False

    def toggle_pause():
        nonlocal paused 

        if paused == True:
            paused = False

        else:
            paused = True
        
        return paused
    
    #Valores predeterminados de los cuerpos celestes (scale_1)
    sun = pl.Planet(0, 0, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    mercury = pl.Planet(0.387 * pl.Planet.AU, 0, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000 #Km/s * 1000 para obtener M/s

    venus = pl.Planet(0.723 * pl.Planet.AU, 0, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    earth = pl.Planet(-1 * pl.Planet.AU, 0, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.78 * 1000
        
    mars = pl.Planet(-1.524 * pl.Planet.AU, 0, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
            
    #asteroidsB = pl.Planet(-3 * pl.Planet.AU, 0, DARK_GREY, 3.3 * 10**21) #¿Hacer uno que represente todo o varios independientes? ¿Alargar órbita para representar anillo o no?
    #asteroidsB.y_vel = 17.88 * 1000

    jupiter = pl.Planet(-5.2 * pl.Planet.AU, 0, BROWN, 1.898 * 10**27) #Revisar parámetro de UA
    jupiter.y_vel = 13.07 * 1000 

    saturn = pl.Planet(-9.5 * pl.Planet.AU, 0, BEAGE, 5.6834 * 10**26)
    saturn.y_vel = 9.68 * 1000

    uranus = pl.Planet(19.8 * pl.Planet.AU, 0, LIGHTBLUE, 8.681 * 10**25)
    uranus.y_vel = -6.80 * 1000

    #La posición inicial 'x' no puede ser la misma. ZeroDivisionError: float division by zero
    neptune = pl.Planet(30 * pl.Planet.AU, 0, DARKBLUE, 1.024 * 10**26)
    neptune.y_vel = -5.43 * 1000

    #kuiperB = pl.Planet(40 * pl.Planet.AU, 0, DARK_GREY, 1.01 * 10*22)  
    #kuiperB.y_vel = -4.43 * 1000 #Cambiar

    planetsSS = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # ------------------------------------------------------------------------------------------------------ #
    trappist = pl.Planet(0, 0, RED, 1.77 * 10**29)
    trappist.sun = True

    b = pl.Planet(-0.01154775 * pl.Planet.AU, 0, ORANGE, 6.077592 * 10**24)
    b.y_vel = -82692.92 #M/s

    c = pl.Planet(0.01581512 * pl.Planet.AU, 0, OCRE, 6.908256 * 10**24)
    c.y_vel = 82552.94

    d = pl.Planet(-0.02228038 * pl.Planet.AU, 0, LIGHT_GREY, 1.77487 * 10**24) #Esta órbita se cruza con las demás, revisar. 
    d.y_vel = -59514.87

    e = pl.Planet(0.02928285 * pl.Planet.AU, 0, BLUE, 4.613472 * 10**24)
    e.y_vel = 51913.48

    f = pl.Planet(-0.03853361 * pl.Planet.AU, 0, DARKBLUE, 5.581584 * 10**24)
    f.y_vel = -45255.04

    g = pl.Planet(-0.04687692 * pl.Planet.AU, 0, GREEN, 6.860448 * 10**24)
    g.y_vel = -41030.54

    h = pl.Planet(0.06193488 * pl.Planet.AU, 0, LIGHTBLUE, 1.978056 * 10**24)
    h.y_vel = 35695.97

    planetsAS = [trappist, b, c, d, e, f, g, h]

    # -------------------------------------------------------------------------------- #
    earth2 = pl.Planet(0, 0, BLUE, 5.9736 * 10**24)
    earth2.sun = True

    moon = pl.Planet(0.002569555 * pl.Planet.AU, 0, DARK_GREY, 7.349 * 10**22)
    moon.y_vel = 1 * 1000

    objectsEM = [earth2, moon]

    # -------------------------------------------------------------------------------- #
    #¿Cambiar escala o hacer una simulacion nueva? (No sé si se consiga el mismo efecto) // Escala un poco más interactiva (tiene satelites muy pequeños)
    jupiter2 = pl.Planet(0, 0, BROWN, 1.898 * 10**27)
    jupiter2.sun = True
    
    #Grupo de Amaltea
    metis = pl.Planet(0.000855627152 * pl.Planet.AU, 0, WHITE, 1.2 * 10**17)
    metis.y_vel = 31.501 * 1000

    adrastea = pl.Planet(0.000862311739 * pl.Planet.AU, 0, WHITE, 1.8 * 10**16)
    adrastea.y_vel = 29.56 * 1000

    amalthea = pl.Planet(0.00122220991 * pl.Planet.AU, 0, WHITE, 2.1 * 10**18)
    amalthea.y_vel = 26.57 * 1000

    thebe = pl.Planet(0.00148397834 * pl.Planet.AU, 0, WHITE, 4.3 * 10**17)
    thebe.y_vel = 23.92 * 1000

    #Satelites Galileanos

    io = pl.Planet(0.00281889039 * pl.Planet.AU, 0, YELLOW, 8.931938 * 10**22)
    io.y_vel = 17.334 * 1000

    europa = pl.Planet(0.00452505104 * pl.Planet.AU, 0, WHITE, 4.799844 * 10**22)
    europa.y_vel = 13.74 * 1000

    ganymede = pl.Planet(0.007147160551 * pl.Planet.AU, 0, DARK_GREY, 1.4819 * 10**23)
    ganymede.y_vel = 10.88 * 1000

    callisto = pl.Planet(0.01268066177 * pl.Planet.AU, 0, RED, 1.075938 * 10**23)
    callisto.y_vel = 8.204 * 1000

    #Grupo de Himalia

    himalia = pl.Planet(0.07649173044 * pl.Planet.AU, 0, DARK_GREY, 6.7 * 10**18)
    himalia.y_vel = 3.312 * 1000

    objectsJM = [jupiter2, io, europa, ganymede, callisto, amalthea, himalia, thebe, metis, adrastea] #, +70 lunas
    
    scaleSS_0 = (200 / pl.Planet.AU)/0.2 #Estrella madre
    scaleSS_1 = 200 / pl.Planet.AU #Planetas rocosos
    scaleSS_2 = (200 / pl.Planet.AU)*0.5 #Cinturón de asteroides
    #Subescala Ceres
    scaleSS_3 = (200 / pl.Planet.AU)*0.1 #Gigantes gaseosos
    #Subescala anillos de Saturno +info
    #Subescala de algunas lunas de Saturno-Jupiter +info
    #Subescala 'sobrevolando Júpiter'
    scaleSS_4 = (200 / pl.Planet.AU)*0.06 #Cinturón de Kuiper
    #Subescala Plutón
    #Subescala Cometa Halley
    scaleSS_5 = (200 / pl.Planet.AU)*0.005 #Nube de Oort
    #scale_&  #*Subescala* Asteroides de órbita larga (no sé, algo como lo de "La materia oscura y los dinosaurios")

    #Etc.

    scaleAS_0 = (200 / pl.Planet.AU)/0.04 #Trappist
    scaleAS_1 = 200 / pl.Planet.AU #Inmediaciones
    #scaleAS_2 = (200 / pl.Planet.AU)*0.5

    scaleJS_0 = (200 / pl.Planet.AU)/0.001
    scaleJS_1 = (200 / pl.Planet.AU)/0.009
    scaleJS_2 = (200 / pl.Planet.AU)/0.015
    scaleJS_3 = (200 / pl.Planet.AU)/0.030
    scaleJS_4 = (200 / pl.Planet.AU)/0.045
    scaleJS_5 = (200 / pl.Planet.AU)/0.080
    scaleJS_6 = (200 / pl.Planet.AU)/0.095

    camera_x = 0
    camera_y = 0
        
    pygame.init()

    x = 0
    #Podría poner cada sistema (incluyendo subescalas) en funciones distintas, pero eso me quitaría la continuidad en 2do plano que busco.
    while run:
        global WND, FULLSCREEN, pause_button
        clock.tick(60) #FPS
        WND.fill(BLACK)
        WND.blit(starBackground_img, (camera_x, camera_y))
        #camera_x -= 2 #-pygame.mouse.get_pos()[0]
        
        if solarSystem == True:
            text_surface = systemFont.render('SISTEMA SOLAR', False, WHITE)
            WND.blit(text_surface, (10, 10))
            
            if anotherSystem_button.draw(WND):
                fadeIn(1366, 768)
                solarSystem = False
                pl.Planet.TIMESTEP = 100
                pl.Planet.SCALE = 200 / pl.Planet.AU
                anotherSystem = True
                pl.Planet.anotherS = True
                pl.Planet.solarS = False
                
            #Se asume que los cuerpos celestes con radio 0 no aparecerían a esta escala, de hacerlo debido a alguna función futura (colisiones, desvío de órbita, etc), reajustar radio que tenían
            if pl.Planet.SCALE == scaleSS_0:
                text_surface = systemFont.render('SOL', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('<1 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))
                
                sun.radius = 300
                mercury.radius = 7
                venus.radius = 9
                earth.radius = 0 #24
                mars.radius = 0 #18
                #asteroidsB.radius = 0 #5
                jupiter.radius = 0 #25
                saturn.radius = 0 #22
                uranus.radius = 0 #17
                neptune.radius = 0 #22

                if sun_button.draw(WND):
                    #print("Sol")
                    planetDetail = True
                    sunDetail = True
                
                if zoom_in_button.draw(WND):
                    x += 1
                    pl.Planet.SCALE = scaleSS_0
                    
                if x == 5:
                    #Funciones a programar
                    x = 0

                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleSS_1

            if pl.Planet.SCALE == scaleSS_1:
                text_surface = systemFont.render('PLANETAS ROCOSOS', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~1.5 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                sun.radius = 50
                mercury.radius = 5
                venus.radius = 14
                earth.radius = 16
                mars.radius = 12
                #asteroidsB.radius = 5
                jupiter.radius = 0 #25
                saturn.radius = 0 #22
                uranus.radius = 0 #17
                neptune.radius = 0 #22

                if mercury_button.draw(WND):
                    planetDetail = True
                    mercuryDetail = True
                    #print("Mercurio")

                if venus_button.draw(WND):
                    planetDetail = True
                    venusDetail = True
                    #print("Venus")

                if earth_button.draw(WND):
                    planetDetail = True
                    earthDetail = True
                    #print("Tierra")

                if moon_button.draw(WND):
                    planetDetail = True
                    moonDetail = True
                    #print("Luna")

                if mars_button.draw(WND):
                    planetDetail = True
                    marsDetail = True
                    #print("Marte")
                
                if subScaleIn_button.draw(WND):
                    fadeIn(1366, 768)
                    pl.Planet.SCALE = (200 / pl.Planet.AU)/0.002
                    pl.Planet.TIMESTEP = 3600
                    earthMoonSystemSubScale = True
                    solarSystem = False
                    
                if zoom_in_button.draw(WND):
                    pl.Planet.SCALE = scaleSS_0

                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleSS_2
                    #    
                
            if pl.Planet.SCALE == scaleSS_2:
                text_surface = systemFont.render('CINTURÓN DE ASTEROIDES', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~3 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                sun.radius = 20
                mercury.radius = 4
                venus.radius = 7
                earth.radius = 8
                mars.radius = 6
                #asteroidsB.radius = 5
                jupiter.radius = 32
                saturn.radius = 0 #27
                uranus.radius = 0 #22
                neptune.radius = 0 #27

                if asteroidsB_button.draw(WND):
                    planetDetail = True
                    asteroidsBDetail = True
                    #print("Cinturón de asteroides")
                
                if subScaleIn_button.draw(WND):
                    #fadeIn(1366, 768)
                    #pl.Planet.TIMESTEP == 100
                    #solarSystem = False
                    print("Ceres") #quitar print cuando hayan otras funciones

                if zoom_in_button.draw(WND):
                    pl.Planet.SCALE = scaleSS_1
                
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleSS_3

            if pl.Planet.SCALE == scaleSS_3:
                text_surface = systemFont.render('GIGANTES GASEOSOS', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~50 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                sun.radius = 12
                mercury.radius = 0
                venus.radius = 1
                earth.radius = 1
                mars.radius = 1
                #asteroidsB.radius = 3
                jupiter.radius = 25
                saturn.radius = 19
                uranus.radius = 17
                neptune.radius = 22

                if jupiter_button.draw(WND):
                    #print("Jupiter")
                    planetDetail = True
                    jupiterDetail = True

                if saturn_button.draw(WND):
                    #print("Saturno")
                    planetDetail = True
                    saturnDetail = True
                
                if uranus_button.draw(WND):
                    #print("Urano")
                    planetDetail = True
                    uranusDetail = True

                if neptune_button.draw(WND):
                    #print("Neptuno")
                    planetDetail = True
                    neptuneDetail = True
                
                if subScaleIn_button.draw(WND):
                    fadeIn(1366, 768)
                    pl.Planet.SCALE = (200 / pl.Planet.AU)/0.009
                    pl.Planet.TIMESTEP = 300
                    jupiterMoonsSystemSubScale = True
                    solarSystem = False
                    #print("Júpiter")
                    #print("Lunas Saturno")
                    #print("Lunas Jupiter")
                    #print("Anillos de Saturno")

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleSS_2

                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleSS_4
            
            if pl.Planet.SCALE == scaleSS_4:
                text_surface = systemFont.render('CINTURÓN DE KUIPER', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('<70 UA', False, WHITE) 
                WND.blit(text_surface, (10, 50))
                
                sun.radius = 12
                mercury.radius = 0
                venus.radius = 0
                earth.radius = 0
                mars.radius = 0
                #asteroidsB.radius = 0
                jupiter.radius = 16
                saturn.radius = 13
                uranus.radius = 7
                neptune.radius = 11
                #kuiperB.radius = 6
                
                if kuiperB_button.draw(WND):
                    #print("Cinturón de Kuiper")
                    planetDetail = True
                    kuiperBDetail = True

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleSS_3
                
                if zoom_out_button.draw(WND):
                    fadeIn(1366, 768)
                    pl.Planet.SCALE = scaleSS_5

            # Acerca del cambio de velocidad utilizando TIMESTEP...
            if pl.Planet.SCALE == scaleSS_5: 
                text_surface = systemFont.render('NUBE DE OORT', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('>100.000 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))
                
                sun.radius = 1
                mercury.radius = 0
                venus.radius = 0
                earth.radius = 0 
                mars.radius = 0 
                #asteroidsB.radius = 0 
                jupiter.radius = 0
                saturn.radius = 0
                uranus.radius = 0
                neptune.radius = 0
                #kuiperB.radius = 0

                if oortC_button.draw(WND):
                    #print("Nube de Oort")
                    planetDetail = True
                    oortCDetail = True

                if zoom_in_button.draw(WND):
                    fadeIn(1366, 768)
                    pl.Planet.SCALE = scaleSS_4
                
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleSS_5
            
            for planet in planetsSS:
                planet.draw(WND)     
        
        elif anotherSystem == True:
            
            text_surface = systemFont.render('TRAPPIST-1', False, WHITE)
            WND.blit(text_surface, (10, 10))

            if solarSystem_button.draw(WND):
                fadeIn(1366, 768)
                anotherSystem = False
                pl.Planet.TIMESTEP = (3600*24)
                pl.Planet.SCALE = 200 / pl.Planet.AU
                solarSystem = True
                pl.Planet.anotherS = False
                pl.Planet.solarS = True

                #fadeOut(1366, 768)      

            if pl.Planet.SCALE == scaleAS_0:
                
                text_surface = systemFont.render('2MASS J23062928-0502285', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('<0.061 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                #text_surface = systemFont2.render('Constelación de Acuario', False, WHITE)
                #WND.blit(text_surface, (10, 600))

                trappist.radius = 50
                b.radius = 4
                c.radius = 4
                d.radius = 1
                e.radius = 2
                f.radius = 3
                g.radius = 4
                h.radius = 1

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleAS_0
                
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleAS_1

            if pl.Planet.SCALE == scaleAS_1:
                text_surface = systemFont.render('INMEDIACIONES', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('<1 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))
                
                trappist.radius = 0
                b.radius = 0
                c.radius = 0
                d.radius = 0
                e.radius = 0
                f.radius = 0
                g.radius = 0
                h.radius = 0

                if zoom_in_button.draw(WND):
                    pl.Planet.SCALE = scaleAS_0
                
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleAS_1            

            for planet in planetsAS:
                planet.draw(WND)          
        
        elif earthMoonSystemSubScale == True:
            text_surface = systemFont.render('SISTEMA TIERRA-LUNA', False, WHITE)
            WND.blit(text_surface, (10, 10))
            text_surface = systemFont2.render('~1 UA', False, WHITE)
            WND.blit(text_surface, (10, 30))

            if subScaleOut_button.draw(WND):
                earthMoonSystemSubScale = False
                pl.Planet.TIMESTEP = (3600*24)
                pl.Planet.SCALE = 200 / pl.Planet.AU
                solarSystem = True
                fadeIn(1366, 768)
                #fadeOut(1366, 768)

            earth2.radius = 100
            moon.radius = 10

            for planet in objectsEM:
                planet.draw(WND)
            
        elif jupiterMoonsSystemSubScale == True:
            text_surface = systemFont.render('SISTEMA JOVIANO', False, WHITE)
            WND.blit(text_surface, (10, 10))

            if back_button.draw(WND):
                jupiterMoonsSystemSubScale = False
                pl.Planet.TIMESTEP = (3600*24)
                pl.Planet.SCALE = scaleSS_3
                solarSystem = True
                fadeIn(1366, 768)
                #fadeOut(1366, 768)
            
            if pl.Planet.SCALE == scaleJS_0: 
                text_surface = systemFont.render('GRUPO DE AMALTEA', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~5.2 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                jupiter2.radius = 50
                io.radius = 10
                europa.radius = 10
                ganymede.radius = 10
                callisto.radius = 10
                amalthea.radius = 1
                himalia.radius = 1
                thebe.radius = 1

                if zoom_in_button.draw(WND):
                    x += 1
                    pl.Planet.SCALE = scaleJS_0
                    
                if x == 5:
                    #Funciones a programar
                    x = 0
                
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleJS_1
            
            if pl.Planet.SCALE == scaleJS_1:
                text_surface = systemFont.render('SATELITES GALILEANOS', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~5.2 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                jupiter2.radius = 20
                io.radius = 10
                europa.radius = 10
                ganymede.radius = 10
                callisto.radius = 10
                amalthea.radius = 1
                himalia.radius = 1
                thebe.radius = 1

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleJS_0
                    
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleJS_2

            if pl.Planet.SCALE == scaleJS_2: 
                text_surface = systemFont.render('GRUPO DE TEMISTO', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~5.2 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                jupiter2.radius = 18
                io.radius = 4
                europa.radius = 4
                ganymede.radius = 4
                callisto.radius = 4
                amalthea.radius = 2
                himalia.radius = 2
                thebe.radius = 1

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleJS_1
                    
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleJS_3
            
            if pl.Planet.SCALE == scaleJS_3: 
                text_surface = systemFont.render('GRUPO DE HIMALIA', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~5.2 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                jupiter2.radius = 16
                io.radius = 2
                europa.radius = 2
                ganymede.radius = 2
                callisto.radius = 2
                amalthea.radius = 1
                himalia.radius = 1
                thebe.radius = 0

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleJS_2
                    
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleJS_4

            if pl.Planet.SCALE == scaleJS_4: 
                text_surface = systemFont.render('GRUPO DE ANANKÉ', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~5.2 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                jupiter2.radius = 14
                io.radius = 2
                europa.radius = 2
                ganymede.radius = 2
                callisto.radius = 2
                amalthea.radius = 0
                himalia.radius = 0
                thebe.radius = 0

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleJS_3
                    
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleJS_5

            if pl.Planet.SCALE == scaleJS_5: 
                text_surface = systemFont.render('GRUPO DE CARMÉ', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~5.2 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                jupiter2.radius = 12
                io.radius = 1
                europa.radius = 1
                ganymede.radius = 1
                callisto.radius = 1
                amalthea.radius = 0
                himalia.radius = 0
                thebe.radius = 0

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleJS_4
                    
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleJS_6
            
            if pl.Planet.SCALE == scaleJS_6: 
                text_surface = systemFont.render('GRUPO DE PASIFAE', False, WHITE)
                WND.blit(text_surface, (10, 30))

                text_surface = systemFont2.render('~5.2 UA', False, WHITE)
                WND.blit(text_surface, (10, 50))

                jupiter2.radius = 10
                io.radius = 1
                europa.radius = 1
                ganymede.radius = 1
                callisto.radius = 1
                amalthea.radius = 0
                himalia.radius = 0
                thebe.radius = 0

                if zoom_in_button.draw(WND): 
                    pl.Planet.SCALE = scaleJS_5
                    
                if zoom_out_button.draw(WND):
                    pl.Planet.SCALE = scaleJS_6

            for planet in objectsJM:
                planet.draw(WND)

        elif jupiterFlyOverSubScale == True:
            text_surface = systemFont.render('SOBREVUELO DE JUPITER', False, WHITE)
            WND.blit(text_surface, (10, 10))
            text_surface = systemFont2.render('~1 UA', False, WHITE)
            WND.blit(text_surface, (10, 30))
 
            if back_button.draw(WND):
                jupiterFlyOverSubScale = False
                pl.Planet.TIMESTEP = (3600*24)
                pl.Planet.SCALE = 200 / pl.Planet.AU
                solarSystem = True
                fadeIn(1366, 768)
                #fadeOut(1366, 768)

            jupiter2.radius = 400
            io.radius = 10
            europa.radius = 10
            ganymede.radius = 10
            callisto.radius = 10            

        if planetDetail == True:
            solarSystem = False
            
            if back_button.draw(WND):
                planetDetail = False
                sunDetail = False
                mercuryDetail = False
                venusDetail = False
                earthDetail = False
                moonDetail = False
                marsDetail = False
                asteroidsBDetail = False
                jupiterDetail = False
                saturnDetail = False
                uranusDetail = False
                neptuneDetail = False
                kuiperBDetail = False
                oortCDetail = False
                solarSystem = True

            if sunDetail == True:
                solarSystem = False
                #print("Interfaz Sol")
                
            if mercuryDetail == True:
                solarSystem = False
                #print("Interfaz Mercurio")                        
                
            if venusDetail == True:
                solarSystem = False
                #print("Interfaz Venus")                      
                
            if earthDetail == True:
                solarSystem = False
                sp.sprites.draw(WND)
                sp.sprites.update(0.2)
                
                '''for event in pygame.event.get():      
                   
                    if event.type == pygame.KEYDOWN:                
                        if event.key == pygame.K_1:
                            sp.animate()'''
                #print("Interfaz Tierra")
                
            if moonDetail == True:
                solarSystem = False
                #print("Interfaz Luna")                
                
            if marsDetail == True:
                solarSystem = False
                #print("Interfaz Marte")

            if asteroidsBDetail == True:
                solarSystem = False
                #print("Interfaz Cinturón de asteroides")                        
                
            if jupiterDetail == True:
                solarSystem = False
                #print("Interfaz Júpiter")
                
            if saturnDetail == True:
                solarSystem = False
                #print("Interfaz Saturno")
                
            if uranusDetail == True:
                solarSystem = False
                #print("Interfaz Urano")
                
            if neptuneDetail == True:
                solarSystem = False
                #print("Interfaz Neptuno")
                
            if kuiperBDetail == True:
                solarSystem = False
                #print("Interfaz Cinturón de Kuiper")
            
            if oortCDetail == True:
                solarSystem = False
                #print("Interfaz Nube de Oort")

        if pause_button.draw(WND):
            toggle_pause()
        
        if not paused:
            for planet in planetsSS:
                planet.update_position(planetsSS)

            if anotherSystem == True:
                for planet in planetsAS:
                    planet.update_position(planetsAS)
            
            elif earthMoonSystemSubScale == True:
                for planet in objectsEM:
                    planet.update_position(objectsEM)
            
            elif jupiterMoonsSystemSubScale == True:
                for planet in objectsJM:
                    planet.update_position(objectsJM)
                
        #mouse_x, mouse_y = pygame.mouse.get_pos() 
        for event in pygame.event.get():      
            if event.type == pygame.VIDEORESIZE:
                if not FULLSCREEN:
                    WND = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
            elif event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_f:
                    FULLSCREEN = not FULLSCREEN

                    if FULLSCREEN:
                        WND = pygame.display.set_mode(monitor_resolution, pygame.FULLSCREEN)
                    else:
                        WND = pygame.display.set_mode(monitor_resolution, pygame.RESIZABLE)

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                elif event.key == pygame.K_SPACE:
                    toggle_pause()
            
            elif event.type == pygame.QUIT:
                run = False         
        
        pygame.display.update()

    pygame.quit()

mainMenu()