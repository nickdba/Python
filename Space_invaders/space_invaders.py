import json
import pygame

def player(x, y):
    screen.blit(playerImg, (x, y))

# Read the config.json 
def get_configuration():
    with open('config.json') as file:
        conf = json.load(file)
    return conf        

# Initialize the pygame
pygame.init()

# Create the screen
conf = get_configuration()
print(conf['window']['width'])
win_width = int(conf['window']['width'])
win_height = int(conf['window']['height'])
screen = pygame.display.set_mode((win_width, win_height))

# Caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Resources/si_icon.png")
pygame.display.set_icon(icon)

# Player image
playerImg = pygame.image.load("Resources/si_player.png")
playerX = win_width/2
playerY = win_height*5/6
movement = 0

# Game Loop
running = True
while running:
    
    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = -0.3
            if event.key == pygame.K_RIGHT:
                movement = 0.3
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement = 0    

    # Limits and movement increment
    if playerX < 0:
        playerX = 0
    elif playerX > win_width - (64/2):
        playerX = win_width - (64/2)
    else:
        playerX += movement

    screen.fill((0,0,0))
    player(playerX, playerY)
    pygame.display.update()
