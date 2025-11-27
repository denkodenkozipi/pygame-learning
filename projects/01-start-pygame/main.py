from operator import truediv

import pygame
import sys

# запуск Pygame
pygame.init()

# параметры окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First game!")

# цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE) # белый экран
    pygame.draw.rect(screen, RED, (355, 250, 100, 100)) # красный квадрат
    pygame.display.flip() # вывод нарисованного

# выключение
pygame.quit()
sys.exit()