import pygame
import time,math,random


# initilize the pygame
pygame.init()
# screen height and width
width ,height = 600,400
# center of the screen 
cx,cy = width/2,height/2
# initilize the screen 
screen = pygame.display.set_mode((width,height))
# initilize the clock
clock = pygame.time.Clock()
dt = 0.015
# colors 
WHITE = (254,254,254)
BLACK = (0,0,0)
RED = (254,0,0)
BLUE = (0,0,254)
GREEN = (0,254,0)
# object vertex
vertex = (1.000000 ,-1.000000, -1.000000),( 1.000000, -1.000000, 1.000000),( -1.000000 ,-1.000000 ,1.000000),( -1.000000, -1.000000 ,-1.000000),( 1.000000, 1.000000, -0.999999),( 0.999999 ,1.000000, 1.000001),( -1.000000, 1.000000 ,1.000000),( -1.000000, 1.000000, -1.000000)
edges = (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)

class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
    def update(self,dt,key):
        s = dt*10
        if key[pygame.K_q]: self.pos[2]-=s;print "q"
        if key[pygame.K_e]: self.pos[2]+=s;print "e"

        if key[pygame.K_w]: self.pos[1]+=s
        if key[pygame.K_s]: self.pos[1]-=s

        if key[pygame.K_a]: self.pos[0]-=s
        if key[pygame.K_d]: self.pos[0]+=s

cam =Cam((0,0,-5))

# initilize the main loop
while True:
    # setting the smallest time variation 
    dt = float(clock.tick(60))/1000
    clock.tick(60) 
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type==pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)

    # Fill the background color to screen as white
    screen.fill(WHITE)
    
    for x,y,z in vertex:
      
      z+=5
      f = 200/z
      x,y = x*f,y*f
   
      pygame.draw.circle(screen,BLACK,(cx+int(x),cy+int(y)),3)

    for edge in edges:
        points = []            
        for x,y,z,in (vertex[edge[0]],vertex[edge[1]]):
            x -=cam.pos[0]
            y -=cam.pos[1]
            z +=cam.pos[2]
            f = 200/z

            x,y = x*f,y*f
            points +=  [(cx+int(x),cy+int(y))]
        pygame.draw.line(screen,BLACK,points[0],points[1],1)

            
    pygame.display.flip()
    
    key = pygame.key.get_pressed()
    
    cam.update(dt,key)
    print dt





