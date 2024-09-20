import pygame
import sys
from plot import Plot
from level import Level
from settings import *


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('SpongeBob SquarePants')
        self.screen.blit(pygame.image.load('../graphics/begin/SpongeBob SquarePants begin.png'), (0, 0))
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.plot = Plot()
        self.level = Level()
        # sound
        main_sound = pygame.mixer.Sound('../audio/SpongeBob SquarePants.mp3')
        main_sound.set_volume(1)
        main_sound.play(loops=-1)

    def show_plots(self):
        self.plot.plot_load(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.show_plots()
    game.run()
