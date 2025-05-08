import pygame
import random as rand
import pandas as pd







# each in-game pixel will be 20px by 20px.


blockTypes = ["Cube","Line","Tpiece","RightL","LeftL","LeftZ","RightZ"]


    #pygame setup
pygame.init()
    #sets window to 259px by 459px, or 10 blocks by 20 blocks.
screen = pygame.display.set_mode((259,459))
    #initializes clock for framerate
clock = pygame.time.Clock()
    #sets gamestate as running, enabling while loop
running = True





class block:
    def __init__(self,pos,type,rotation,moving):
        self.pos = pos
        self.rotation = rotation
        self.type = type
        if self.type == "Square":
            pygame.draw.rect(screen,"red",(40,40),pos)

        if self.type == "TPiece":
            self.posX , self.posY = self.pos
            self.image = pygame.image.load("Images/Tpiece.png")
            pygame.sprite(self.image)

    #movement subclasses

    def moveLeft(self,value):
        self.x , self.y = self.pos
        self.x -= value
        self.pos = self.x , self.y

    def moveRight(self,value):
        self.x , self.y = self.pos
        self.x += value
        self.pos = self.x , self.y


    def collision(self,bool):
        self.collision = bool


activeBlock = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #spawn new block
    if activeBlock == False:

        
        
        block((124,20),rand(blockTypes),0,True)
        

        activeBlock = True



    









        #render screen
    screen.fill("gray")
    pygame.display.flip()
    clock.tick(60)


pygame.quit()






