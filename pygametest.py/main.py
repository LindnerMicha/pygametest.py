import pygame
# !! Pygame initalisieren, muss immer gemacht werden
pygame.init()

#Bildfläche definieren
screen = pygame.display.set_mode((800, 600))                                    # () - einfügen -> darin Bildfläche erstellen
background = pygame.image.load("graphics/galaxie.jpg").convert_alpha()          # .convert_alpha() -> besserer Performance
score_tile = pygame.Surface((800,50))

#Titel & Icon
pygame.display.set_caption("Spaceinvador")                                      # Titel des Fensters festlegen
icon = pygame.image.load("graphics/ufo.png").convert_alpha()                    # Icon für das fenster festlegen
pygame.display.set_icon(icon)

#Clock                                                                          # Clock für die Framerate festlegen
clock = pygame.time.Clock()

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

def player(playerImg,playerX,playerY):
    screen.blit(playerImg, (playerX, playerY))                                  # .blit = synonüm für drawing
def endboss(endbossImg,endbossY, endbossX):
    screen.blit(endbossImg, (endbossY, endbossX))

#gameloop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                                                     # fenster schließen

    #screen.fill((255,255,255))                                                 # Hintergrundfarbe festlegen
    screen.blit(background,(0,0))                                               # Background textur draw
    screen.blit(score_tile, (0,550))                                        # Score Tile draw

    #Movement Endboss

    endboss(endbossImg,endbossY, endbossX)                                  # Endboss draw


    player(playerImg,playerX,playerY)                                       # Player draw

    screen.blit(score, (20, 555))

    pygame.display.update()                                                 # Bildschirm mit änderungen updaten -> nach jeden Gameloop durchlauf
    clock.tick(60)                                                          # legt die maximale Framerate auf 60 FPS fest -> while loop wird max 60 mal pro sekunde wiederholt