
# pygame biblo
import pygame
# sto noe om det her men skjønte ikke heilt
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#start opp bibloteket
pygame.init()

# konstanter for skjermen
bredde = 500
høyde = 600
# Setter opp skjermen
screen = pygame.display.set_mode([bredde, høyde])

# spill til quit
running = True #variabel

#MAIN LOOP
while running:  #bure sette opp de andre også - gjør senere
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
  #  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # Flip the display
    #pygame.display.flip()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))

    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    # put sentrumet til surfacen i sentrumet til skjermen
    surf_center = (
        (bredde - surf.get_width()) / 2,
        (høyde - surf.get_height()) / 2
    )

    # "Draw surf onto the screen at the center"
    screen.blit(surf, surf_center)
    pygame.display.flip()

    # Done
pygame.quit()
