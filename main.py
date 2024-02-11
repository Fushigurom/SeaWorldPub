import pygame
import math
import schedule

import projectiles
from projectiles import Projectile
from game import Game
from player import Player

pygame.init()

# Genere la fenetre du jeu
pygame.display.set_caption("SeaWorld")
screen = pygame.display.set_mode((1080, 720))

# Arriere plan de la fenetre
background = pygame.image.load('assets/bg.jpg')

banner = pygame.image.load('assets/logo seaworld.png')
banner = pygame.transform.scale(banner, (750, 750))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 7)
banner_rect.y = -50

play_button = pygame.image.load('assets/butoon play.png')
play_button = pygame.transform.scale(play_button, (1250, 1250))
button_rect = play_button.get_rect()
button_rect.x = -20
button_rect.y = -125

# Charger le jeu
game = Game()

# Charger le joueur
player = Player(game)

clock = pygame.time.Clock()

running = True

schedule.every(2).seconds.do(player.mana_regen)

# Boucle pour maintenir la fenetre ouverte
while running:
    schedule.run_pending()
    clock.tick(60)
    # Application de l'arriere plan
    screen.blit(background, (0, -200))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, button_rect)
        screen.blit(banner, banner_rect)

    # Mettre à jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Touche espace enclenche ?
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile_right()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game.is_playing = True
