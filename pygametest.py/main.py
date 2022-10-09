import pygame

# !! Pygame initalisieren, muss immer gemacht werden
pygame.init()

#Bildfläche definieren
screen = pygame.display.set_mode((800, 600))       # () - einfügen -> darin Bildfläche erstellen

#Titel & Icon
pygame.display.set_caption("Pussyinvador")          # Titel des Fensters festlegen
icon = pygame.image.load("ufo.png")                 # Icon für das fenster festlegen
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("penis.png")
playerX = 370
playerY = 480

#Endboss
endbossImg = pygame.image.load("vagina.png")
endbossX = 40
endbossY = 370

def player():
    screen.blit(playerImg, (playerX, playerY))                             # .blit = synonüm für drawing
def endboss():
    screen.blit(endbossImg, (endbossY, endbossX))

running = True
#gameloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                                                 # fenster schließen

    screen.fill((255,255,255))                                              # Hintergrundfarbe festlegen

    endboss()
    player()                                                                # Player draw
    pygame.display.update()                                                 # Bildschirm mit änderungen updaten -> nach jeden Gameloop durchlauf