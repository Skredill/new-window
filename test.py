import pygame
import random as rand



# each in-game pixel will be 20px by 20px.


blockTypes = ["Square","Line","Tshape","rightL","leftL"]


    #pygame setup
pygame.init()
    #sets window to 200px by 600px, or 10 blocks by 30 blocks.
screen = pygame.display.set_mode((200,600))
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

        if self.type == "Tshape":
            posX , posY = self.pos
            pygame.draw.rect(screen,"orange",(60,20),pos)
        
            pygame.draw.rect(screen,"orange",(20,20),(posX + 20, posY + 20))

    #movement subclasses

    def moveLeft(self,value):
        self.x , self.y = self.pos
        self.x -= value
        self.pos = self.x , self.y

    def moveRight(self,value):
        self.x , self.y = self.pos
        self.x += value
        self.pos = self.x , self.y

    def moveUp(self,value):
        self.x , self.y = self.pos
        self.y -= value
        self.pos = self.x , self.y

    def moveDown(self,value):
        self.x , self.y = self.pos
        self.y += value
        self.pos = self.x , self.y

    def collision(self,bool):
        self.collision = bool


    





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    activeBlock = block((200,200),0,"Gray",True)
    










    screen.fill("gray")
    pygame.display.flip()
    clock.tick(60)


pygame.quit()






