import pygame 
import numpy as np

# Object Classes

# NOTES
# If the Z value is set to one then nothing will change
# If the Z value is set to zero then the point won't render

# Point Class
class Point:
    def __init__(self, xPos:float, yPos:float, zPos:float): #zPos:float):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos

    def rotate(self, angle:float):
        # This is just a rotation matrix

        # do trig function
        cosineAngle = np.cos(angle)
        sineAngle = np.sin(angle)

        oldxPos = self.xPos
        # apply to positions
        self.xPos = oldxPos * cosineAngle - self.zPos * sineAngle
        self.zPos = oldxPos * sineAngle + self.zPos * cosineAngle

    def find_screen_position(self, zOffset:float, angle:float, display:pygame.surface.Surface):
        
        # Rotate it first
        self.rotate(angle)

        translatedZ = self.zPos + 1 + zOffset # add a offset to a Z Position

        projectX = self.xPos / translatedZ
        projectY = self.yPos / translatedZ

        screen_x = ((projectX + 1) / 2) * display.get_width()
        screen_y = (1 - (projectY + 1) / 2) * display.get_height()

        return pygame.Vector2(screen_x, screen_y)

# Drawing Variables
next_screen_pos = pygame.Vector2()
current_screen_pos = pygame.Vector2()

# Cube Class
class Cube:
    def __init__(self, x:float, y:float, z:float, size:float):

        # Default Points with size
        self.Points = np.array([
            # First plane
            Point( size + x,  size + y, size + z), # Top Right
            Point(-size + x,  size + y, size + z), # Top Left
            Point(-size + x, -size + y, size + z), # Bottom Left
            Point( size + x, -size + y, size + z), # Bottom Right
            
            # Other plane
            Point( size + x, -size + y,  -size + z), # Bottom Right
            Point(-size + x, -size + y,  -size + z), # Bottom Left
            Point(-size + x,  size + y,  -size + z), # Top Left
            Point( size + x,  size + y,  -size + z), # Top Right
        ])

        # Faces for drawing the cube
        self.Faces = [
            [0,1,2,3], # first plane
            [4,5,6,7],  # other plane

            # Connectors
            [0,7],
            [1,6],
            [2,5],
            [3,4]
        ]

    def Draw_Cube(self, display:pygame.surface.Surface, angle:float, ZOffset:float, thickness:int, color:str):
        for face in self.Faces:
            for j in range(len(face)):
                current_screen_pos = self.Points[face[j]].find_screen_position(ZOffset, angle, display)
                next_screen_pos = self.Points[face[(j+1)%len(face)]].find_screen_position(ZOffset, angle, display) # find the next points
                pygame.draw.line(display,  color, next_screen_pos, current_screen_pos, width=thickness)

# Prism Class
class Prism:
    def __init__(self, x:float, y:float, z:float, width:float, height:float, depth:float):

        # Default Points with size
        self.Points = np.array([
            # First plane
            Point( width + x,  height + y, depth + z), # Top Right
            Point(-width + x,  height + y, depth + z), # Top Left
            Point(-width + x, -height + y, depth + z), # Bottom Left
            Point( width + x, -height + y, depth + z), # Bottom Right
            
            # Other plane
            Point( width + x, -height + y,  -depth + z), # Bottom Right
            Point(-width + x, -height + y,  -depth + z), # Bottom Left
            Point(-width + x,  height + y,  -depth + z), # Top Left
            Point( width + x,  height + y,  -depth + z), # Top Right
        ])

        # Faces for drawing the Prism
        self.Faces = [
            [0,1,2,3], # first plane
            [4,5,6,7],  # other plane

            # Connectors
            [0,7],
            [1,6],
            [2,5],
            [3,4]
        ]
    def Draw_Prism(self, display:pygame.surface.Surface, angle:float, OffsetZ:float, thickness:int, color:str):
        for face in self.Faces:
            for j in range(len(face)):
                current_screen_pos = self.Points[face[j]].find_screen_position(OffsetZ, angle, display)
                next_screen_pos = self.Points[face[(j+1)%len(face)]].find_screen_position(OffsetZ, angle, display) # find the next points
                pygame.draw.line(display,  color, next_screen_pos, current_screen_pos, width=thickness)

# Pyramid Class for a normal square pyramid
class Pyramid:
    def __init__(self, x:float, y:float, z:float, width:float, height:float):
        
        # Define points -> 5 points in a square pyramid
        self.Points = np.array([
            # Bottom square
            Point(-width + x, y, width + z), # close Left
            Point(-width + x, y, -width + z), # far Left
            Point(width + x, y, -width + z), # close Right
            Point(width + x, y, width + z), # far Right

            # Top point
            Point(x, y + height, z) 
        ])

        # Define Faces
        self.Faces = [
            # Connect the bottom
            [0,1,2,3],

            # Connectors to the top point
            [0,4],
            [1,4],
            [2,4],
            [3,4]
        ]
        

    def Draw_Pyramid(self, display:pygame.surface.Surface, angle:float, OffsetZ:float, thickness:int, color:str):
        for face in self.Faces:
            for j in range(len(face)):
                current_screen_pos = self.Points[face[j]].find_screen_position(OffsetZ, angle, display)
                next_screen_pos = self.Points[face[(j+1)%len(face)]].find_screen_position(OffsetZ, angle, display) # find the next points
                pygame.draw.line(display,  color, next_screen_pos, current_screen_pos, width=thickness)