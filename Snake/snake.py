import math
import random
import pygame

# class snake(object)
#     pass

def redrawWindow(win, width, height, scale_factor):
    
    win.fill((0,0,0))

    # Draw Matrix
    for y in range (1,width/scale_factor):
        for x in range(1,height/scale_factor):
            pygame.draw.line(win, (256,256,256), (x,1), (x, width), width=1)
        pygame.draw.line(win, (256,256,256), (1,y), (height, y), width=1)

    pygame.display.update()

def setTitleAndIcon():
    pygame.display.set_caption("Snake")
    icon = pygame.image.load("Imgs/snake.png")
    pygame.display.set_icon(icon)

def main ():
    width = 600
    height = 500
    scale_factor = 10
    
    # Initialize pygame
    pygame.init()

    # Draw the main window
    win = pygame.display.set_mode((width, height))

    # Set title and icon
    setTitleAndIcon()

    # Main loop
    running = True
    while running:

        # Checking for the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.delay(50)

        redrawWindow(win, width, height, scale_factor)

main()
   