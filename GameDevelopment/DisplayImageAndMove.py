import pygame # Step -1
from pygame import mixer

pygame.init()  # Step -2
mixer.init()

screen = pygame.display.set_mode((500, 500))  # Step 3
pygame.display.set_caption('Dog with Music')  # Step -4

# Loading the song
mixer.music.load("02.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

x = 20  # x coordnate of image
y = 30  # y coordinate of image

dogImage = pygame.image.load("dog.png").convert()

# Quit the program
running = True
speed = 1
mixer.music.play()

while (running):  # loop listeneint for end of game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mixer.music.stop()
            running = False

    screen.fill((0, 0, 0))

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:    y = y - speed
    if pressed[pygame.K_DOWN]:  y = y + speed
    if pressed[pygame.K_LEFT]:  x = x - speed
    if pressed[pygame.K_RIGHT]: x = x + speed

    screen.blit(dogImage, (x, y))  # paint to screen
    pygame.display.flip()  # paint screen one time

# loop over, quite pygame
pygame.quit()
