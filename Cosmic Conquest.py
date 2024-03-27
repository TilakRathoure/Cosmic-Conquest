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


setimg=pygame.image.load

enemyImg=[setimg("./images/space-ship.png"),setimg("./images/space-ship.png"),setimg("./images/spaceship (3).png"),setimg("./images/spaceship (3).png"),setimg("./images/ufo.png"),setimg("./images/ufo.png")]
enemyX=[]
enemyY=[]
enemyChange=[]
numberofenemy=6

for i in range(numberofenemy):
    enemyChange.append(0.4)
    enemyX.append(random.randint(0,836))
    enemyY.append(random.randint(0,50))

bulletX=0
bulletY=0

state="fire"
closewindow=False
white=(255,255,255)


Score=19

fonnt=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10


def showscore(x):
    score1=fonnt.render("Score : "+str(x),True,white)
    gameWindow.blit(score1,(15,20))
    



def enemy(x,y,i):
    gameWindow.blit(enemyImg[i],(x,y))

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
    
def youlost():
    lost=pygame.font.Font('freesansbold.ttf',64).render("Game Over! You Lost",True,white)
    gameWindow.blit(lost,(100,250))
    
def youwon():
    lost=pygame.font.Font('freesansbold.ttf',64).render("Good! You Won",True,white)
    gameWindow.blit(lost,(160,250))
    

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
    
    for i in range(numberofenemy):
        
        
        if enemyX[i]>836:
            enemyX[i]=836
            enemyChange[i]=-0.4
            enemyY[i]+=20
    
        elif enemyX[i]<0:
            enemyX[i]=0
            enemyChange[i]=0.4
            enemyY[i]+=20
            
        if enemyY[i]>=430:
            for j in range(numberofenemy):
                enemyY[j]=2000
                youlost()
            break
        
        enemyX[i]+=enemyChange[i]
        check=collision(enemyX[i],enemyY[i],bulletX,bulletY)
    
        if check==True:
            Score+=1
            bulletY=-100
            bulletX=-100
            state="fire"
            enemyY[i]=-64
        
        enemy(enemyX[i],enemyY[i],i)
        
               
                
    if playerX<=0:
        playerX=0
    
    elif playerX>=836:
        playerX=836
        
    
    if bulletY<=0:
        state="fire"
                  
    playerX+=playerX_change
    bulletY-=1.5
    
    if Score==20:
        for i in range(numberofenemy):
            enemyY[i]=-200000
        youwon()
    
    
    
    showscore(Score)
    player(playerX,playerY)
    fire(bulletX,bulletY)
    pygame.display.update()
