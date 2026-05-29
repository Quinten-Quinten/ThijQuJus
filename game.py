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
geel = (255, 255, 0)
rood = (255, 0, 0)

# speler
schip_breedte = 30
schip_hoogte = 50
schip_x = breedte // 2 - schip_breedte // 2
schip_y = hoogte - 60
schip_snelheid = 0.12

#kogels
kogels = []
kogel_snelheid = 0.2

#aliens
aliens = []
alien_breedte = 40
alien_hoogte = 30

for rij in range(3):
    for kolom in range(8):
        x = kolom * 60 + 50
        y = rij * 50 + 50
        aliens.append([x, y])

#dit tekent de schip op het scherm
def teken_schip(x, y):
    pygame.draw.rect(scherm, groen, (x, y, schip_breedte, schip_hoogte))

#tekent de kogels op het scherm
def teken_kogels():
    for kogel in kogels:
        pygame.draw.rect(scherm, rood, (kogel[0], kogel[1], 5, 15))

#tekent de aliens op het scherm
def teken_aliens():
    for alien in aliens:
        pygame.draw.rect(scherm, geel, (alien[0], alien[1], alien_breedte, alien_hoogte))

# de loop voor het spel
draait = True
while draait:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draait = False
        # checkt of er een toets is ingedrukt
        if event.type == pygame.KEYDOWN:
            # als de spatiebalk wordt ingedrukt, wordt er een kogel gemaakt
            if event.key == pygame.K_SPACE:
                #maakt de kogel boven het schip
                kogels.append([schip_x + schip_breedte // 2, schip_y])
    
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
    
    # dit beweegt de kogels omhoog
    for kogel in kogels[:]:
        kogel[1] -= kogel_snelheid
        # verwijder kogels die van het scherm zijn
        if kogel[1] < 0:
            kogels.remove(kogel)


    scherm.fill(zwart)
    teken_schip(schip_x, schip_y)
    teken_kogels()
    teken_aliens()
    
    pygame.display.flip()

pygame.quit()