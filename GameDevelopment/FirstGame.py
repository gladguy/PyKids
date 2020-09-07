import pygame
pygame.init()

#This is the name of the Window
win = pygame.display.set_mode((500,500))

#Labelling the Window
pygame.display.set_caption("First Game")

x = 250
y = 250
width = 40
height = 40
speed = 1

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Good Bye !!")
            done = True

    win.fill((0, 0, 0))

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:    y = y - speed
    if pressed[pygame.K_DOWN]:  y = y + speed
    if pressed[pygame.K_LEFT]:  x = x - speed
    if pressed[pygame.K_RIGHT]: x = x + speed

    pygame.draw.rect(win, (100,100,255), (x, y, width, height))
    pygame.display.flip()

pygame.quit()






