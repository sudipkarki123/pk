import math
import random
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
PLAYER_Y = 380
ENEMY_COUNT = 6
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set-mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("Space Invaders"))

background = pygame.image.load("background.png")
bullet = pygame.image.load("bullet.png")
enemy = pygame.image.load("enemy.png")
icon = pygame.image.load("icon.png")
player = pygame.image.load("player.png")

font = pygame.font.Font('freesansbold.ttf',32)
over_font = pygame.font.Font('freesansbold.ttf',64)

player_x = 370
player_x_change = 0
bullet_x = 0
bullet_y = PLAYER_Y
bullet_state = "ready"
score = 0

enemies = [{
    "x": random.randint(0, SCREEN_WIDTH - 64)
    "y": random.randint(50, 150),
    "x_change": 2,
    "y_change": 20,
} for i in range(ENEMY_COUNT)]

def show_score(x, y):
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_display, (x, y))

def draw_player(x, y):
    screen.blit(player_image, (x, y))

def draw_enemy(enemy):
    screen.blit(enemy_image, (enemy["x"], enemy["y"]))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

def is_collision(ex, ey, bx, by):
    return math.hypot(ex - bx, ey - by) < COLLISION_DISTANCE

def show_score(x, y):
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

