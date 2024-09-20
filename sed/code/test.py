import sys
import pygame
from plot import Plot

pygame.init()
plots = []
for i in range(0, 4):
    plots.append(pygame.image.load("../plot/{}.png".format(i)))

show_image = False
index = 0
image = pygame.image.load("../graphics/tilemap/ground.png")

screen = pygame.display.set_mode((800, 600), 0)
screen.blit(image, (0, 0))
pygame.display.update()

plot = Plot()
plot.plot_load(screen)