import pygame

import sys

import os

from pygame.locals import *


pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screenwidth, screenheight = (480, 640)

screen = pygame.display.set_mode((screenwidth, screenheight))


class ScrollingBackground:

    def __init__(self, screenheight, imagefile):

        self.img = pygame.image.load(imagefile)

        self.coord = [0, 0]

        self.coord2 = [0, -screenheight]

        self.y_original = self.coord[1]

        self.y2_original = self.coord2[1]

    def UpdateCoords(self, speed_y, time):

        distance_y = speed_y * time

        self.coord[1] += distance_y

        self.coord2[1] += distance_y

        if self.coord2[1] >= 0:

            self.coord[1] = self.y_original
    
            self.coord2[1] = self.y2_original
# Set the framerate

framerate = 60



# Set the background scrolling speed

bg_speed = 100



# Load the background image here. Make sure the file exists!

StarField = ScrollingBackground(screenheight, "background.jpg")

pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Age Game')



# fix indentation

while True:

    time = clock.tick(framerate)/1000.0

    x, y = pygame.mouse.get_pos()




    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    # Set new Background Coordinates and update the screen

    StarField.UpdateCoords(bg_speed, time)

    StarField.Show(screen)

    pygame.display.update()