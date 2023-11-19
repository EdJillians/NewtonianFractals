# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

colours = (
    (46, 97, 113),
    (85, 111, 122),
    (121, 128, 134),
    (183, 159, 173),
    (212, 175, 205),
)

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for x in range(500):
        for y in range(500):
            color = colours[(round(x / 100) + round(y / 100)) % 5]
            screen.set_at((x, y), color)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()