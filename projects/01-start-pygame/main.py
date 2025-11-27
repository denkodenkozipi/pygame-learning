import pygame
import sys
import random

# запуск Pygame
pygame.init()

# параметры окна
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("my first game!")

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# разные цвета для круга
colors_cirl = [RED, GREEN, BLUE]
current_color = GREEN
# разные цвета для фона
colors_bg = [WHITE, BLACK]
current_color_bg = WHITE


# параметры круга
radius_circle = 100 # радиус круга
circle_x = 500 # положение по x
circle_y = 0 # положение y

# параметры движения
direction_x = 1
direction_y = 1
speed = 1

# цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # движение
    circle_y += speed * direction_y
    circle_x += speed * direction_x

    # смена движения по y со сменой цветов по условию
    if circle_y >= 800 - radius_circle:
        direction_y = -1
        current_color = random.choice(colors_cirl)
    elif circle_y <= radius_circle:
        direction_y = 1
        current_color_bg = random.choice(colors_bg)
    # смена движения по x со сменой цветов по условию
    if circle_x >= 1000 - radius_circle:
        direction_x = -1
        current_color = random.choice(colors_cirl)
    elif circle_x <= radius_circle:
        direction_x = 1
        current_color_bg = random.choice(colors_bg)

    screen.fill(current_color_bg) # фон
    pygame.draw.circle(screen, current_color, (circle_x, circle_y), radius_circle) # круг
    pygame.display.flip() # вывод нарисованного

# выключение
pygame.quit()
sys.exit()