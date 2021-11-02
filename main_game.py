import sys

import pygame

import rps
from button import Button
from action import Action

class Settings():
    "background and screen settings"

    def __init__(self, screen_height, screen_width, bg_colour):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.bg_colour = bg_colour

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    rps_settings = Settings(600, 1000, (255, 234, 0))

    screen = pygame.display.set_mode((rps_settings.screen_width, rps_settings.screen_height))
    pygame.display.set_caption("Rock! Paper! Scissors!")

    screen_choice = 1 #differentiate between screens
    actions = ['rock', 'paper', 'scissors']
    score = [0, 0]

    #start the main loop for the game
    while True:
        #get mouse position
        mouse = pygame.mouse.get_pos()

        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                #checks if 'play again' button is clicked
                if (rps_settings.screen_width/2 - 85) <= mouse[0] <= (rps_settings.screen_width/2 + 85) and \
                (9/10*rps_settings.screen_height - 25) <= mouse[1] <= (9/10*rps_settings.screen_height + 25)\
                and screen_choice == 2:
                    screen_choice = 1

                #choosing action
                #1 - rock
                if (1/6*rps_settings.screen_width - 95) <= mouse[0] <= (1/6*rps_settings.screen_width + 95) and \
                (rps_settings.screen_height/2 - 95) <= mouse[1] <= (rps_settings.screen_height/2 + 95) and \
                screen_choice == 1:
                    screen_choice = 2
                    user_input = 'rock'
                    computer_input, text_result, score, action1, action2 = rps.play_round(user_input, actions, score, screen, rps_settings)
                #2 - paper
                if (1/2*rps_settings.screen_width - 95) <= mouse[0] <= (1/2*rps_settings.screen_width + 95) and \
                (rps_settings.screen_height/2 - 95) <= mouse[1] <= (rps_settings.screen_height/2 + 95) and \
                screen_choice == 1:
                    screen_choice = 2
                    user_input = 'paper'
                    computer_input, text_result, score, action1, action2 = rps.play_round(user_input, actions, score, screen, rps_settings)
                #3 - scissors
                if (5/6*rps_settings.screen_width - 95) <= mouse[0] <= (5/6*rps_settings.screen_width + 95) and \
                (rps_settings.screen_height/2 - 95) <= mouse[1] <= (rps_settings.screen_height/2 + 95) and \
                screen_choice == 1:
                    screen_choice = 2
                    user_input = 'scissors'
                    computer_input, text_result, score, action1, action2 = rps.play_round(user_input, actions, score, screen, rps_settings)


        #Redraw screen
        screen.fill(rps_settings.bg_colour)
        #check which screen to draw
        if screen_choice == 1:
            rps.choose_screen(screen, rps_settings, actions)
        else:
            rps.final_screen(screen, rps_settings, text_result, score, action1, action2)

        #Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
