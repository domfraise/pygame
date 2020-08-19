import pygame, sys
from pygame.locals import *
import time
pygame.init()

screen=pygame.display.set_mode((640,360))
pygame.display.set_caption("Dom's Shitty Maze")


X,Y = 5,0
#animation start
a = 70

movex=0
movey=0

clock = pygame.time.Clock()

font = pygame.font.Font(None,25)





begin = time.time()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                movex=-5
            if event.key==pygame.K_RIGHT:
                movex=5
            if event.key==pygame.K_UP:
                movey=-5
            if event.key==pygame.K_DOWN:
                movey=5

        if event.type == pygame.KEYUP:
            movex,movey=0,0
            
    screen.fill((0,0,0))
    #cursor restes
    if X >590:
        X,Y = 5,0
    if X <0:
        X,Y = 5,0
    if Y >310:
        Y,X=0,5
    if Y<0:
        Y,X = 0,5
    #cursor movement
    X+=movex
    Y+=movey
    
    #speed
    clock.tick(50)

    #start and end blocks
    start = pygame.draw.rect(screen,(0,250,0),(0,0,60,60))
    end = pygame.draw.rect(screen,(0,250,0),(580,0,60,60))

    #maze rects
    wall1=pygame.draw.rect(screen,(200,0,200),(60,0,10,300))
    wall2 = pygame.draw.rect(screen,(200,0,200),(140,200,200,200))
    wall3 = pygame.draw.rect(screen,(200,0,200),(140,0,80,120))
    wall4 = pygame.draw.rect(screen,(200,0,200),(300,70,60,300))
    wall5 = pygame.draw.rect(screen,(200,0,200),(420,0,90,290))
    #animation
    wall6 =  pygame.draw.rect(screen,(200,0,200),(570,a,10,300))
    a-=10
    if a < - 250:
        a = 360
    
    
    
    curs = pygame.draw.rect(screen,(250,250,250),(X,Y,50,50))
    maze = [wall1,wall2,wall3,wall4,wall5,wall6]
    #reset
    if curs.colliderect(wall1)or curs.colliderect(wall2) or curs.colliderect(wall3) or curs.colliderect(wall4) or curs.colliderect(wall5) or curs.colliderect(wall6):
        #sound effect here#
        X,Y = 5,0

    #timer
    
    if curs.collidepoint(620,10):
        
        time_taken = finish - begin
        text =  font.render(str(time_taken)+" Seconds",True,(250,250,250))
        time.sleep(5)
        break
        
    else:
        finish = time.time()
        text = font.render(str(time.time()-begin),True,(250,250,250))
    screen.blit(text,(150,300))

    
    pygame.display.update()

pygame.quit()

print "Your time was "+str(time_taken)
name = raw_input("Name: ")
fob = open("highscores.txt","a")
fob.write(name+" - "+str(time_taken)+"\n")
fob.close()
print "High score saved in Highscores.txt"



