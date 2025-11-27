import pygame
import sys

# запуск Pygame
pygame.init()

# параметры окна
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("my first game!")

# цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE) # белый экран
    pygame.draw.circle(screen, GREEN, (500, 400), 350) # зеленый круг
    pygame.display.flip() # вывод нарисованного

# выключение
pygame.quit()
sys.exit()