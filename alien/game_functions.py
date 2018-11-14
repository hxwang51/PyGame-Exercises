import sys
import pygame
from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_event_keydown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets )

def check_event_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key == pygame.K_LEFT:
        ship.moving_left=False

def check_events(ai_settings, screen, ship ,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_event_keyup(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)
