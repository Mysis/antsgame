__author__ = 'conrad'
import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class AntLeader(pygame.sprite.Sprite):

    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)

        self.hspeed = 0
        self.vspeed = 0
        self.x = location[0]
        self.y = location[1]
        self.destination = [self.x, self.y]

        self.antSpritesGroup = pygame.sprite.Group()
        for i in range(10):
            ant = AntFollower(self, i)
            self.antSpritesGroup.add(ant)

    def update(self):

        distanceToDestination = [self.destination[0] - self.x, self.destination[1] - self.y]

        try:
            self.x += 5 * distanceToDestination[0]/(abs(distanceToDestination[0]) + abs(distanceToDestination[1]))
        except:
            self.x += 0
        try:
            self.y += 5 * distanceToDestination[1]/(abs(distanceToDestination[0]) + abs(distanceToDestination[1]))
        except:
            self.y += 0

        self.antSpritesGroup.update()

    def draw(self, screen):

        self.antSpritesGroup.draw(screen)

class AntFollower(pygame.sprite.Sprite):

    def __init__(self, antLeader, move):

        pygame.sprite.Sprite.__init__(self)

        self.antLeader = antLeader
        self.move = move

        self.image = pygame.Surface((3, 3))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = self.antLeader.x + random.randint(-10, 10)
        self.rect.y = self.antLeader.y + random.randint(-10, 10)

    def update(self):

        self.move += 1
        if self.move > 10:
            self.rect.x = self.antLeader.x + random.randint(-10, 10)
            self.rect.y = self.antLeader.y + random.randint(-10, 10)
            self.move = 0