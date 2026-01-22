import pygame
pygame.init()
screen=pygame.display.set_mode((600, 600))
pygame.display.set_caption("Name of window")
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
idle=[]
jump=[]
flip=False
count=0
flag=False
clock=pygame.time.Clock()
for i in range(1, 10):
    image=pygame.image.load("/Users/vishay/Downloads/png/Idle ("+str(i)+").png")
    idle.append(image)
for i in range(1, 13):
    image=pygame.image.load("/Users/vishay/Downloads/png/Jump ("+str(i)+").png")
    jump.append(image)


while True:
    screen.fill((0,0,0))
    clock.tick(30)
    if flip==True:
        fimage=pygame.transform.flip(jump[count], True, False)
        screen.blit(fimage,(0,0))
    else:
        screen.blit(jump[count], (0, 0))
    count +=1
    if count==len(idle):
        count=0
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                flip=True
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                flag=True
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                flag=False
        if event.type==pygame.QUIT:
            print("bye")
            pygame.quit()
            exit()
    pygame.display.update()
import pygame
import time
pygame.init()
screen=pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Name of window")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
right=False
left=False
run=[]
idle=[]
number=0
count=0
x=0
y=0

     
for a in range(1, 9):
        image=pygame.image.load("/Users/vishay/Downloads/png/Run ("+str(a)+").png")
        run.append(image)
for b in range(1,11):
    imoge=pygame.image.load("/Users/vishay/Downloads/png/Idle ("+str(b)+").png")
    idle.append(imoge)
while True:
    screen.fill((0,0,0))
    clock=pygame.time.Clock()
    clock.tick(30)
    if right==True:
        screen.blit(run[count], (x, y))
        x=x+10
    elif left==True:
        fimage=pygame.transform.flip(run[count], True, False)
        x=x-10
        screen.blit(fimage, (x,y))
    else:
         screen.blit(idle[number], (x, y))
    number += 1
    if number==len(idle):
         number=0
         
         
    
    count += 1
    if count==len(run):
         count=0
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                  right=True
            if event.key==pygame.K_LEFT:
                left=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                  right=False
            if event.key==pygame.K_LEFT:
                left=False
        
        if event.type==pygame.QUIT:
            print("bye")
            pygame.quit()
            exit()
    pygame.display.update()
import pygame
import time
pygame.init()
screen=pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Name of window")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
attack=[]
x=300
y=300
count=0
idle=[]
jump=[]
jumpattack=[]
run=[]
jumpcount=0
rflag=False
lflag=False
jflag=False
jaflag=False
iflag=False
aflag=False

bg=pygame.image.load("/Users/vishay/Downloads/graveyardtilesetnew/png/BG.png")
bg=pygame.transform.scale(bg, (1000, 600))
for a in range(0, 10):
     f=pygame.image.load("/Users/vishay/Downloads/png 2/Attack__00"+str(a)+".png")
     f=pygame.transform.scale(f, (200, 200))
     attack.append(f)
for b in range(0, 10):
     f=pygame.image.load("/Users/vishay/Downloads/png 2/Idle__00"+str(b)+".png")
     f=pygame.transform.scale(f, (100, 200))
     idle.append(f)
for c in range(0, 10):
     f=pygame.image.load("/Users/vishay/Downloads/png 2/Jump__00"+str(c)+".png")
     f=pygame.transform.scale(f, (150, 200))
     jump.append(f)
for d in range(0, 10):
     f=pygame.image.load("/Users/vishay/Downloads/png 2/Jump_Attack__00"+str(d)+".png")
     f=pygame.transform.scale(f, (150, 200))
     jumpattack.append(f)
for e in range(0, 10):
     f=pygame.image.load("/Users/vishay/Downloads/png 2/Run__00"+str(e)+".png")
     f=pygame.transform.scale(f, (150, 200))
     run.append(f)
while True:
     gravity=True
     screen.blit(bg, (0, 0))
     clock=pygame.time.Clock()
     clock.tick(30)
     if y>=400:
         gravity=False
     if gravity==True and jflag==False:
         y=y+15
     if rflag==True:
        screen.blit(run[count], (x, y))
        x=x+10
     elif lflag==True:
        flip=pygame.transform.flip(run[count], True, False)
        x=x-10
        screen.blit(flip, (x,y))
     elif aflag==True:
         screen.blit(attack[count], (x,y))
     elif jflag==True: 
         screen.blit(jump[count], (x,y))
         jumpcount=jumpcount+1
     elif jaflag==True:
         screen.blit(jumpattack[count],(x,y))
     else:
         screen.blit(idle[count],(x,y))
     count += 1
     if count==9:
         count=0
     if jumpcount<=5:
         y -= 10
     else:
         jflag=False 

     for event in pygame.event.get():
          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_f:
                 aflag=True
               elif event.key==pygame.K_UP:
                 jflag=True
                 jumpcount=0
               elif jflag==True and event.key==pygame.K_f:
                 jaflag=True
               elif event.key==pygame.K_LEFT:
                 lflag=True
               elif event.key==pygame.K_RIGHT:
                 rflag=True
          if event.type==pygame.KEYUP:
               if event.key==pygame.K_f:
                 aflag=False
               elif jflag==True and event.key==pygame.K_f:
                 jaflag=False
               elif event.key==pygame.K_LEFT:
                 lflag=False
               elif event.key==pygame.K_RIGHT:
                 rflag=False
              
          if event.type==pygame.QUIT:
               print("bye")
               pygame.quit()
               exit()
     pygame.display.update()

