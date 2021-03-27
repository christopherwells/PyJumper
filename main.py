from random import randint
import pygame
from pygame.locals import *
from settings import *
from sprites import *


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
        self.blocks = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        p1 = Block(0, HEIGHT - 32, WIDTH, 32)
        p2 = Block(WIDTH / 2 - 32, HEIGHT * 3 / 4, 100, 20)
        self.all_sprites.add(p1)
        self.all_sprites.add(p2)
        self.blocks.add(p1)
        self.blocks.add(p2)
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
        # collision detection
        collision = pygame.sprite.spritecollide(
            self.player, self.blocks, False)
        if collision:
            self.player.pos.y = collision[0].rect.top + 1
            self.player.vel.y = 0

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
        # flip display after draw events
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
