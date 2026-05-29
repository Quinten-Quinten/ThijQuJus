# Space Invaders
import pygame
# het spel opstarten
pygame.init()

# dit maakt het venster aan voor de game
breedte = 600
hoogte = 800
scherm = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("Space Invaders")

# kleuren
zwart = (0, 0, 0)
wit = (255, 255, 255)
groen = (0, 255, 0)

# speler
speler_breedte = 30
speler_hoogte = 50
speler_x = breedte // 2 - speler_breedte // 2
speler_y = hoogte - 60
speler_snelheid = 5

#dit tekent de spelere op het scherm
def teken_speler(x, y):
    pygame.draw.rect(scherm, groen, (x, y, speler_breedte, speler_hoogte))

# de loop voor het spel
draait = True
while draait:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draait = False
    
    scherm.fill(zwart)
    teken_speler(speler_x, speler_y)
    
    pygame.display.flip()

pygame.quit()