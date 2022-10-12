# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

import pygame

# !! Pygame initalisieren, muss immer gemacht werden
pygame.init()

#Bildfläche definieren
screen = pygame.display.set_mode((800, 600))                                    # () - einfügen -> darin Bildfläche erstellen
background = pygame.image.load("graphics/galaxie.jpg").convert_alpha()          # .convert_alpha() -> besserer Performance


#Titel & Icon
pygame.display.set_caption("Spaceinvador")                                      # Titel des Fensters festlegen
icon = pygame.image.load("graphics/ufo.png").convert_alpha()                    # Icon für das fenster festlegen
pygame.display.set_icon(icon)

#Clock                                                                          # Clock für die Framerate festlegen
clock = pygame.time.Clock()
fps = 60
edurations = 0
delay_sec = 3

# Fonts
test_font = pygame.font.Font("fonts/PixeloidSans.ttf", 30)                      # Eine Font erstellen -> (Font, größe)

#Score
score_tile = pygame.Surface((800, 50))
score_val = 0
score = test_font.render(f"Score:  {score_val}", False, "White")                # rendern von Schriften -> ("Was möchte ich rendern", Antialiasing(Kantensmoothnes), Color)
score_count = score_val
level_val = 1
level = test_font.render(f"Level:  {level_val}", False, "White")

#Player
playerImg = pygame.image.load("graphics/raumschiff.png").convert_alpha()
playerX = 370
playerY = 480

# Bullet init / surface
kugel = pygame.image.load("graphics/kugel.png").convert_alpha()
kugelX = 0
kugelY = 0
kugelYbewegung = 6
kugelstatus = False

#Explosion Bullet
explosionImg = pygame.image.load("graphics/explosion.png").convert_alpha()
exploX = 0
exploY = 0

#Leben
leben_val = 8

#Endboss
endbossImg = pygame.image.load("graphics/monster.png").convert_alpha()
endbossX = 40
endbossY = 370

# Meteor
meteor = pygame.image.load("graphics/meteorit_gross.png").convert_alpha()
meteorX = 0
meteorY = 0
meteorYbewegung = 2
meteorstatus = False


boss_speed = 2

def player(playerImg, playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))                                  # .blit = synonüm für drawing
def endboss(endbossImg, endbossY, endbossX):
    screen.blit(endbossImg, (endbossY, endbossX))
def kugelfliegt(y, x):
    screen.blit(kugel, (y, x))
def meteorfliegt(meteorY, meteorX):
    screen.blit(meteor, (meteorY, meteorX))
def kollisionskontrolle_boss(kugelX, kugelY, endbossX, endbossY):
    if (kugelX >= endbossY-20 and kugelX <= endbossY + 40) and (kugelY >= endbossX-40 and kugelY <= endbossX + 30):
        return True
    else:
        return False
def kollisionskontrolle_player(meteorX, meteorY, playerX, playerY):
    if (meteorX >= playerX-20 and meteorX <= playerX + 40) and (meteorY >= playerY-40 and meteorY <= playerY + 30):
        return True
    else:
        return False
