#Main file that controls the game state
import pygame
from checkers import *  #imports everything from the checkers folder, reads from .\checkers\__init__.py


"""
Explanation of Checkers:
        board is a class containing: 
            an array storing piece objects, the amount of kings left, the amount of pieces left
        
        board has functions:
            draw_squares(self,win) - fills the screen with black, then draws the red squares on the board
            create_board(self) - creates pieces from the Pieces class and assigns them to positions in board[], a 2-d array
            draw(self, win) - calls draw_squares, checks if a piece in the board array is non-zero, then calls piece.draw(win)
                            - draw can probably be merged with draw_squares... not too sure yet.
            move(self, piece, row, col) - gets the piece position and swaps it with the new position in the board array, then calls piece.move(row, col)
                                        - checks if the new space will make it a king or not, and if so, does so
            get_piece(self, row, col) - returns a piece at a position
        
        when the class Board() is called/created, it will run the function create_board() automatically
        
  
        piece is a class containing:
            row, col, color, king value, direction, and x + y positions.
            x and y positions are used for centering the images of crowns, and the piece circle
    
        piece has functions:
            calc_pos(self) - calculates the center of a square the piece is in to x, y values
            make_king(self) - self.king = True
            draw(self, win) - draws the circle, outline, and crown of a piece
            move(self, row, col) - changes a pieces row/col values to whatever's passed, and updates its x + y positions
            __repr__(self) - not sure, apparently it avoids garbage return
            
        when the class Piece() is called, it's x, y are initialized to 0, and its position is calculated
        
    
    Process:
    main() runs, creates a board class called board that will immediately run create_board.
    A board is created with red and white pieces in their correct array positions, and with any empty spots holding the value 0.
    Each position in the board array is a piece class instance, and holds its own data. It can be referenced by the array position.
    
    The clock starts and the game runs. The game will check for any events, drawing and updating the board at any instance of an event.
    When the game is created, it hits an event and calls board.draw(WIN). This calls draw_squares, creating the red and black board.
    draw_squares then checks for piece positions and calls piece.draw(win) where it hits.
    
    On the event of a click, the mouse position is calculated and then calls get_piece where it was clicked.
    The piece clicked is returned, and functions can be done on it.
    In main, board.move(piece, 7, 3) is called. This moved the clicked piece value to position row = 7, col = 3.
    board.move swaps the position given with the pieces stored position in board[], it then calls piece.move to update its stored values, and recalculate its x and y values.
    This is done so that when the event is finished and the board redraws itself, it redraws to its correct position. 
        My question: Couldn't board.draw() do all the same things piece.draw does? It seems like it.
        Then, is there any instance where piece.draw() is called when board.draw() isn't? Or vice verse? If this is the case then it's necessary to split them, but if not,
        then you could probably safe complexity by merging the two functions.
        
    The move given here moves the piece to a king position. When the board calculates .move(), it notices this and calls piece.make_king()
    
    If the close button is clicked, the game is closed.
"""


FPS = 60    #user-side variable, thus not defined in constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #Create the display environment
pygame.display.set_caption('Checkers')  #Caption for the game window


def get_row_col_from_mouse(pos):    #pos is a tuple containing x and y based on mouse
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col



#event to run the game
def main():
    
    run = True
    clock = pygame.time.Clock() #Creates the games timesense
    board = Board() #initializes/creates the board enviornment
    
    while run:  #while run == true
        clock.tick(FPS) #starts the games time
        
        for event in pygame.event.get(): #checks to see if any events in pygame are happening, such as a click, and if so, run the loop
            if event.type == pygame.QUIT:   #if user clicks the red X, game will close
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 7, 3) #test king and click
            
        board.draw(WIN) #draws and updates the window after every event
        pygame.display.update()
    
    #if run == false and the loop breaks, the game ends 
    pygame.quit()
    
    
#run program
main()
