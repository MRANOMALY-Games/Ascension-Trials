import sys

import pygame
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Ascension Trials | A game by Hatman Games')
        self.screen = pygame.display.set_mode((1080, 720))

        self.clock = pygame.time.Clock()

        self.playerplaceholder = pygame.image.load('data/sprites/player-placeholder.png')

        self.playerplaceholder_pos = [500, 350]
        self.movement = [False, False, False, False]
    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.playerplaceholder_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.playerplaceholder_pos[0] += (self.movement[3] - self.movement[2]) * 5
            self.screen.blit(self.playerplaceholder, self.playerplaceholder_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                        print('up')
                    elif event.key == pygame.K_DOWN:
                        self.movement[1] = True
                        print('down')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                        print('up')
                    elif event.key == pygame.K_DOWN:
                        self.movement[1] = False
                        print('down')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                        print('up')
                    elif event.key == pygame.K_DOWN:
                        self.movement[1] = True
                        print('down')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[2] = True
                        print('left')
                    elif event.key == pygame.K_RIGHT:
                        self.movement[3] = True
                        print('right')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[2] = False
                        print('left')
                    elif event.key == pygame.K_RIGHT:
                        self.movement[3] = False
                        print('right')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                        print('up (alt)')
                    elif event.key == pygame.K_s:
                        self.movement[1] = True
                        print('down (alt)')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    elif event.key == pygame.K_s:
                        self.movement[1] = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                        print('up (alt)')
                    elif event.key == pygame.K_s:
                        self.movement[1] = True
                        print('down (alt)')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[2] = True
                        print('left (alt)')
                    elif event.key == pygame.K_d:
                        self.movement[3] = True
                        print('right (alt)')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[2] = False
                    elif event.key == pygame.K_d:
                        self.movement[3] = False
                
            pygame.display.update()
            self.clock.tick(60)

Game().run()