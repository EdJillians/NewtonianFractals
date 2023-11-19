# Simple pygame program

# Import and initialize the pygame library
import pygame

from calc import generate_newton_fractal

pygame.init()

colours = (
    (46, 97, 113),
    (85, 111, 122),
    (121, 128, 134),
    (183, 159, 173),
    (212, 175, 205),
)

n = 500

# Generate the fractal matrix:
print("Generating fractal...")
fractal = generate_newton_fractal(n=n)

print("Fractal generated.")

# Set up the drawing window
screen = pygame.display.set_mode([n, n])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for x in range(n):
        for y in range(n):
            color = colours[round(fractal[x, y]) % len(colours)]
            screen.set_at((x, y), color)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()