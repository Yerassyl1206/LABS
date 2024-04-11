

import pygame
from random import randrange
pygame.init()

clock = pygame.time.Clock()

screen=pygame.display.set_mode((800,800))

screen.fill((0,0,0))
running=True



def restart_game():
    res = 800 
    size = 50
    x,y = randrange(0,res,size),randrange(0,res,size)
    apple = randrange(0,res,size),randrange(0,res,size)
    dirs = {'UP':True,'DOWN':True,'RIGHT':True,'LEFT':True}
    length = 1
    snake = [(x,y)]
    dx,dy = 0,0
    fps = 10
    score = 0
    font_score = pygame.font.SysFont('Arial',26,bold = True)
    font_end = pygame.font.SysFont('Arial',66,bold=True)

    fo = pygame.image.load('fonforsnake.jpg')
    fon = pygame.transform.scale(fo,(res,res))
    running = True
    while running:
        screen.fill((255,255,255))
        screen.blit(fon,(0,0))

        [(pygame.draw.rect(screen,pygame.Color('green'),(i,j,size-2,size-2)))for i,j in snake]

        pygame.draw.rect(screen,pygame.Color('red'),(*apple,size-5,size-5))
        render_score = font_score.render(f'SCORE:{score}',1,pygame.Color('white'))
        screen.blit(render_score,(5,5))

        x+=dx*size
        y+=dy*size
        snake.append((x,y))
        snake = snake[-length:]

        if snake[-1] == apple:
            apple = randrange(0,res,size),randrange(0,res,size)
            length += 1
            score += 1
            fps += 1
    
        if x < 0 or x > res - size or y < 0 or y > res - size or len(snake) != len(set(snake)):
            while True:
                render_end = font_end.render('GAME OVER',1,pygame.Color('white'))
                screen.blit(render_end,(res//2 - 200,res//3))
                render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('white')) 
                screen.blit(render_score, ((res //2) - 75, (res//3) + 70))

                draw_button(800/2 - 125 , 800/2 - 30, 200, 50, 'RESTART')

                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 800/2 - 50 <= mouse_pos[0] <= 800/2 + 150 and 800/2 - 25 <= mouse_pos[1] <= 800/2 +25 :
                            restart_game()

        pygame.display.flip()
        clock.tick(fps)  

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    
    

        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP] and dirs['UP']: 
            dx, dy = 0, -1 
            dirs = {'UP': False, 'DOWN': True, 'RIGHT': True, 'LEFT': True} 
        if keys[pygame.K_DOWN] and dirs['DOWN']: 
            dx, dy = 0, 1 
            dirs = {'UP': True, 'DOWN': False, 'RIGHT': True, 'LEFT': True} 
        if keys[pygame.K_LEFT] and dirs['LEFT']: 
            dx, dy = -1, 0 
            dirs = {'UP': True, 'DOWN': True, 'RIGHT': True, 'LEFT': False} 
        if keys[pygame.K_RIGHT] and dirs['RIGHT']: 
            dx, dy = 1, 0 
            dirs = {'UP': True, 'DOWN': True, 'RIGHT': False, 'LEFT': True}  



def draw_text(text,font,color,surface,x,y):
    text_obj = font.render(text,True,color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    surface.blit(text_obj,text_rect)

def draw_button(x,y,width,height,text):
    pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    font = pygame.font.Font(None, 36)
    draw_text(text,font,(255,255,255), screen,x + width/2,y + height/2)

restart_game()
