# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

import pygame

# !! Pygame initalisieren, muss immer gemacht werden
pygame.init()

#Bildfläche definieren
screen = pygame.display.set_mode((800, 600))                                    # () - einfügen -> darin Bildfläche erstellen
background = pygame.image.load("graphics/galaxie.jpg").convert_alpha()          # .convert_alpha() -> besserer Performance
score_tile = pygame.Surface((800, 50))

#Titel & Icon
pygame.display.set_caption("Spaceinvador")                                      # Titel des Fensters festlegen
icon = pygame.image.load("graphics/ufo.png").convert_alpha()                    # Icon für das fenster festlegen
pygame.display.set_icon(icon)

#Clock                                                                          # Clock für die Framerate festlegen
clock = pygame.time.Clock()
fps = 60


# Fonts
test_font = pygame.font.Font("fonts/PixeloidSans.ttf", 30)                      # Eine Font erstellen -> (Font, größe)

#Score
score_val = 0
score = test_font.render(f"Score:  {score_val}", False, "White")                # rendern von Schriften -> ("Was möchte ich rendern", Antialiasing(Kantensmoothnes), Color)

#Player
playerImg = pygame.image.load("graphics/raumschiff.png").convert_alpha()
playerX = 370
playerY = 480

#Endboss
endbossImg = pygame.image.load("graphics/monster.png").convert_alpha()
endbossX = 40
endbossY = 370

# Bullet init / surface
kugel = pygame.image.load("graphics/kugel.png")
kugelX = 0
kugelY = 0
kugelYbewegung = 6
kugelstatus = False

boss_speed = 2



def player(playerImg, playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))                                  # .blit = synonüm für drawing
def endboss(endbossImg, endbossY, endbossX):
    screen.blit(endbossImg, (endbossY, endbossX))
def kugelfliegt(x, y):
    screen.blit(kugel, (x, y))
def kollisionskontrolle(kugelX, kugelY, endbossX, endbossY):
    if :
        return True
    else:
        return False


#gameloop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                                                     # fenster schließen

    #screen.fill((255,255,255))                                                 # Hintergrundfarbe festlegen
    screen.blit(background, (0, 0))                                               # Background textur draw
    screen.blit(score_tile, (0, 550))                                            # Score Tile draw

    #Movement Endboss
    endbossY += boss_speed
    if endbossY < 30:
        boss_speed *= -1

    if endbossY > 700:
        boss_speed *= -1
    endboss(endbossImg, endbossY, endbossX)                                  # Endboss draw

    #Player Movement
    keys = pygame.key.get_pressed()
    playerX += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    playerY += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    if playerY <= 200:
        playerY = 200
    elif playerY >= 480:
        playerY = 480

    if playerX <= 10:
        playerX = 10
    elif playerX >= 730:
        playerX = 730

    #Player Shooting   ->   https://www.python-lernen.de/invaders-game-python-gegner-abschiessen.htm / https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame


    # Spielfeld/figuren zeichnen

    player(playerImg, playerX, playerY)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:                                # auf druck der Leertaste warten
        if not kugelstatus:                            # wenn kugel nichtmehr sichtbar ist wird der nächste Schuss freigegeben
            kugelstatus = True
            kugelX = playerX                                # kugel die Schiffkoordinaten geben
            kugelY = playerY + 50


    if kugelstatus:
        kugelY -= kugelYbewegung
        if kugelY <= 0:
            kugelstatus = False

    if kugelstatus:
        kugelfliegt(kugelX, kugelY)


    kollisionskontrolle(kugelX, kugelY, endbossX, endbossY)
    screen.blit(score, (20, 555))

    pygame.display.update()                                                 # Bildschirm mit änderungen updaten -> nach jeden Gameloop durchlauf
    clock.tick(fps)                                                         # legt die maximale Framerate auf 60 FPS fest -> while loop wird max 60 mal pro sekunde wiederholt