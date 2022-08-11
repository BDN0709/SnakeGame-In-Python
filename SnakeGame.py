import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def PrintScore(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])
 
 
 
def DrawSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])
 
 
def Message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [dis_width / 6, dis_height / 3])
 
 
def GameLoop():
    game_close = False
    game_over = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_close:
 
        while game_over == True:
            display.fill(blue)
            Message("You Lost! Press C - Play Again or Q - Quit", red)
            PrintScore(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_c:
                        GameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True
 
        DrawSnake(snake_block, snake_List)
        PrintScore(Length_of_snake)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
GameLoop()