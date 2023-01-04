import pygame, sys
from pygame.locals import *
import random, time
from skimage.io import imread
from numpy import fliplr, flipud
from skimage.transform import rescale
# image = imread('cube.jpg')
# image = rescale(imread('cube.jpg'), 0.25, multichannel=True)
# image = fliplr(rescale(imread(), 0.25, multichannel=True))
speed = 1
# Importing the pygame module


# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((1200,600))


# Create a list of different sprites
# that you want to use in the animation
image_zumbiF = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (1).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (2).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (3).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (4).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (5).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (6).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (7).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (8).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (9).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (10).png"),(90,100)),True,False)]
image_zumbiM = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (1).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (2).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (3).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (4).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (5).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (6).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (7).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (8).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (9).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (10).png"),(90,100)),True,False)]


# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Creating a new variable
# We will use this variable to
# iterate over the sprite list
value = 0
x = 1200
y = 100

# Creating a boolean variable that
# we will use to run the while loop
run = True

# Creating an infinite loop
# to run our game
while run:

    if x == 0:
        pygame.quit()
        sys.exit()
    # Setting the framerate to 3fps just
    # to see the result properly
    clock.tick(30)

    # Setting 0 in value variable if its
    # value is greater than the length
    # of our sprite list
    if value >= len(image_zumbiF)*8:
        value = 0

    # Storing the sprite image in an
    # image variable
    image = image_zumbiF[int(value/8)]
    image2 = image_zumbiM[int(value/8)]

    # Creating a variable to store the starting
    # x and y coordinate

    # Changing the y coordinate
    # according the value stored
    # in our value variable


    # Displaying the image in our game window
    window.blit(image, (x, y))
    window.blit(image2, (x, 300))
    # Updating the display surface
    pygame.display.update()

    # Filling the window with black color
    window.fill((0, 0, 0))

    # Increasing the value of value variable by 1
    # after every iteration
    value += 1
    x -= speed