def lifebar(leben_val):
    if leben_val == 8:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [320, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [340, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [360, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [380, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [400, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [420, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [440, 555, 15, 40], 0)
    if leben_val == 7:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [320, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [340, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [360, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [380, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [400, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [420, 555, 15, 40], 0)
    if leben_val == 6:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [320, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [340, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [360, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [380, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [400, 555, 15, 40], 0)
    if leben_val == 5:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [320, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [340, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [360, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [380, 555, 15, 40], 0)
    if leben_val == 4:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [320, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [340, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [360, 555, 15, 40], 0)
    if leben_val == 3:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [320, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [340, 555, 15, 40], 0)
    if leben_val == 2:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0),
        pygame.draw.rect(screen, "Green", [320, 555, 15, 40], 0)
    if leben_val == 1:
        pygame.draw.rect(screen, "Green", [300, 555, 15, 40], 0)

    if leben_val > 0:
        return True
    else:
        return False
def delay(edurations, delay_sec):
    sec = delay_sec * 60
    ed_count = edurations
    if ed_count > sec:
        return True
    else:
        return False






bullet_surf = pygame.Surface((10, 10), pygame.SRCALPHA)
pygame.draw.circle(bullet_surf, (64, 64, 62), bullet_surf.get_rect().center, bullet_surf.get_width() // 2)
bullet_list = []


tank_surf = pygame.Surface((800, 600), pygame.SRCALPHA)
tank_rect = tank_surf.get_rect(top=(playerX, playerY))







#gameloop
running = True
while running:

    tank_surf = pygame.Surface((playerX, playerY), pygame.SRCALPHA)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    if keys[pygame.K_SPACE]:
        bullet_list.insert(0, tank_rect.top)

    screen.blit(background, (0, 0))




    current_time = pygame.time.get_ticks()

    for i, bullet_pos in enumerate(bullet_list):
        bullet_list[i] = bullet_pos[0] + 5, bullet_pos[1]
        if bullet_surf.get_rect(center = bullet_pos).left > screen.get_width():
            del bullet_list[i:]
            break

    for bullet_pos in bullet_list:
        screen.blit(bullet_surf, bullet_surf.get_rect(center = bullet_pos))









    #Movement Endboss
    endbossY += boss_speed
    if endbossY < 30:
        boss_speed *= -1

    if endbossY > 700:
        boss_speed *= -1
    endboss(endbossImg, endbossY, endbossX)

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
    player(playerImg, playerX, playerY)


    if keys[pygame.K_SPACE]:                                # auf druck der Leertaste warten
        if not kugelstatus:                                 # wenn kugel nichtmehr sichtbar ist wird der nächste Schuss freigegeben
            kugelstatus = True
            kugelX = playerX                                # kugel die Schiffkoordinaten geben
            kugelY = playerY + 50


    if kugelstatus:
        kugelY -= kugelYbewegung
        if kugelY <= 0:
            kugelstatus = False

    if kugelstatus:
        kugelfliegt(kugelX, kugelY)

    # Bossgeschwindigkeit erhöhen
    if score_count + 10 == score_val:
        score_count = score_val
        level_val += 1
        if boss_speed > 0:
            boss_speed += 0.5
        elif boss_speed < 0:
            boss_speed -= 0.5

    # Timer
    if delay(edurations, delay_sec):
        if not meteorstatus:
            meteorstatus = True
            meteorX = endbossY
            meteorY = endbossX + 50
            edurations = 0

    if meteorstatus:
        meteorY += meteorYbewegung
        if meteorY >= 550:
            meteorstatus = False

    if meteorstatus:
        meteorfliegt(meteorX, meteorY)

    # Score
    kollisionskontrolle_boss(kugelX, kugelY, endbossX, endbossY)
    kollisionskontrolle_player(meteorX, meteorY, playerX, playerY)

    if kollisionskontrolle_boss(kugelX, kugelY, endbossX, endbossY) and kugelstatus:
        score_val += 1
        kugelstatus = False
        screen.blit(explosionImg, (kugelX, kugelY))
    if kollisionskontrolle_player(meteorX, meteorY, playerX, playerY) and meteorstatus:
        leben_val -= 1
        meteorstatus = False
        screen.blit(explosionImg, (meteorX, meteorY))


    screen.blit(score_tile, (0, 550))                                       # Score Tile draw
    score = test_font.render(f"Score:  {score_val}", False, "White")        # Update des scores
    screen.blit(score, (20, 555))
    level = test_font.render(f"Level:  {level_val}", False, "White")        # Update level
    screen.blit(level, (600, 555))
    lifebar(leben_val)



    pygame.display.update()                                                 # Bildschirm mit änderungen updaten -> nach jeden Gameloop durchlauf
    edurations += 1
    clock.tick(fps)                                                         # legt die maximale Framerate auf 60 FPS fest -> while loop wird max 60 mal pro sekunde wiederholt