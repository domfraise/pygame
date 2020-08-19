import pygame, sys
from pygame.locals import *
import time
pygame.init()
screen_width = 640
screen_height = 360
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("The Improbable Maze")

clock = pygame.time.Clock()
font = pygame.font.Font(None,25)
#colors
black = (0,0,0)
white = (250,250,250)
red = (250,0,0)
green = (0,250,0)
blue = (0,0,250)
yellow = (255,255,0)
orange = (255,128,0)

time_start = time.time()
class Curr():
    def __init__(self):
        self.x = 3
        self.y = 0
        self.width = 5
        self.height = 5
        self.move_x = 0
        self.move_y = 0
        self.speed = 2
        self.color = green
        self.rect = pygame.draw.rect(screen,(red),(self.x,self.y,self.width,self.height))
    def move(self,move_x,move_y):
        self.x+=move_x
        self.y+=move_y
        #cursor boundaries
        if self.x <= 0 :
            self.x = 0
        if self.x >= screen_width - self.width:
            self.x = screen_width-self.width
        if self.y <= 0 :
            self.y = 0
        if self.y >= screen_height - self.height:
            self.y = screen_height-self.height

        #collisions
        for item in walls:
            
            if self.rect.colliderect(item.rect):
                
                self.x = 3
                self.y=0
            
        
    def draw(self):
        #start/end blocks
        self.start_rect =  pygame.draw.rect(screen,white,(0,0,10,10))
        self.end_rect = pygame.draw.rect(screen,white,(0,315,45,45))
        self.rect = pygame.draw.rect(screen,(red),(self.x,self.y,self.width,self.height))        
        

class Wall:
    def __init__(self,x,y,width,height,move_x=0,move_y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = blue
        self.move_x = move_x

        self.move_y = move_y
        self.rect = pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
    def move(self):
        
        self.x += self.move_x
        self.y += self.move_y

    def draw(self):
        self.rect = pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        

    
#define cursor
curr = Curr()
move_x = 0
move_y = 0

#lists for walls/animations
walls = []
boxs = []
#create walls
wall1 = Wall(10,0,5,300)
walls.append(wall1)
wall2 = Wall(0,310,250,5)
walls.append(wall2)
wall3 = Wall(250,10,5,305)
walls.append(wall3)

box_rect = (15,0,235,310)#boundries of animation box
#create section 1 boxes
wall_box1 = Wall(16,0,40,40,move_y=2)
walls.append(wall_box1)
boxs.append(wall_box1)

wall_box2 = Wall(16,250,25,25,move_x=2)
walls.append(wall_box2)
boxs.append(wall_box2)

wall_box3 = Wall(16,100,30,30,2,2)
walls.append(wall_box3)
boxs.append(wall_box3)

wall_box4 = Wall(100,20,10,10,1,2)
walls.append(wall_box4)
boxs.append(wall_box4)

wall_box5 = Wall(240,0,5,5,move_y=4)
walls.append(wall_box5)
boxs.append(wall_box5)

#section 2 walls

wall4 = Wall(255,100,370,5)
walls.append(wall4)

box_rect2 = (255,0,360,100)
barrs = []
#moving barrieres
barr1 = Wall(280,0,5,60,move_y=1)
walls.append(barr1)
barrs.append(barr1)

barr2 = Wall(330,10,5,60,move_y=1)
walls.append(barr2)
barrs.append(barr2)

barr3 = Wall(390,20,5,60,move_y=1)
walls.append(barr3)
barrs.append(barr3)

barr4 = Wall(450,30,5,60,move_y=1)
walls.append(barr4)
barrs.append(barr4)

barr5 = Wall(510,39,5,60,move_y=1)
walls.append(barr5)
barrs.append(barr5)

barr6 = Wall(570,20,30,10,move_y=4)
walls.append(barr6)
barrs.append(barr6)

#section 3
wall5 = Wall(screen_width-255,105,5,245)
walls.append(wall5)

#rotating wall
wallchange = Wall(screen_width-230,225,250,10)
wallchange.color = (51,255,200)
walls.append(wallchange)
height_change = 5

#section 5
wall6 = Wall(320,120,5,240)
walls.append(wall6)
#movingwalls
movs = []

wallmov1 = Wall(325,250,60,5,move_y=-1)
walls.append(wallmov1)
movs.append(wallmov1)

wallmov2 = Wall(325,200,60,5,move_y = -1)
walls.append(wallmov2)
movs.append(wallmov2)

wallmov3 = Wall(325,150,60,5,move_y = -1)
walls.append(wallmov3)
movs.append(wallmov3)

wallmov4 = Wall(325,300,60,5,move_y = -1)
walls.append(wallmov4)
movs.append(wallmov4)
#moving the other way



wallmov1 = Wall(255,250,65,5,move_y=1)
walls.append(wallmov1)
movs.append(wallmov1)

wallmov2 = Wall(255,200,65,5,move_y = 1)
walls.append(wallmov2)
movs.append(wallmov2)

wallmov3 = Wall(255,150,65,5,move_y = 1)
walls.append(wallmov3)
movs.append(wallmov3)

wallmov4 = Wall(255,300,65,5,move_y = 1)
walls.append(wallmov4)
movs.append(wallmov4)

#final section
block1 = Wall(100,315,5,30)
walls.append(block1)

block2 = Wall(150,330,5,30)
walls.append(block2)

block3 = Wall(50,330,5,30)
walls.append(block3)

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = -curr.speed
                if event.key == K_RIGHT:
                    move_x = curr.speed
                if event.key == K_UP:
                    move_y = -curr.speed
                if event.key == K_DOWN:
                    move_y = curr.speed
        if event.type == KEYUP:
            move_x = 0
            move_y = 0



    #end red section
    pygame.draw.rect(screen,red,(0,315,200,45))

    curr.move(move_x,move_y)
    curr.draw()
    
    for item in walls:
        item.move()
        item.draw()
        #section 1
    for item in boxs:        #animation box
        item.color = green
        #wall bounces
        if item.x <= box_rect[0] or item.x >= box_rect[0]+box_rect[2]-item.width:
            item.move_x *= -1
        if item.y <= box_rect[1] or item.y >= box_rect[1]+box_rect[3]-item.height:
            item.move_y *= -1
       #section 2
    for item in barrs:
        
        item.color = yellow
        if item.y <= box_rect2[1] or item.y >= box_rect2[1]+box_rect2[3]-item.height:
            item.move_y *= -1
       
      #section 3
    if wallchange.height == 110 or wallchange.height == 9 or wallchange.height == -110 or wallchange.height == -9:
        height_change *= -1
    wallchange.height+=height_change

       #section 4
    for item in movs:
        item.color = (204,0,102)
        if item.y <= 125:
            item.y = 365
        if item.y >=366:
            item.y = 126


    if curr.rect.colliderect(curr.end_rect):
        time_end = time.time()
        pygame.quit()
        time = time_end-time_start
        break
    

    
    clock.tick(100)
    
    pygame.display.update()

print "You completed the Improbable Maze in: "+str(time)+" seconds."
name = raw_input("Name: ")
fob = open("The_Improbable_game.txt","a")
fob.write(name+" - "+str(time)+"\n")
fob.close()
print "High score saved in The_improbable_game.txt"



