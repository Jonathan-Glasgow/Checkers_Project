#Main file that controls the game state
import pygame
from checkers import *  #imports everything from the checkers folder, reads from .\checkers\__init__.py


FPS = 60    #user-side variable, thus not defined in constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #Create the display environment
pygame.display.set_caption('Checkers')  #Caption for the game window


#event to run the game
def main():
    run = True
    
    #Creates the games timesense
    clock = pygame.time.Clock()
    
    
    while run:  #while run == true
        clock.tick(FPS) #starts the games time
        board = Board() #initializes/creates the board enviornment
        
        for event in pygame.event.get(): #checks to see if any events in pygame are happening, such as a click, and if so, run the loop
            if event.type == pygame.QUIT:   #if user clicks the red X, game will close
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
        board.draw_squares(WIN) #draws and updates the window after every event
        pygame.display.update()
    
    #if run == false and the loop breaks, the game ends 
    pygame.quit()
    
    
main()
