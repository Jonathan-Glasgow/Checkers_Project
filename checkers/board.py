#Class for checkers board
from asyncore import loop
import colorsys
from tkinter.tix import ROW
import pygame
from .piece import *
from .constants import *

class Board:
    def __init__(self):
        self.board = [] #Stores piece objects in a 2-d array
        self.red_left = self.white_left = 12 #How many red and white pieces are left?
        self.red_kings = self.white_kings = 0 #init. kings
        self.create_board()
       
        
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
                
                
                
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])   #list representing what each row contains
            
            #init. board array to [white, 0, white, ...] or red, 0, ect. to keep track of piece positions
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):  #draw a piece on every other square, starting square changes based on the row number, similar to above.
                    if row < 3:                 #only draw on the right rows
                        self.board[row].append(Piece(row, col, WHITE))  #remember, .board is defined when creating the class. It's just also named board
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)   #init. middle pieces to 0

                else:
                    self.board[row].append(0)       #init every square without a piece to 0
                    


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
                        
                    
    #swaps current piece position with row/col given    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        
        if row == ROWS - 1 or row == 0: #this doesn't break the game because it only hits if you do a move
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1
        
    
    
    def get_piece(self, row, col):
        return self.board[row][col]