
import pygame
pygame.init()

#ikonet til spillet
icon = pygame.image.load("/Users/dicteaj/PycharmProjects/Spill/Bilder/heart.png")
pygame.display.set_icon(icon)

#navn til spillet
pygame.display.set_caption("Jansen minigame")

bredde = 500
høyde = 500
screen = pygame.display.set_mode([bredde, høyde])

running = True
while running:
 # fiks de andre quit greiene også
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) #hvit bakgrunn

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)  #bare en sikrel

    pygame.display.flip()

pygame.quit()