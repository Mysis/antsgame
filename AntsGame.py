__author__ = 'conrad'
import pygame
import antbehavior, selection

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game():

    def __init__(self):

        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ants")
        clock = pygame.time.Clock()

        selectedSpritesGroup = pygame.sprite.Group()
        allSelectableSpritesGroup = pygame.sprite.Group()

        ant = antbehavior.AntLeader((400, 300))
        allSelectableSpritesGroup.add(ant)
        select = selection.SelectionRect()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            mouseButtons = pygame.mouse.get_pressed()
            if mouseButtons[0] and not mouseButtonsPrevious[0]:
                select.startPoint = pygame.mouse.get_pos()
                for selectedLeader in selectedSpritesGroup:
                    for selectedFollower in selectedLeader.antSpritesGroup:
                        selectedFollower.image.fill(BLUE)
                selectedSpritesGroup.empty()
            if mouseButtons[0] and mouseButtonsPrevious[0]:
                select.select(selectedSpritesGroup, allSelectableSpritesGroup)
                for selectedLeader in selectedSpritesGroup:
                    for selectedFollower in selectedLeader.antSpritesGroup:
                        selectedFollower.image.fill(RED)
            if mouseButtons[2]:
                for ant in selectedSpritesGroup:
                    ant.destination = pygame.mouse.get_pos()
            mouseButtonsPrevious = mouseButtons

            #update all objects

            ant.update()

            #draw all objects

            screen.fill(BLACK)
            ant.draw(screen)
            select.draw(screen)
            pygame.display.flip()

            #final updates, plus framerate check

            clock.tick(40)

game = Game()