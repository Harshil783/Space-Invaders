import os
import time
import random
import pygame
pygame.font.init()

# Main window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader tutorial")

# loading images
RED_SPACE_SHIP = pygame.image.load(
    os.path.join("assets/", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(
    os.path.join("assets/", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(
    os.path.join("assets/", "pixel_ship_green_small.png"))

# player ship
YELLOW_SPACE_SHIP = pygame.image.load(
    os.path.join("assets/", "pixel_ship_yellow.png"))

# loading lasers
RED_LASER = pygame.image.load(os.path.join("assets/", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets/", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets/", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets/", "pixel_laser_yellow.png"))

# Background images
BG = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/", "background-black.png")), (WIDTH, HEIGHT))


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):

    COLOR_MAP = {
        "red" : (RED_SPACE_SHIP, RED_LASER),
        "blue" : (BLUE_SPACE_SHIP, BLUE_LASER),
        "green" : (GREEN_SPACE_SHIP, GREEN_LASER)
    }

    def __init__(self, x, y, color, health=100): # "red", "green", "blue"
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, vel):
        self.y += vel