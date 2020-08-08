import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

#ikonet til spillet
icon = pygame.image.load("/Users/dicteaj/PycharmProjects/Spill/Bilder/L1.png")
pygame.display.set_icon(icon)

#laster bilder til spillet
walkRight = [pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R1.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R2.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R3.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R4.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R5.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R6.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R7.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R8.png'),
             pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R9.png')]
walkLeft = [pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L1.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/l2.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L3.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L4.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L5.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L6.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L7.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L8.png'),
            pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L9.png')]

#bakgrunn
bg = pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/bg.jpg').convert()
bgX = 0
bgX2 = bg.get_height()

char = pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/standing.png')

clock = pygame.time.Clock()

score = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60)


    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 20, self.y, 28, 60)
      #  pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit (self):
        self.isJump = False
        self.jumpCount = 10
        font1 = pygame.font.SysFont('comicsans', 100, True)
        text = font1.render('-5', 1, (255,0, 0))
        win.blit(text, (500/2 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

#FIENDE
class enemy(object):
    walkRight = [pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R1.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R2.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R3.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R4.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R5.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R6.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R7.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R8.png'),
                 pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/R9.png')]
    walkLeft = [pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L1.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/l2.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L3.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L4.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L5.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L6.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L7.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L8.png'),
                pygame.image.load('/Users/dicteaj/PycharmProjects/Spill/Bilder/L9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]  # This will define where our enemy starts and finishes their path.
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0],self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))
            self.hitbox = (self.x + 20, self.y, 28, 60)
         #   pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


def redrawGameWindow():
    win.blit(bg, (0, bgX))
    win.blit(bg, ( 0, bgX2))
    #win.blit(bg, (0, 0))
    text = font.render('score:' + str(score), 1, (0,0,0))
    win.blit(text, (350,10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)


    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = player(200, 410, 64, 64)
bullets = []
goblin = enemy(100, 410, 64, 64, 450)
shootloop = 0
run = True
speed = 30
while run:

    #PRØVER starrt
    clock.tick(speed)
    bgX -= 1.4
    bgX2 -= 1.4

    if bgX < bg.get_height() * -1:  #
        bgX = bg.get_height()

    if bgX2 < bg.get_height() * -1:
        bgX2 = bg.get_height()

    #PRØVER slutt

   # clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5

    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))  # FJERNE BULLET FRA INDEX

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) #FJERNE BULLET FRA INDEX

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootloop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()