# Space Invaders
import pygame
# het spel opstarten
pygame.init()

# venster aanmaken
breedte = 600
hoogte = 800
scherm = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("Space Invaders")

# kleuren
zwart = (0, 0, 0)
wit = (255, 255, 255)

# spel loop
draait = True
while draait:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draait = False
    
    # achtergrond zwart maken
    scherm.fill(zwart)
    
    pygame.display.flip()

pygame.quit()