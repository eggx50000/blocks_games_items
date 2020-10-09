import sys # exit 하기위해서 
import random # 아이탬을 쓰기위해서 
import pygame # 게임을 만들기 위해서 
import math #속도를 측정하기 위해서

from pygame.locals import QUIT, KEYDOWN,K_LEFT,K_RIGHT, Rect, K_SPACE #키보드 입력을 받기위해서

class items(x, y):
    pass
# 블록,패들 , 공
class Block:
    
    def __init__(self, col, rect, speed=0):
        self.col=col
        self.rect=rect
        self.speed=speed
        self.dir=270
        self.score=0
        
    def move(self):        
        self.rect.centerx += math.cos(math.radians(self.dir))\
            * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))\
            * self.speed
        
    def draw(self):
        if self.speed==0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)
class AddScore:
    def __init__(self,rect,y):
        self.rect=rect
        self.y=y
        self.color=(50,250,255)
        
    def draw(self):
        pygame.draw.rect(SURFACE,self.color,self.rect)



        

def tick():   
    global BLOCKS
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_LEFT:
                if PADDLE.rect.centerx-10<50:
                    PADDLE.rect.centerx==50
                else:
                    PADDLE.rect.centerx-=10
            elif event.key==K_RIGHT:
                
                if PADDLE.rect.centerx+10>550:
                    PADDLE.rect.centerx==550
                else:    
                    PADDLE.rect.centerx+=10
                
    if BALL1.rect.centery<1000:
        BALL1.move()

    prevlen=len(BLOCKS)
    BLOCKS=[x for x in BLOCKS 
            if not x.rect.colliderect(BALL1.rect)]
    
    if len(BLOCKS) != prevlen:
        BALL1.dir *= -1
        BALL1.score+=50
        if random.randint(1,100)<=20:
 
            f=AddScore(Rect(random.randint(0,520),0,80,30),5)
            items.append(f)
            
       
        
        

    if PADDLE.rect.colliderect(BALL1.rect):
        BALL1.dir=90+(PADDLE.rect.centerx - BALL1.rect.centerx) \
            / PADDLE.rect.width * 80

    if BALL1.rect.centerx < 0 or BALL1.rect.centerx > 600:
        BALL1.dir=180-BALL1.dir
        
    if BALL1.rect.centery < 0:
        BALL1.dir= -BALL1.dir  

    for i in items:
        i.rect.top += i.y
        if PADDLE.rect.colliderect(i.rect):
            BALL1.score+=100
            u=items.index(i)
            items.pop(u)
        elif BALL1.rect.colliderect(i.rect):
            BALL1.score+=300
            BALL1.dir*=-1
            u=items.index(i)
            items.pop(u)


        
        
pygame.init()

pygame.key.set_repeat(5,5)

SURFACE=pygame.display.set_mode((600, 850))
FPSCLOCK=pygame.time.Clock()
pygame.display.set_caption("blocks")
items=[]
BLOCKS=[]
PADDLE=Block((190,190,190), Rect(300, 750, 100, 30))
BALL1=Block((255,255,255), Rect(0,0,20,20),10)

def main():
    
    myfont=pygame.font.SysFont(None, 80)
    mess_clear=myfont.render("Cleared!", True, (255, 250, 0))
    
    
    fps=50
    colors=[(255,0,0), (12,89,255), (255,255,10),
            (111,222,98), (255,100,100), (149,68,1),(115,255,55)
            ]
    
    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0,5):
            BLOCKS.append(Block(color,  Rect(xpos * 100 + 60, ypos * 50 + 40, 80,30)))       
    while True:
        tick()

        SURFACE.fill((0, 0, 0))
        BALL1.draw()
        PADDLE.draw()
        for i in items:
            i.draw()
        for block in BLOCKS:
            block.draw()
           
            
        if len(BLOCKS) ==0:
            mess_clear=myfont.render("score is {0}".format(BALL1.score + 300), True, (255, 250, 0))
            SURFACE.blit(mess_clear, (200, 400))
            
        if BALL1.rect.centery > 800 and len(BLOCKS) > 0:
            mess_over=myfont.render("score is {0}".format(BALL1.score-200), True, (255, 250, 0))
            SURFACE.blit(mess_over, (150, 400))

        pygame.display.update()
        FPSCLOCK.tick(fps)


if __name__ == '__main__':
    
    main()
