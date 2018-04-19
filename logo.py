# ICS3U
# Assignment 2: Logo
# <Shaan>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
import math
pygame.init()
Font = pygame.font.SysFont('magnificent', 80)

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LGREEN = (86, 219, 74)
# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shanns Logo")


text = Font.render('Spotify',1,(WHITE))
screen.blit(text, (90, 295))

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLACK)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, LGREEN, [50,50, 300, 300], 0) #Main green circle
    pygame.draw.ellipse(screen, WHITE, [100,140, 25, 25], 0) #White circle on the left or the top arc
    pygame.draw.ellipse(screen, WHITE, [276,143, 25, 25], 0) #White circle on the right or the top arc
    pygame.draw.ellipse(screen, WHITE, [110,180, 20, 20], 0) #White circle on the left or the middle arc
    pygame.draw.ellipse(screen, WHITE, [270,180, 20, 20], 0) #White circle on the right or the middle arc
    pygame.draw.ellipse(screen, WHITE, [120,220, 16, 16], 0) #White circle on the left or the bottom arc
    pygame.draw.ellipse(screen, WHITE, [260,218, 16, 16], 0) #White circle on the right or the bottom arc
    pygame.draw.arc(screen, WHITE, [100, 120, 200, 80], math.radians(0), math.radians(173), 25) #Top/largest arc
    pygame.draw.arc(screen, WHITE, [100, 165, 200, 80], math.radians(25), math.radians(153), 20) #Middle/second largest arc
    pygame.draw.arc(screen, WHITE, [100, 209, 200, 80], math.radians(43), math.radians(143), 15) #Bottom/smallest arc

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
