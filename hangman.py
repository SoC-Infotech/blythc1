import pygame
import random
#Initialize the pygame (game loop, game scene)
pygame.init()

#Declare some variables/constants
winHeight = 480
winWidth = 700
GREEN = (0,255,0)

#Create window game
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by Caleb Blythe")

#Main program


#Create a game loop to keep the window visible
inPlay = True
while inPlay:
    win.fill(GREEN) #Make background color green
    pygame.display.update()
    pygame.time.delay(100)


#Quit the pygame
pygame.quit()
