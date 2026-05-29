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
schip_breedte = 30
schip_hoogte = 50
schip_x = breedte // 2 - schip_breedte // 2
schip_y = hoogte - 60
schip_snelheid = 0.12

#dit tekent de schip op het scherm
def teken_schip(x, y):
    pygame.draw.rect(scherm, groen, (x, y, schip_breedte, schip_hoogte))

# de loop voor het spel
draait = True
while draait:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draait = False
    
    # toetsen checken of er beweging plaats vindt
    toetsen = pygame.key.get_pressed()
    if toetsen[pygame.K_LEFT] and schip_x > 0:
        schip_x -= schip_snelheid
    if toetsen[pygame.K_RIGHT] and schip_x < breedte - schip_breedte:
        schip_x += schip_snelheid
    if toetsen[pygame.K_UP] and schip_y > 0:
        schip_y -= schip_snelheid
    if toetsen[pygame.K_DOWN] and schip_y < hoogte - schip_hoogte:
        schip_y += schip_snelheid

    scherm.fill(zwart)
    teken_schip(schip_x, schip_y)
    
    pygame.display.flip()

pygame.quit()