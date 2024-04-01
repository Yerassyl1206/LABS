import pygame
import os
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((700, 700))
b=pygame.image.load('Darkhan juzz.WEBP')
screen.blit(b,(0, 0))
pygame.display.flip()
running = True

pygame.mixer.music.load('music1.mp3')
pygame.mixer.music.play()

musics = ['music1.mp3', 'music2.mp3', 'music3.mp3']
cnt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_RETURN:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_LEFT:
                if cnt == 0:
                    cnt = 2
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
                else:
                    cnt -= 1
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
            if event.key == pygame.K_RIGHT:
                if cnt == 2:
                    cnt = 0
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
                else:
                    cnt += 1
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
    pygame.display.flip()