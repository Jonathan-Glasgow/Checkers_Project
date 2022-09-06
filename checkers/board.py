#Class for checkers board
from asyncore import loop
import pygame
#from .constants import *
from .constants import *

class Board:
    def __init__(self):
        self.board = [] #Stores piece objects in a 2-d array
        self.selected_piece = None
        self.red_left = self.white_left = 12 #How many red and white pieces are left?
        self.red_kings = self.white_kings = 0 #init. kings
        
    def draw_squares(self, win): #pass a surface (window) to draw the squares
        
        win.fill(BLACK) #init. game window as black.
        
        """     
        for(int i = 0; i < ROWS; i++) 
            for(int j = i % 2; i < ROWS; j + 2)
        
        this draws the red squares. In the first row: R | B | R | B | R | B | R | B
                                          second row: B | R | B | R | B | R | B | R
        
        1. row = 0, loops until 8, increments by 1 for each completion of col loop
        2. starts at row % 2, which is just 0 here, will carry out the loop until row 8
        3. draw red square, increment the loop by 2, now at value 2
        4. draw red squares until you reach the end of the board, skipping every other piece
        5. row = 1, loops until 8
        6. starts at row % 2, which is 1 now. Draws red squares, increments by 2
        7. colors all the odd squares in row 2, next iteration will be back to 0, coloring all even
        """
        
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                
                """
                pygame draws from top-left corner
                x increases to the right, y increases down
                draw red rectangle on the window starting at (x, y) for (x length, y length)
                will start at (0, 0) a.k.a. top-left, for the first one since arrays start at 0.
                """
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #window, color, square to draw
                