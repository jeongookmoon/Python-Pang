import pygame

# Initialize
pygame.init() 

# Screen size setup
screen_width=480
screen_height=640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title setup
pygame.display.set_caption("Python Pang")

# FPS
clock = pygame.time.Clock()

# Background setup
background = pygame.image.load("background.png")

# Character setup
character = pygame.image.load("player.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - character_width/2
character_y_pos = screen_height - character_height

# Amounts the character moves
to_x = 0
to_y = 0

character_speed = .6

# Event Loop
running = True # Is the game running?
while running:
    frame = clock.tick(60)

    # for each event during game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user clicks QUIT button
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # Left and right limit
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # Left and right limit
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    character_x_pos += to_x * frame
    character_y_pos += to_y * frame

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# Exit the game
pygame.quit()