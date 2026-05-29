# Space Invaders
import pygame
# het spel opstarten
pygame.init()

# dit maakt het venster aan voor de game
breedte = 600
hoogte = 800
scherm = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("Space Invaders")

game_over = False
game_state = "start"
score = 0
final_score = 0
final_wave = 0

# kleuren
zwart = (0, 0, 0)
wit = (255, 255, 255)
groen = (0, 255, 0)
geel = (255, 255, 0)
rood = (255, 0, 0)
wit = (255, 255, 255)

# speler
schip_breedte = 30
schip_hoogte = 50
schip_x = breedte // 2 - schip_breedte // 2
schip_y = hoogte - 60
schip_snelheid = 0.25
schip_grens_y = hoogte - 200

#kogels
kogels = []
kogel_snelheid = 0.6

#aliens
aliens = []
alien_breedte = 40
alien_hoogte = 30
alien_snelheid = 0.10
alien_daling = 20
alien_richting = 1  # de kant waar aliens heen gaan 1 voor rechts en -1 voor links

#waves
wave = 1
base_alien_snelheid = 0.1
base_alien_daling = 20

for rij in range(3):
    for kolom in range(8):
        x = kolom * 50 + 100
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

# deze functie checkt of er een kogel een alien raakt en als dat zo is worden zowel de kogel als de alien verwijderd
def check_collisie():
    global score
    for kogel in kogels[:]:
        for alien in aliens[:]:
            if (kogel[0] < alien[0] + alien_breedte and
                kogel[0] + 5 > alien[0] and
                kogel[1] < alien[1] + alien_hoogte and
                kogel[1] + 15 > alien[1]):
                kogels.remove(kogel)
                aliens.remove(alien)
                score += 10
                break

# deze functie reset het spel naar de beginwaarden zodat je opnieuw kan spelen
def reset_game():
    global schip_x, schip_y, kogels, aliens, game_over, alien_richting, wave, alien_snelheid, alien_daling, score

    schip_x = breedte // 2 - schip_breedte // 2
    schip_y = hoogte - 60

    kogels = []

    wave = 1
    alien_snelheid = base_alien_snelheid
    alien_daling = base_alien_daling

    score = 0

    aliens = []
    for rij in range(3):
        for kolom in range(8):
            x = kolom * 50 + 100
            y = rij * 50 + 50
            aliens.append([x, y])

    alien_richting = 1
    game_over = False

# deze functie spawnt een nieuwe wave aliens als alle aliens dood zijn
def spawn_aliens():
    aliens.clear()
    for rij in range(3):
        for kolom in range(8):
            x = kolom * 50 + 100
            y = rij * 50 + 50
            aliens.append([x, y])

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
            # als de R toets wordt ingedrukt, wordt het spel gereset
            if event.key == pygame.K_r and game_over:
                reset_game()
        if event.type == pygame.KEYDOWN:
            if game_state == "start":
                game_state = "playing"

    # als het spel nog niet is begonnen krijg je dit startscherm te zien
    if game_state == "start":
        scherm.fill(zwart)

        titel = pygame.font.SysFont("arial", 50).render("SPACE INVADERS", True, wit)
        knop = pygame.font.SysFont("arial", 30).render("Klik om te starten", True, groen)

        scherm.blit(titel, (breedte // 2 - 210, hoogte // 2 - 80))
        scherm.blit(knop, (breedte // 2 - 120, hoogte // 2))
    
        continue

    # toetsen checken of er beweging plaats vindt
    if not game_over:
        toetsen = pygame.key.get_pressed()
        if toetsen[pygame.K_LEFT] and schip_x > 0:
            schip_x -= schip_snelheid
        if toetsen[pygame.K_RIGHT] and schip_x < breedte - schip_breedte:
            schip_x += schip_snelheid
        if toetsen[pygame.K_UP] and schip_y > schip_grens_y:
            schip_y -= schip_snelheid
        if toetsen[pygame.K_DOWN] and schip_y < hoogte - schip_hoogte:
            schip_y += schip_snelheid

    #als geen aliens zijn spawnt er een nieuwe wave en worden de aliens met elke wave sneller
    if not game_over and len(aliens) == 0:
        wave += 1
        alien_snelheid = base_alien_snelheid + (wave * 0.03)
        alien_daling = base_alien_daling + (wave * 5)
        spawn_aliens()

    # dit beweegt de kogels omhoog
    if not game_over:
        for kogel in kogels[:]:
            kogel[1] -= kogel_snelheid
            # verwijder kogels die van het scherm zijn
            if kogel[1] < 0:
                kogels.remove(kogel)

    # beweeg de aliens
    if not game_over:
        rand_bereikt = False
        for alien in aliens:
            alien[0] += alien_snelheid * alien_richting
            # checkt of alien de rand van het scherm heeft bereikt
            if alien[0] <= 0 or alien[0] >= breedte - alien_breedte:
                rand_bereikt = True

    # als de alien de rand heeft bereikt verandert de richting en dalen ze naar beneden
    if not game_over:
        if rand_bereikt:
            alien_richting *= -1
            for alien in aliens:
                alien[1] += alien_daling

    check_collisie()

    # checkt of een alien het schip aanraakt als dat zo is is het game over
    for alien in aliens:
        if (alien[0] < schip_x + schip_breedte and
            alien[0] + alien_breedte > schip_x and
            alien[1] < schip_y + schip_hoogte and
            alien[1] + alien_hoogte > schip_y):
            game_over = True
            final_score = score
            final_wave = wave
        # als alien de onderkant van het scherm bereikt is het ook game over
        if alien[1] + alien_hoogte >= hoogte:
            game_over = True
            final_score = score
            final_wave = wave

    scherm.fill(zwart)
    if not game_over:
        teken_kogels()
        teken_aliens()
        score_text = pygame.font.SysFont("arial", 25).render("Score: " + str(score), True, wit)
        wave_text = pygame.font.SysFont("arial", 25).render("Wave: " + str(wave), True, wit)
        scherm.blit(score_text, (10, 10))
        scherm.blit(wave_text, (10, 40))

    if not game_over:
        teken_schip(schip_x, schip_y)

    # als het game over is krijg je tekst Game Over
    if game_over:
        tekst1 = pygame.font.SysFont("arial", 40).render("Game Over", True, wit)
        tekst2 = pygame.font.SysFont("arial", 25).render("Druk op R om opnieuw te spelen", True, wit)
        tekst3 = pygame.font.SysFont("arial", 25).render("Score: " + str(final_score), True, wit)
        tekst4 = pygame.font.SysFont("arial", 25).render("Wave: " + str(final_wave), True, wit)
        scherm.blit(tekst1, (breedte // 2 - 100, hoogte // 2))
        scherm.blit(tekst2, (breedte // 2 - 170, hoogte // 2 + 50))
        scherm.blit(tekst3, (10, 10))
        scherm.blit(tekst4, (10, 40))

    pygame.display.flip()

pygame.quit()