import pygame  # Step -1
from pygame import mixer

pygame.init()  # Step -2
mixer.init()

mixer.music.load("02.mp3")
mixer.music.set_volume(0.5)

screen = pygame.display.set_mode((500, 500))  # Step 3

pygame.display.set_caption('Display an image')  # Step -4

x = 20  # x coordnate of image
y = 30  # y coordinate of image

penguinImage = pygame.image.load("dog.png").convert()
screen.blit(penguinImage, (x, y))  # paint to screen

pygame.display.flip()  # paint screen one time
mixer.music.play()

# Quit the program
running = True
while (running):  # loop listeneint for end of game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# loop over, quite pygame
pygame.quit()
