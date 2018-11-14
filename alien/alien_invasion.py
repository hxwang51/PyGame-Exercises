import pygame
import sys
import game_functions as gf
from ship import Ship
from settings import Settings
from pygame.sprite import Group


def run_game():
    ai_settings=Settings()
    pygame.init()
    screen_size=ai_settings.screen_width, ai_settings.screen_height
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")
    bullets = Group()
    ship = Ship(ai_settings, screen)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()