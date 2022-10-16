import pygame
import math
#from pygame import gfxdraw

pygame.init()

WIDTH = 1366
HEIGHT = 768

systemFont = pygame.font.Font('Fonts/pixeldust/pixeldue.ttf', 16)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Planet:
    G = 6.67428e-11 
    AU = 149.6e6 * 1000 #Astronomical Unit: Distancia promedio Tierra-Sol (metros)
    SCALE = 200 / AU #Escala apropiada (cuantos pixeles son un metro, ej) 1AU = 100 pixeles. Cambiar escala a gusto
    TIMESTEP = 3600*24 #1 día 3600*24
    solarS = True
    anotherS = False
    
    #""__init__ = Constructor""
    def __init__(self, x, y, color, mass):
        self.x = x
        self.y = y
        self.color = color
        self.mass = mass

        self.radius = 0
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0 
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        #Órbita
        #Se almacenan las coordenadas x e y para cada punto de la órbita
        
        if len(self.orbit) > 2: #Si ya se han calculado más de 2 coordenadas (x, y) 
            updated_points = [] #Lista que almacenará las coordenadas de cada punto a medida que se calculan*

            for point in self.orbit:
                x, y = point 
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2

                updated_points.append((x, y))

                if self.solarS == True:
                    if Planet.SCALE == (200 / Planet.AU)/0.002:
                        if len(updated_points) > 30:
                            del updated_points[-31]
                    
                    if Planet.SCALE == (200 / Planet.AU)/0.2:
                        if len(updated_points) > 15:
                            del updated_points[-16]

                    if Planet.SCALE == (200 / Planet.AU):
                        if len(updated_points) > 50:
                            del updated_points[-51]
                    
                    if Planet.SCALE == (200 / Planet.AU)*0.5:
                        if len(updated_points) > 30:
                            del updated_points[-31]     

                    if Planet.SCALE == (200 / Planet.AU)*0.1:
                        if len(updated_points) > 30:
                            del updated_points[-31]
                    
                    if Planet.SCALE == (200 / Planet.AU)*0.06:
                        if len(updated_points) > 2:
                            del updated_points[-3]

                    if Planet.SCALE == (200 / Planet.AU)*0.005:
                        if len(updated_points) > 2:
                            del updated_points[-3]
                            
                    if Planet.SCALE == (200 / Planet.AU)/0.009:
                        if self.radius < 1:
                            if len(updated_points) > 2:
                                del updated_points[-3]
                
                elif self.anotherS == True:
                    if Planet.SCALE == (200 / Planet.AU)/0.04:
                        if self.radius == 1:
                            if len(updated_points) > 30:
                                del updated_points[-31]
                        
                        if self.radius == 2:
                            if len(updated_points) > 50:
                                del updated_points[-51]

                        if self.radius == 3:
                            if len(updated_points) > 50:
                                del updated_points[-51]

                        if self.radius == 4:
                            if len(updated_points) > 50:
                                del updated_points[-51]
                    
                    if Planet.SCALE == (200 / Planet.AU):
                        if len(updated_points) > 2:
                            del updated_points[-3]

            pygame.draw.lines(win, self.color, False, updated_points, 1)
            
            updated_points = []
            #Vaciar lista self.orbit = [] para rendimiento
            
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        #pygame.gfxdraw.aacircle(win, int(x), int(y), self.radius, self.color) 
           

        if (self.sun and Planet.SCALE == ((200 / Planet.AU)*0.005)):
            sunMarker = systemFont.render('SOL', False, WHITE)
            win.blit(sunMarker, (683, 384))
            #distance_text = FONT.render(f"{round(self.distance_to_sun/1000), 1}km", 1, WHITE)
            #win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

    def attraction(self, other):
        #Distancia:
        #Las coordenadas x e y (lados 'a' y 'b') nos ayudan a calcular el lado 'c' del triangulo que se 
        #forma entre ambos objetos, siendo 'c' entonces la distancia (hipotenusa) entre ambos cuerpos.
        
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y **2) #c^(2) = a^(2) + b^(2) -> c = √(a^(2) + b^(2))

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2 #Gravitación universal F = (M1*M2) / r^2
        theta = math.atan2(distance_y, distance_x) #arco tangente en radianes de x, y

        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        #Velocidad
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        #Posición
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
