import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/mummy.png')
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 1 + random.randint(0, 2)

    def rotate_monster_s(self):
        self.velocity = 1 + random.randint(0, 2)
        self.image = pygame.image.load('assets/mummy.png')

    def rotate_monster_f(self):
        self.velocity -= 1 + random.randint(0, 2)
        self.image = pygame.image.load('assets/mummy_rotate.png')

    def damage(self, amout):
        self.health -= amout
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health

    def update_health_bar(self, surface):
        if self.health >= 75:
            bar_color = (111, 210, 46)
        elif self.health >= 25:
            bar_color = (255, 165, 0)
        else:
            bar_color = (255, 0, 0)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 10, self.rect.y - 15, self.health, 5]
        back_bar_position = [self.rect.x + 10, self.rect.y - 15, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
