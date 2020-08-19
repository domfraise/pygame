import pygame, sys
from pygame.locals import *
import time
import math
import random
pygame.init()

screen=pygame.display.set_mode((640,360))
pygame.display.set_caption("Catch")

black = (0,0,0)
white = (250,250,250)
red = (250,0,0)
green = (0,250,0)
blue = (0,0,250)
center = (320,180)
x,y = 310,320
move_x,move_y,move_b=0,0,0

y1 = 0
y2 = -360/3
y3= -360*2/3

#bonus_ball start
xb,yb = 180,-10

width = 60

bonus_count = 0


font = pygame.font.Font(None,25)

score = 0
lives = 10

x1 = random.randrange(0,630)
x2 = random.randrange(0,630)
x3 = random.randrange(0,630)

clock = pygame.time.Clock()

 



while True:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
            

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                move_x = -10
            if event.key==pygame.K_RIGHT:
                move_x = 10
        if event.type==pygame.KEYUP:
            move_x = 0
    #cursor    
    curs = pygame.draw.rect(screen,white,(x,320,width,10))

    #cursor boundaries
    x+=move_x
    if x <= -30 :
        x=609
    elif x >=610:
        x=-29

    #falling balls
    ball1=pygame.draw.circle(screen,red,(x1,y1),5)
    ball2=pygame.draw.circle(screen,red,(x2,y2),5)
    ball3=pygame.draw.circle(screen,red,(x3,y3),5)

    
        
    
    #speed due to score
    if score <10:
        y1+=1
        y2+=1
        y3+=1
        level = 1
        
    elif score>=10 and score<30:
        y1+=2
        y2+=2
        y3+=2
        level = 2

    elif score>=30 and score < 60:
        y1+=3
        y2+=3
        y3+=3
        level = 3

    elif score>=60 and score < 100:
        y1+=4
        y2+=4
        y3+=4
        level = 4

    else:
        y1+=30
        y2+=30
        y3+=30
        level = "HOW ARE YOU STILL ALIVE!!!"

        
    #resetting caught balls
    if curs.collidepoint(x1,y1):
        x1 = random.randrange(0,630)
        y1 = -40
        score+=1
        bonus_count+=1
    if curs.collidepoint(x2,y2):
        x2 = random.randrange(0,630)
        y2 = -40
        score+=1
        bonus_count+=1
    if curs.collidepoint(x3,y3):
        x3 = random.randrange(0,630)
        y3 = -40
        score+=1
        bonus_count+=1

        
   

        
    #resetting missed balls
    if y1>360:
        x1 = random.randrange(0,630)
        y1 = 0
        lives-=1
        bonus_count=0
    if y2>360:
        x2 = random.randrange(0,630)
        y2 = 0
        lives-=1
        bonus_count=0
    if y3>360:
        x3 = random.randrange(0,630)
        y3 = 0
        lives-=1    
        bonus_count=0
    #reset missed bonus ball     
    if yb>360:
        xb = random.randrange(0,630)
        yb = -10    
        bonus_count=0
        move_b = 0

     #bonus ball
    b_ball=pygame.draw.circle(screen,green,(xb,yb),5)

    if bonus_count == 9:
        move_b = 1
    
        
        
    
    yb+=move_b

     #bonus ball catch reset
    if curs.collidepoint(xb,yb):
        xb = random.randrange(0,630)
        yb = -10
        move_b = 0
        bouns_count = 0
        if width <= 320:
            width += 40
        else:
            pass

    
    
            
    
    
    text = font.render(("Score: "+str(score)+"                                 Lives: "+str(lives)+"                               Speed Level: "+str(level)),True,(250,250,250))
    text_end = font.render("Out Of Lives!!!",True,white)
    screen.blit(text,(0,340))


    #quit
    if lives <= 0 :
        screen.blit(text_end,(280,180))

    clock.tick(75)
    
    pygame.display.update()

    if lives <= 0 :
        
        time.sleep(4)
        pygame.quit()
        break
print "Your score was "+str(score)
name = raw_input("Name: ")
fob = open("highscores_catch.txt","a")
fob.write(name+" - "+str(score)+"\n")
fob.close()
print "High score saved in Highscores_catch.txt"





