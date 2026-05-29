# Import Modules
import pygame
import objects 

# Pygame Setup
pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
Clock = pygame.time.Clock()
pygame.display.set_caption("Rotating Cube")
running = True

# 3D objects

# Cubes
# positions are between -1 and 1
cube = objects.Cube(0, 0.35, 0, 0.75)

# Prisms
# size is between 0 and 1
# positions are between -1 and 1
prism = objects.Prism(0,-0.05,0,0.5,0.25,0.5)

# Pyramids
# size / height is between 0 and 1
# positions are between -1 and 1
pyramid = objects.Pyramid(0,0.25,0,0.5,0.65)

# Isohedron -> 12 point sphere - ish
# size is between 0 and 1
# positions are between -1 and 1
Isohedron = 0 # Not made yet

# Cylinder -> 16 point cylinder
# size / height is between 0 and 1
# positions are between -1 and 1
cylinder = 0 # Not made yet

# Custom model
# load a wavefont or obj

# dt
deltatime = 0.0

while running:
    
    # Checking for events --> quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT not pygame.quit
            running = False

    # Draw
    screen.fill((0,0,0)) # Background Color

    offsetZ  = 2.0
    angle = 0.002
    
    # Draw Cube
    cube.Draw_Cube(screen, angle, offsetZ, 2, "red")

    # Draw Prism
    prism.Draw_Prism(screen, angle, offsetZ, 2, "white")

    # Draw Pyramid
    pyramid.Draw_Pyramid(screen, angle, offsetZ, 2, "blue")
        

       


    # Flip() to render 
    pygame.display.flip()
    deltatime = Clock.tick(60) / 1000 # set max FPS to 60

# quitting
pygame.quit()
