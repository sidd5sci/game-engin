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
colors =(100,200,254),(254,70,50),(100,100,30),(20,40,50),(40,50,10),(20,60,40),(10,10,10),(210,70,20)
# object vertex
vertex = (1.000000 ,-1.000000, -1.000000),( 1.000000, -1.000000, 1.000000),( -1.000000 ,-1.000000 ,1.000000),( -1.000000, -1.000000 ,-1.000000),( 1.000000, 1.000000, -0.999999),( 0.999999 ,1.000000, 1.000001),( -1.000000, 1.000000 ,1.000000),( -1.000000, 1.000000, -1.000000)
edges = (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)
faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5) 
def rotate2d(pos,rad):
    x,y = pos
    s,c = math.sin(rad),math.cos(rad)
    return x*c-y*s,y*c+x*s
def translate2d(pos):
    dx,dy,dz = pos
    for x,y,z in vertex:
        #print x,y,z,"|"
        x += dx
        y += dy 
        z += dz
    
    
    
class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
    def  events(self,event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            x,y = float(x/200),float(y/200)
            self.rot[0]+=y; self.rot[1]+=x
        if event.type == pygame.KEYDOWN:
            print "hello"
    def update(self,dt,key):
        s = dt*10
        if key[pygame.K_q]: self.pos[2]-=s
        if key[pygame.K_e]: self.pos[2]+=s
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        if key[pygame.K_w]: self.pos[0]+=x;self.pos[2]+=y
        if key[pygame.K_s]: self.pos[0]-=x;self.pos[2]-=y

        if key[pygame.K_a]: self.pos[0]-=y;self.pos[2]+=x
        if key[pygame.K_d]: self.pos[0]+=y;self.pos[2]-=x

cam =Cam((0,0,-5))

pygame.event.get()
pygame.mouse.get_rel()
pygame.mouse.set_visible(1)

#pygame.event.set_grab(1) # mouse will remain within the screen

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
        if event.type == pygame.KEYDOWN :
           if event.key == pygame.K_ESCAPE:
               pygame.quit();sys.exit()
        cam.events(event)
            
    # Fill the background color to screen as white
    screen.fill(WHITE)
    
    
    for edge in edges:
        points = []            
        for x,y,z in (vertex[edge[0]],vertex[edge[1]]):
            x -=cam.pos[0]
            y -=cam.pos[1]
            z +=cam.pos[2]

            x,z = rotate2d((x,z),cam.rot[1])
            y,z = rotate2d((y,z),cam.rot[1])
            
            f = 200/z          
            x,y = x*f,y*f
            points +=  [(cx+int(x),cy+int(y))]
        pygame.draw.line(screen,BLACK,points[0],points[1],1)

    vertex_list=[];screen_coords = []
    
    for x,y,z in vertex:
        x-= cam.pos[0]; y-=cam.pos[1];z-=cam.pos[2]
        x,z = rotate2d((x,z),cam.rot[1])
        y,z = rotate2d((y,z),cam.rot[0])      
        vertex_list+= [(x,y,z)]
        f= 200/z
        x,y = x*f,y*f
        screen_coords += [(cx+int(x),cy+int(y))]
    face_list = [];face_color=[];depth= []

    for face in faces:
        on_screen = False
        for i in face:
            if vertex_list[i][2]>0: on_screen =True;break
        if on_screen :
            coords = [screen_coords[i] for i in face]
            face_list +=[coords]
            face_color+= [colors[faces.index(face)]]
            depth +=[sum(sum(j[i] for j in vertex_list)**2 for i in range(3) )]            
    order =sorted(range(len(face_list)),key = lambda i:depth[i],reverse = 0)

    for i in order:
        pygame.draw.polygon(screen,face_color[i],face_list[i])

    pygame.display.flip()
    
    key = pygame.key.get_pressed()
    translate2d((1,1,0))
    cam.update(dt,key)
    




