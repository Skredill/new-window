import pygame
import random as rand


#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True







class block:
    def __init__(self,pos,rotation,color):
        self.pos = pos
        self.rotation = rotation
        self.color = color
        pygame.draw.rect(screen,color,(10,10),pos)



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



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player = block((200,200),0,"Gray")
    











    screen.fill("gray")
    pygame.display.flip()
    clock.tick(60)


pygame.quit()






