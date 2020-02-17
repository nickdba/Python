import pygame

class Entity:
    def __init__(self, x, y):
        self.playerImg = pygame.image.load("Resources/si_player.png")
        self.movement = 0
        self.x = x
        self.y = y
        
    # Draw player    
    def draw (self, screen, x,y):
        screen.blit(self.playerImg, (x, y))

    # Print entity
    def print_ent(self):
        print("test reusit")
