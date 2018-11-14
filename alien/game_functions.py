import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    for alien in aliens.sprites():
        alien.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings, screen):
    alien=Alien(ai_settings, screen)
    available_space_x = ai_settings.screen_width - alien.rect.width*2
    number_aliens_x = int(available_space_x / (alien.rect.width*2))
    return number_aliens_x

def get_number_rows(ai_settings, screen, ship):
    alien=Alien(ai_settings, screen)
    available_space_y = ai_settings.screen_height - alien.rect.height*2 - ship.rect.height
    number_rows = int(available_space_y/(2*alien.rect.height))
    return number_rows

def create_fleet(ai_settings, screen, ship, aliens):
    number_aliens_x = get_number_aliens_x(ai_settings, screen)
    for row in range(get_number_rows(ai_settings,screen, ship)):
        for alien_index in range(number_aliens_x):
            alien = Alien(ai_settings, screen)
            alien.rect.x = alien.rect.width + alien.rect.width*2*alien_index
            alien.rect.y = alien.rect.height + alien.rect.height*2*row
            aliens.add(alien)
