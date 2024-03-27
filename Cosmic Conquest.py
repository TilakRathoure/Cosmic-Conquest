import pygame
import random
import math

pygame.init()

gameWindow=pygame.display.set_mode((900,600))
pygame.display.set_caption("Cosmic Conquest  ")


icon=pygame.image.load("./images/space.png")
pygame.display.set_icon(icon)


playerImg=pygame.image.load("./images/spaceship (2).png")

back=pygame.image.load("./images/bg.png")

bullet=pygame.image.load("./images/war.png")




playerX=370
playerY=480

block_update=0.3
playerX_change=0


enemyImg=pygame.image.load("./images/space-ship.png")

enemyX=random.randint(0,836)
enemyY=random.randint(50,150)

enemyChange=0.4

bulletX=0
bulletY=0

state="fire"
closewindow=False
white=(255,255,255)


Score=0

fonnt=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10


def showscore(x):
    score1=fonnt.render("Score : "+str(x),True,white)
    gameWindow.blit(score1,(15,20))
    



def enemy(x,y):
    gameWindow.blit(enemyImg,(x,y))

def player(x,y):
    gameWindow.blit(playerImg,(x,y))
    

def fire(x,y):
    gameWindow.blit(bullet,(x,y))
    
def collision(x1,y1,x2,y2):
    distance=math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
    
    if distance<=32:
        return True
    else:
        return False
    
    
    

while not closewindow:
    gameWindow.fill(white)
    gameWindow.blit(back,(0,0))
    for event in pygame.event.get():
        if  event.type==pygame.QUIT:
            closewindow=True
            pygame.quit()
        
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT:
                playerX_change=-block_update
                
            if event.key==pygame.K_RIGHT:
                playerX_change=block_update
                
                
            if event.key==pygame.K_SPACE:
                if state=="fire":
                    bulletX=playerX+16
                    bulletY=playerY
                    state="not"
                
                
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                playerX_change=0
    
    
    
    if enemyX>836:
        enemyX=836
        enemyChange=-0.4
        enemyY+=20
    
    elif enemyX<0:
        enemyX=0
        enemyChange=0.4
        enemyY+=20
        
               
                
    if playerX<=0:
        playerX=0
    
    elif playerX>=836:
        playerX=836
        
    
    if bulletY<=0:
        state="fire"
                  
    playerX+=playerX_change
    enemyX+=enemyChange
    bulletY-=1.5
    
    check=collision(enemyX,enemyY,bulletX,bulletY)
    if check==True:
        Score+=1
        bulletY=0
        bulletX=0
        state="fire"
    
    
    showscore(Score)
    player(playerX,playerY)
    fire(bulletX,bulletY)
    enemy(enemyX,enemyY)
    pygame.display.update()
