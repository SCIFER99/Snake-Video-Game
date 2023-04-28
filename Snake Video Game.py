# By: Tim Tarver
# Snake Video Game developed in Python

import pygame
import time
import random

# Initialize the variables for the screen shown

pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nokia Phone: Snake Game")

# Define all colors

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)


###### EVENT PROGRAMMING ###### 

# Implement all actions while playing the game.
# If the game is over, it will close automatically.

snake_circle = 10

clock = pygame.time.Clock()

# Initialize the speed

snake_speed = 30

# Style of Font

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to Keep Score

def your_score(score):
    value = score_font.render("Your Score:" + str(score), True, yellow)
    window.blit(value, [0, 0])

# Function to Extend the Snake whenever it Eats.

def snake_extension():
    pass

# Our Snake Function

def our_snake(snake_circle, snake_list):

    for x in snake_list:
        pygame.draw.circle(window, green, [x[0], x[1]], snake_circle)

# Display all Messages when specific events happen

def message_display(msg, color):

    message = font_style.render(msg, True, color)
    window.blit(message, [width / 2, height / 2])

# The Game Loop Function

def game_loop():

    x1_change = 0
    y1_change = 0
    x1 = width / 2
    y1 = height / 2
    game_over = False
    game_close = False

    snake_list = []
    snake_length = 1

    # Snake Food for Growth

    food_x = round(random.randrange(0, width-snake_circle) / 10.0)*10.0
    food_y = round(random.randrange(0, height-snake_circle) / 10.0)*10.0

    # Event Programming Section

    while not game_over:

        while game_close == True:
            window.fill(black)
            message_display("Game Over. Press q to Quit or P to play", red)
            pygame.display.update()

            # Events for Quitting or Replaying the Game
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        # Motion of the Snake with Arrow Keys
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_circle
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_circle
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_circle
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_circle
                    x1_change = 0

        # If you go out of bounds, the game will end.            

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True


        
        x1 += x1_change
        y1 += y1_change

        window.fill(black)
        
        
        pygame.draw.circle(window, red, [food_x, food_y], snake_circle-3)
        

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_circle, snake_list)
        your_score(snake_length - 1)
        pygame.display.update()

                
        # If food is eaten, change food coordinates randomly
        
        if x1 == food_x and y1 == food_y:

            food_x = round(random.randrange(0, width-snake_circle) / 10.0)*10.0
            food_y = round(random.randrange(0, height-snake_circle) / 10.0)*10.0
            snake_length += 1
                        
                                
        
        clock.tick(snake_speed)



    pygame.quit()
    quit()

game_loop()    
