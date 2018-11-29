import pygame
import time
import random

pygame.init()
height=1000
width=2000

white=(255 , 255 , 255)
black=(0, 0 , 0)
red=(255 , 0 , 0)
blue=(255 , 255 , 0)
green=( 0, 255 , 0)

gamedisplay=pygame.display.set_mode((width , height))
pygame.display.set_caption('this is gona be a car')
clock=pygame.time.Clock()
carimage=pygame.image.load('car1.png')
def car(x,y):
    gamedisplay.blit(carimage,(x,y))
def textobjects(text , font):
    textsurface=font.render(text , True , black)
    return textsurface , textsurface.get_rect()


def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf', 115)
    textsurf , textrect=textobjects(text , largetext)
    textrect.center=(width/2 , height/2)
    gamedisplay.blit(textsurf , textrect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('you crashed')

def game_loop():
    change_x=0
    x = ( width * 0.45)
    y = ( height * 0.6 )
    car_width=450

    gameExit=False

    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                change_x=-5
            elif event.key==pygame.K_RIGHT :
                change_x=5


            x+=change_x

            gamedisplay.fill(blue)
            pygame.draw.rect(gamedisplay , (0 , 100 , 0) , (0 , 600 , 2000 , 400))
            car(x,y)
            if x>width-car_width or x<0:
                crashed=True
                crash()
            pygame.display.update()
            clock.tick(60)


game_loop()
pygame.quit()
quit()
