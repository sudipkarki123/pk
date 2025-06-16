import math
import random
import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
PLAYER_Y = 380
ENEMY_COUNT = 6
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(pygame.image.load('ufo.png'))

# Load Assets
background = pygame.image.load('background.png')
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')
bullet_img = pygame.image.load('bullet.png')

# Fonts
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Game Variables
player_x = 370
player_x_change = 0
bullet_x = 0
bullet_y = PLAYER_Y
bullet_state = "ready" 
score = 0

# Enemies
enemies = [{
    "x": random.randint(0, SCREEN_WIDTH - 64),
    "y": random.randint(50, 150),
    "x_change": 2,
    "y_change": 20
} for i in range(ENEMY_COUNT)]

# Functions
def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_enemy(enemy):
    screen.blit(enemy_img, (enemy["x"], enemy["y"]))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(ex, ey, bx, by):
    return math.hypot(ex - bx, ey - by) < COLLISION_DISTANCE

def show_score():
    score_text = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def show_game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Game Loop
running = True
while running:
    screen.blit(background, (0, 0))

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 5
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        elif event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_x_change = 0

    # Update Player
    player_x += player_x_change
    player_x = max(0, min(player_x, SCREEN_WIDTH - 64))
    # Update Enemies
    for enemy in enemies:
        if enemy["y"] > 340:
            for e in enemies:
                e["y"] = 2000
            show_game_over()
            break

        enemy["x"] += enemy["x_change"]
        if enemy["x"] <= 0 or enemy["x"] >= SCREEN_WIDTH - 64:
            enemy["x_change"] *= -1
            enemy["y"] += enemy["y_change"]
        # Collision
        if is_collision(enemy["x"], enemy["y"], bullet_x, bullet_y):
            bullet_y = PLAYER_Y
            bullet_state = "ready"
            score += 1
            enemy["x"] = random.randint(0, SCREEN_WIDTH - 64)
            enemy["y"] = random.randint(50, 150)

        draw_enemy(enemy)

    # Update Bullet
    if bullet_y <= 0:
        bullet_y = PLAYER_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= 10

    draw_player(player_x, PLAYER_Y)
    show_score()
    pygame.display.update()
