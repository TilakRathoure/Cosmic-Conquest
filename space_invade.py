import pygame
import random

pygame.init()

gameWindow=pygame.display.set_mode((900,600))
pygame.display.set_caption("Space Invader")


icon=pygame.image.load("space.png")
pygame.display.set_icon(icon)


playerImg=pygame.image.load("spaceship (2).png")

back=pygame.image.load("bg.png")

bullet=pygame.image.load("war.png")




playerX=370
playerY=480

block_update=0.3
playerX_change=0


enemyImg=pygame.image.load("space-ship.png")

enemyX=random.randint(0,836)
enemyY=random.randint(50,150)

enemyChange=0.4

bulletX=0
bulletY=0


def enemy(x,y):
    gameWindow.blit(enemyImg,(x,y))

def player(x,y):
    gameWindow.blit(playerImg,(x,y))
    

def fire(x,y):
    gameWindow.blit(bullet,(x,y))
    
    
state="fire"
    


closewindow=False

white=(255,255,255)


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
                    fire(bulletX,bulletY)
                    state="not"
                
                
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change=0
            else:
                pass
                
    enemyX+=enemyChange
    
    
    
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
        
    bulletY-=2
    
    if bulletY==0:
        state="fire"
        
    fire(bulletX,bulletY)
               
    playerX+=playerX_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
