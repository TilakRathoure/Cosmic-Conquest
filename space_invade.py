import pygame

pygame.init()

gameWindow=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")


icon=pygame.image.load("space.png")
pygame.display.set_icon(icon)


playerImg=pygame.image.load("spaceship (2).png")
playerX=370
playerY=480

block_update=0.3
playerX_change=0

enemyImg=pygame.image.load("space-ship.png")

enemyX=0
enemyY=0


def enemy(x,y):
    gameWindow.blit(enemyImg,(x,y))





def player(x,y):
    gameWindow.blit(playerImg,(x,y))
    


closewindow=False

white=(255,255,255)


while not closewindow:
    gameWindow.fill(white)
    for event in pygame.event.get():
        if  event.type==pygame.QUIT:
            closewindow=True
            pygame.quit()
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-block_update
                
            if event.key==pygame.K_RIGHT:
                playerX_change=block_update
                
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change=0
                
    if playerX<=0:
        playerX=0
    
    elif playerX>=736:
        playerX=736
               
    playerX+=playerX_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
