import random

#import numpy as np

import pygame
from action import Action
from button import Button
import rps

def fight(user_input, computer_input, user_point, computer_point):
    '''Decide who wins, rock - 1, scissors - 2, paper - 3'''
    if user_input == computer_input:
        pass
    elif user_input == 'rock':
        if computer_input == 'scissors':
            user_point = 1
        else:
            computer_point = 1
    elif user_input == 'scissors':
        if computer_input == 'rock':
            computer_point = 1
        else:
            user_point = 1
    else:
        if computer_input == 'rock':
            user_point = 1
        else:
            computer_point = 1
    return  user_point, computer_point

def gen_input(action):
    computer_input = random.choice(action)
    return computer_input

def text_to_display(user_point, computer_point):
    if user_point == 1:
        text = 'You won'
    elif computer_point == 1:
        text = 'Computer won'
    else:
        text = "It's a tie"
    return text

def play_round(user_input, actions, score, screen, rps_settings):
    "Compiles all functions responsible for getting the result of the round in one function"
    #initial points
    user_point, computer_point = [0, 0]
    #computer's choice of action
    computer_input = rps.gen_input(actions)
    #deciding who won
    user_point, computer_point = rps.fight(user_input, computer_input, user_point, computer_point)
    text_result = rps.text_to_display(user_point, computer_point)
    #update score
    score[0] += user_point
    score[1] += computer_point
    #set up action based on round results
    action1 = Action(screen, user_input + '.bmp', 1, True, rps_settings) #users pick
    action2 = Action(screen, computer_input + '.bmp', 2, True, rps_settings) #computer pick

    return computer_input, text_result, score, action1, action2

def final_screen(screen, rps_settings, text_result, score, action1, action2):
    "draw final screen with the result displayed"
    #selecting font
    font = pygame.font.Font('Prototype.ttf', 35)
    screen_rect = screen.get_rect()
    text = font.render(text_result, True, (49, 47, 48))

    #position result text
    textRect = text.get_rect()
    textRect.centerx = screen_rect.centerx
    textRect.centery = 1/8*rps_settings.screen_height

    #score
    text_score = font.render('SCORE {} - {}'.format(score[0], score[1]), True, (49, 47, 48))
    text_scoreRect = text_score.get_rect()
    text_scoreRect.centerx = screen_rect.centerx
    text_scoreRect.centery = 3/4*rps_settings.screen_height

    #user, computer text
    font = pygame.font.Font('Prototype.ttf', 25)
    text_user = font.render('You', True, (49, 47, 48))
    text_userRect = text_user.get_rect()
    text_userRect.centerx = 1/4*rps_settings.screen_width
    text_userRect.centery = 1/4*rps_settings.screen_height


    text_computer = font.render('Computer', True, (49, 47, 48))
    text_computerRect = text_computer.get_rect()
    text_computerRect.centerx = 3/4*rps_settings.screen_width
    text_computerRect.centery = 1/4*rps_settings.screen_height

    #set up a buttons
    button = Button(rps_settings, screen, 'PLAY AGAIN')

    #draw text onto screen
    screen.blit(text, textRect)
    screen.blit(text_user, text_userRect)
    screen.blit(text_computer, text_computerRect)
    screen.blit(text_score, text_scoreRect)
    button.blitme()

    #draw hands onto screen
    action1.blitme()
    action2.blitme()

def choose_screen(screen, rps_settings, actions):
    #create prompt text
    font = pygame.font.Font('Prototype.ttf', 35)
    text_prompt = font.render('Take your pick', True, (49, 47, 48))
    text_prompt_rect = text_prompt.get_rect()
    text_prompt_rect.centerx = rps_settings.screen_width/2
    text_prompt_rect.centery = 1/6 * rps_settings.screen_height
    screen.blit(text_prompt, text_prompt_rect)

    #choose font
    font = pygame.font.Font('Prototype.ttf', 25)
    #draw hands and text for them
    for i in range(3):
        #define action and draw hand
        action = Action(screen, actions[i] + '.bmp', i + 1, False, rps_settings)
        action.blitme()
        #position and display text
        text = font.render(actions[i].upper(), True, (49, 47, 48))
        text_rect = text.get_rect()
        text_rect.centerx = action.rect.centerx
        text_rect.centery = action.rect.centery + 1/4 * rps_settings.screen_height
        screen.blit(text, text_rect)
