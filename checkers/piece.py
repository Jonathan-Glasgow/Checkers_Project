from re import T
from .constants import *
from .board import *
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 5
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        #Each piece needs a direction it can go (up, down, both)
        #White is at the top, and will move down (positive), Red will be at the bottom, and move up (or negative)
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1
            
        #creating position variables to store later
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    
    
    def calc_pos(self):
        #Pieces are circular and should be drawn from the center of a square, thus we need to find the midpoint of our square
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2      #x = (squaresize * col) + (squaresize / 2 rounded down)
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    
    
    def make_king(self):
        self.king = True
        
    
    
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, PURPLE, (self.x, self.y), radius + self.OUTLINE)  #outline color
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)           #piece color
        
        if self.king:   #draws the crown in the center of piece. Need to offset a bit to the top-left to make it look right
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))
    
    
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    
    
    #avoids garbage returns?
    def __repr__(self):
        return str(self.color)