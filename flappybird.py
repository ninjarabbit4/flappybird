# Using as a guide: https://www.askpython.com/python/examples/flappy-bird-game-in-python

import sys
import random
import pygame
from pygame.locals import *

# Declare global variables
fps = 32
screen_width = 300
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

ground_y = screen_height * 0.8
game_images = {}
game_sounds = {}

player = "C:/Users/tomxu/Documents/GitHub/flappybird/bird.jpg"
background = "C:/Users/tomxu/Documents/GitHub/flappybird/background.jpg"
pipe = "C:/Users/tomxu/Documents/GitHub/flappybird/pipe.jpg"
title = "C:/Users/tomxu/Documents/GitHub/flappybird/title.png"

if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    game_images=['numbers'] = (
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/one.jpeg").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/two.jpeg").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/three.webp").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/four.jpg").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/five.jpeg").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/six.jpeg").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/seven.png").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/eight.png").convert_alpha(),
        pygame.image.load("C:/Users/tomxu/Documents/GitHub/flappybird/nine.jpeg").convert_alpha()
        )
    # No message or base at the moment - let's just see how it goes so far
    # game_images['message'] = pygame.image.load('gallery/images/message.png').convert_alpha()
    # game_images['base'] = pygame.image.load('gallery/images/base.png').convert_alpha()

    game_images['background'] = pygame.image.load(background).convert_alpha()
    game_images['player'] = pygame.image.load(player).convert_alpha()
    game_images['title'] = pygame.image.load(title).convert_alpha()

    # No game sounds either
    # game_sounds['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    # game_sounds['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    # game_sounds['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    # game_sounds['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    # game_sounds['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    
    while True:
        welcomeScreen()
        mainGame()