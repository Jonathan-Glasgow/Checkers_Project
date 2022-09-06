#Holds constants for checkers game
import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8

# // is just dividing C style. Rounds down to the nearest whole int, no decimals.
# The size of a single square is 800 / 8 = 100 pixels.
SQUARE_SIZE = WIDTH//COLS   

#Pygame uses colors in (r,g,b)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (150, 50, 200)

#creates and scales the image
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))

 

