import pygame
pygame.init()

#This is the name of the Window
win = pygame.display.set_mode((500,500))

#Labelling the Window
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
speed = 5

done = False
while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    win.fill((0, 0, 0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:    y = y - 1
    if pressed[pygame.K_DOWN]:  y = y + 1
    if pressed[pygame.K_LEFT]:  x = x - 1
    if pressed[pygame.K_RIGHT]: x = x + 1

    pygame.draw.rect(win, (100,100,255), (x, y, width, height))
    pygame.display.flip()

pygame.quit()






