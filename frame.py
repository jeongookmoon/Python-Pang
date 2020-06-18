import pygame
import random

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

# Enemy setup
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 5

# Amounts the character moves
to_x = 0
character_speed = .6

# Font setup
game_font = pygame.font.Font(None, 40)

# Game time
total_time = 60
start_ticks = pygame.time.get_ticks()

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

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # Left and right limit
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Enemy position reset
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # Get character and enemy's rectangle info (top, left, width, height)
    # So update top and left info
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Handle collision
    if character_rect.colliderect(enemy_rect):
        print("Collided")
        running = false

    # Update Character's position
    character_x_pos += to_x * frame

    # Update Enemy's position
    enemy_y_pos += enemy_speed

    # Clock
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    
    # Draw elements on the screen
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("Time out")
        running = False

    # Update display
    pygame.display.update()

pygame.time.delay(2000)

# Exit the game
pygame.quit()