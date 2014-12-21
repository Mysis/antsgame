__author__ = 'conrad'
import pygame

WHITE = (255, 255, 255)

class SelectionRect():

    def __init__(self):

        self.startPoint = [None, None]
        self.selecting = False
        self.width = 0
        self.height = 0
        
    def select(self, selectedSpritesGroup, allPossibleSpritesGroup):
        
        for possibleSprite in allPossibleSpritesGroup:
            if self.startPoint[0] < possibleSprite.x < self.startPoint[0] + self.width and self.startPoint[1] < possibleSprite.y < self.startPoint[1] + self.height:
                selectedSpritesGroup.add(possibleSprite)
            if self.startPoint[0] < possibleSprite.x < self.startPoint[0] + self.width and self.startPoint[1] > possibleSprite.y > self.startPoint[1] + self.height:
                selectedSpritesGroup.add(possibleSprite)
            if self.startPoint[0] > possibleSprite.x > self.startPoint[0] + self.width and self.startPoint[1] < possibleSprite.y < self.startPoint[1] + self.height:
                selectedSpritesGroup.add(possibleSprite)
            if self.startPoint[0] > possibleSprite.x > self.startPoint[0] + self.width and self.startPoint[1] > possibleSprite.y > self.startPoint[1] + self.height:
                selectedSpritesGroup.add(possibleSprite)

    def draw(self, screen):

        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            self.width = mousePos[0] - self.startPoint[0]
            self.height = mousePos[1] - self.startPoint[1]
            pygame.draw.rect(screen, WHITE, (self.startPoint[0], self.startPoint[1], self.width, self.height), 1)
            self.selecting = True
            