import pygame

from player import Player
from monster import Monster


class Game:

    def __init__(self):
        # genere notre joueur
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu a neuf
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.mana = self.player.max_mana
        self.is_playing = False

    def update(self, screen):
        # appliquer le joueur sur l'ecran
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.player.update_mana_bar(screen)

        # recuperer les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            if monster.rect.x < 0:
                monster.rotate_monster_f()
            elif monster.rect.x > 950:
                monster.rotate_monster_s()
            monster.forward()
            monster.update_health_bar(screen)

        # applique l'image du projectile
        self.player.all_projectiles.draw(screen)

        self.all_monsters.draw(screen)

        # droite ou gauche + bordure
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 720:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 500:
            self.player.move_down()

    # deuxieme classe pour le jeu
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)


