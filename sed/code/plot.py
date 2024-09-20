import sys
import pygame


class Plot:
    pygame.init()

    def __init__(self):
        self.plots = []
        self.index = 0
        self.show_image = False

    def plot_load(self, screen):
        for i in range(0, 5):
            self.plots.append(pygame.image.load("../plot/{}.png".format(i)))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.show_image and self.index < len(self.plots):
                            self.show_image = True
                            screen.blit(self.plots[self.index], (0, 0))
                            pygame.display.update()
                            self.index += 1
                        self.show_image = False
                        if self.index >= len(self.plots):
                            return

