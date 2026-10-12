# Simple pygame program

# Import and initialize the pygame library
import pygame

from calc import generate_newton_fractal

pygame.init()

# Alternative palette option:
# colours = (
#     (46, 97, 113),
#     (85, 111, 122),
#     (121, 128, 134),
#     (183, 159, 173),
#     (212, 175, 205),
# )

colours = (
    (0, 135, 108),
    (87, 161, 139),
    (140, 188, 172),
    (190, 214, 206),
    (211, 211, 211),
    (241, 198, 198),
    (236, 156, 157),
    (226, 112, 118),
    (212, 61, 81)
)

n = 600

# Generate the fractal matrix:
print("Generating fractal...")
fractal = generate_newton_fractal(n=n)
print("Fractal generated.")

# Set up the drawing window
screen = pygame.display.set_mode([n, n])
pygame.display.set_caption("Newton Fractal")

# Draw the fractal once onto the screen
screen.fill((255, 255, 255))
for x in range(n):
    for y in range(n):
        color = colours[round(fractal[x, y]) % len(colours)]
        screen.set_at((x, y), color)

pygame.display.flip()
pygame.image.save(screen, "fractal.png")
print("Saved image to fractal.png")

# Run event loop until the user asks to quit
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(30)

pygame.quit()


