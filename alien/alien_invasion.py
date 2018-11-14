import pygame
import game_functions as gf
from ship import Ship
from settings import Settings
from pygame.sprite import Group
from alien import Alien


def run_game():
    ai_settings=Settings()
    pygame.init()
    screen_size=ai_settings.screen_width, ai_settings.screen_height
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")
    bullets = Group()
    ship = Ship(ai_settings, screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()