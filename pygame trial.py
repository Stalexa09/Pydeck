import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smooth Cursor Following")

# Square properties
square_size = 50
square_color = RED
square_x = 100
square_y = 100
base_speed = 5  # Initial speed of the square
speed_increase_rate = 0.5  # Speed increase per second

# Time tracking for speed increase
start_time = time.time()

# Main game loop
running = True
while running:
    screen.fill(BLACK)  # Fill the screen with white

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the mouse is within the window bounds
    if 0 <= mouse_x < screen_width and 0 <= mouse_y < screen_height:
        # Calculate the target position (center the square on the mouse)
        target_x = mouse_x - square_size // 2
        target_y = mouse_y - square_size // 2

        # Calculate distance to the target
        distance_x = target_x - square_x
        distance_y = target_y - square_y
        distance = (distance_x**2 + distance_y**2) ** 0.5

        # Move the square towards the target
        if distance > base_speed:
            square_x += base_speed * (distance_x / distance)
            square_y += base_speed * (distance_y / distance)
        else:
            square_x = target_x
            square_y = target_y

        # Check if the square has reached the cursor
        if distance <= base_speed:
            print("Game Over!")
            running = False

    # Increase speed over time
    current_time = time.time()
    elapsed_time = current_time - start_time
    base_speed = 5 + speed_increase_rate * elapsed_time  # Gradually increase speed

    # Prevent the square from moving out of bounds
    if square_x < 0:
        square_x = 0
    elif square_x > screen_width - square_size:
        square_x = screen_width - square_size

    if square_y < 0:
        square_y = 0
    elif square_y > screen_height - square_size:
        square_y = screen_height - square_size

    # Draw the square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()
    pygame.time.delay(10)  # Delay to control speed of the game loop

# Quit Pygame
pygame.quit()
sys.exit()
