import pygame
import os
import datetime

pygame.init()

size = (WIDTH, HEIGHT) = (1000, 800)
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()
white = (255, 255, 255)

bg = pygame.transform.scale(pygame.image.load(os.path.join('main-clock.png')), (WIDTH, HEIGHT))

sec_img = pygame.image.load(os.path.join('left-hand.png'))
x_sec, y_sec = WIDTH / 2 + 10, HEIGHT / 2

min_img = pygame.image.load(os.path.join('right-hand.png'))
x_min, y_min = WIDTH / 2, HEIGHT / 2 - 15


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect


while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    screen.blit(bg, (0, 0))

    now = datetime.datetime.now()

    second = now.second
    screen.blit(rot_center(sec_img, -second * 6, x_sec, y_sec)[0], rot_center(sec_img, -second * 6, x_sec, y_sec)[1])

    minute = now.minute
    screen.blit(rot_center(min_img, -minute * 6, x_min, y_min)[0], rot_center(min_img, -minute * 6, x_min, y_min)[1])

    pygame.draw.circle(screen, (53, 54, 55), (WIDTH / 2, HEIGHT / 2), 30)

    pygame.display.update()

pygame.quit()