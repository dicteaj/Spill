import pygame # trenger for å få tilgang til pygame bibloteket

# initierer pygame
pygame.init()

# lager skjermen
screen = pygame.display.set_mode((600,700)) # bredde 800 høyde 600

# tittel og ikon
pygame.display.set_caption("Magic Girl")
icon = pygame.image.load('/Users/dicte/PycharmProjects/pygame/heart.png')
pygame.display.set_icon(icon)

# spiller
playerImg = pygame.image.load('/Users/dicte/PycharmProjects/pygame/standing.png')
playerX = 270 # x kordinatene til hvor spillern starter
playerY = 600 # y kordinatene til hvor spillern starter
playerX_change = 0

vel = 5

isJump = False
jumpCount = 10

#funksjon
def player(x,y):
    screen.blit(playerImg, (x, y))  # blit = draw

# game loop
running = True
while running:

    # RGB - rød, grønn, blå
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hvis man trykker på x knappen
            running = False           # avslutter spillet

        keys = pygame.key.get_pressed()  # sånn at spilleren kan gå opp ned til sidene

        if keys[pygame.K_LEFT] and playerX > vel:
            playerX -= vel
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and playerX  < 500 - vel - width:
            playerX += vel
            left = False
            right = True

        else:  # hvis karakteren ikke går frem eller bakover blir walkcount 0 igjen.
            left = False
            right = False
            walkCount = 0

        if not (isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0

        else:
            if jumpCount >= -10:
                playerY -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False

        # hvis knapp presses sjekk om det er høyre/venstre
    """    if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8  # antall piksler som fjernes
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8 # antall piksler som legges på

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
"""



    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update() # må oppdateres for å funke