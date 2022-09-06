#Main file that controls the game state
import pygame
from checkers import *  #imports everything from the checkers folder, reads from .\checkers\__init__.py


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
                board.move(piece, 4, 3)
            
        board.draw(WIN) #draws and updates the window after every event
        pygame.display.update()
    
    #if run == false and the loop breaks, the game ends 
    pygame.quit()
    
    
main()
