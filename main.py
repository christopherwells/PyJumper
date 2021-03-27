from settings import *
import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        # pygame
        pygame.init()
        pygame.mixer.init()
        # window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        # game
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # new game
        self.all_sprites = pygame.sprite.Group()
        self.loop()

    def loop(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.update()
            self.events()
            self.draw()

    def update(self):
        # update
        self.all_sprites.update()

    def events(self):
        # pygame events
        for event in pygame.event.get():
            # window close event
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # draw events
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_splash(self):
        pass

    def show_level(self):
        pass

    def game_over(self):
        pass


game = Game()
game.show_splash()
while game.running:
    game.new()
    game.show_level()

pygame.quit()
