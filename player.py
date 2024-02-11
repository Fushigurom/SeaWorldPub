import pygame

from projectiles import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.mana = 80
        self.max_mana = 80
        self.mana_regen_rate = 15
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()  # Groupe de tous les projectiles lancés par le joueur
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amout):
        if self.health - amout > amout:
            self.health -= amout
        else:
            self.game.game_over()

    def mana_regen(self):
        print("e")
        if self.mana <= self.max_mana:
            self.mana += 5
            print(self.mana)

    def update_health_bar(self, surface):
        if self.health >= 75:
            bar_color = (111, 210, 46)
        elif self.health >= 25:
            bar_color = (255, 165, 0)
        else:
            bar_color = (255, 0, 0)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 45, self.rect.y - 15, self.health, 5]
        back_bar_position = [self.rect.x + 45, self.rect.y - 15, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def update_mana_bar(self, surface):
        back_bar_color2 = (60, 63, 60)
        bar_color2 = (51, 224, 255)
        bar_position2 = [self.rect.x + 55, self.rect.y - 5, self.mana, 3]
        back_bar_position2 = [self.rect.x + 55, self.rect.y - 5, self.max_mana, 3]
        pygame.draw.rect(surface, back_bar_color2, back_bar_position2)
        pygame.draw.rect(surface, bar_color2, bar_position2)

    def launch_projectile_right(self):
        if self.mana >= 5:
            self.all_projectiles.add(Projectile(self))
            self.mana -= 5

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity

    def move_up(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.y -= self.velocity

    def move_down(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.y += self.velocity
