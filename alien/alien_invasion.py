import pygame
import game_functions as gf
from ship import Ship
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats


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
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()