import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width =input("Enter width")
window_height = input("Enter height")
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Floor Plan")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Set dimensions of the floor plan
floor_width = 600
floor_height = 400

# Set dimensions and position of a room
room_width = 200
room_height = 150
room_x = 200
room_y = 100

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(WHITE)

    # Draw the floor plan
    pygame.draw.rect(window, BLACK, (0, 0, floor_width, floor_height), 2)

    # Draw a room
    pygame.draw.rect(window, GRAY, (room_x, room_y, room_width, room_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
