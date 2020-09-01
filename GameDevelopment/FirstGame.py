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

for i in range(2000):
    pygame.draw.rect(win, (100,100,255), (x, y, width, height))
    pygame.display.update()

    pygame.draw.circle(win,(0,255,0),(x+100,y+30),20)
    pygame.display.update()
pygame.quit()






