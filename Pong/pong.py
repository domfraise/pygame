import pygame, sys
from pygame.locals import *
import time
import math
import random
pygame.init()

class Player():
    def __init__(self):
        #constants
        self.x,self.y = 16,screen_height/2-50
        self.speed = 0
        self.pad_width,self.pad_height = 10,80
        self.score = 0
        self.scoreFont = pygame.font.Font(None,60)
       
    def scoring(self):
        wining_text = self.scoreFont.render("<-- Winner!!!",1,white)
        score_text = self.scoreFont.render(str(self.score),1,white)
        screen.blit(score_text,(32,16))
        if self.score >= 10:
            screen.blit(wining_text,(center[0]-100,300))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    def movement(self):
        
        self.y+=self.speed
        if self.y <=0:
            self.y = 0
        elif self.y >= screen_height - self.pad_height:
            self.y = screen_height-self.pad_height

    def draw(self):
        global curs1
        curs1 = pygame.draw.rect(screen,white,(40,self.y,self.pad_width,self.pad_height))

class Enemy():
    def __init__(self):
        self.x,self.y = 626,screen_height/2-50
        self.speed = 0
        self.pad_width,self.pad_height = 10,80
        self.score = 0
        self.scoreFont = pygame.font.Font(None,60)
        
    def scoring(self):
        score_text = self.scoreFont.render(str(self.score),1,white)
        wining_text = self.scoreFont.render("Winner!!! -->",1,white)
        screen.blit(score_text,(600,16))
        if self.score >= 10:
            screen.blit(wining_text,(center[0]-100,300))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
            
                                            
    def movement(self):
        self.y+=self.speed
        if self.y <=0:
            self.y = 0
        elif self.y >= screen_height - self.pad_height:
            self.y = screen_height-self.pad_height

    def draw(self):
        global curs2
        curs2 = pygame.draw.rect(screen,white,(600,self.y,self.pad_width,self.pad_height))


class Ball():
    def __init__(self):
        self.x,self.y = screen_width/2,screen_height/2
        self.speed_x = -3
        self.speed_y = 3
        self.size = 8

    def movement(self):
        self.x +=self.speed_x
        self.y+= self.speed_y

        #wall collisions
        if self.y <= 0 :
            self.speed_y*=-1
            
        elif self.y >=screen_height-self.size:
            self.speed_y *= -1
            

        if self.x <=0:
            self.x,self.y = center
            self.speed_x = 3
            enemy.score +=1
            time.sleep(2)
        elif self.x >= screen_width - self.size:
            self.x,self.y = center
            self.speed_x = -3
            player.score += 1
            time.sleep(2)
        elif curs2.collidepoint(self.x,self.y):
            self.speed_x*=-1
            bounce.play()
            
        elif curs1.collidepoint(self.x,self.y):
            self.speed_x*=-1
            bounce.play()
            

        
    def draw(self):
        pygame.draw.rect(screen,white,(self.x,self.y,8,8))
            


screen=pygame.display.set_mode((640,360))
pygame.display.set_caption("PONG!")

black = (0,0,0)
white = (250,250,250)
red = (250,0,0)
green = (0,250,0)
blue = (0,0,250)
screen_height = 360
screen_width = 640

center = (320,180)

win = False
player = Player()
enemy = Enemy()
ball = Ball()


clock = pygame.time.Clock() 
curs1 = pygame.draw.rect(screen,white,(40,screen_height/2,player.pad_width,enemy.pad_height))
curs2 = pygame.draw.rect(screen,white,(600,screen_height/2,enemy.pad_width,enemy.pad_height))
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.speed = -10
            if event.key == pygame.K_s:
                player.speed = 10
    
            if event.key == pygame.K_UP:
                enemy.speed = -10
            if event.key == pygame.K_DOWN:
                enemy.speed = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                enemy.speed = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.speed = 0
            
        
          
    pygame.display.update()
    screen.fill(black)
    player.draw()
    enemy.draw()
    ball.movement()
    player.movement()
    enemy.movement()
    ball.draw()
    
    player.scoring()
    
    enemy.scoring()
    
    clock.tick(80)
    pygame.display.update()
    if win == True:
        break
pygame.mixer.music.stop()
    
