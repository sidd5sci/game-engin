import pygame
import time,math,random
from OpenGL.GL import  *
from OpenGL.GLU import  *


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
colors =(30,191,56),(26,130,38),(15,77,22),(245,5,5),(145,3,3),(255,46,46),(10,10,10),(210,70,20)

# create the wx windows

# object vertex
#vertex = (1.000000 ,-1.000000, -1.000000),( 1.000000, -1.000000, 1.000000),( -1.000000 ,-1.000000 ,1.000000),( -1.000000, -1.000000 ,-1.000000),( 1.000000, 1.000000, -0.999999),( 0.999999 ,1.000000, 1.000001),( -1.000000, 1.000000 ,1.000000),( -1.000000, 1.000000, -1.000000)
edges = (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)
faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
verts = [1.000000 ,-1.000000, -1.000000],[ 1.000000, -1.000000, 1.000000],[ -1.000000 ,-1.000000 ,1.000000],[ -1.000000, -1.000000 ,-1.000000],[ 1.000000, 1.000000, -0.999999],[ 0.999999 ,1.000000, 1.000001],[ -1.000000, 1.000000 ,1.000000],[ -1.000000, 1.000000, -1.000000]

'''
==========================================
    object classes
==========================================
'''  
class cube:
    def __init__(self,pos):
        self.vertex = [1.000000 ,-1.000000, -1.000000],[ 1.000000, -1.000000, 1.000000],[ -1.000000 ,-1.000000 ,1.000000],[ -1.000000, -1.000000 ,-1.000000],[ 1.000000, 1.000000, -0.999999],[ 0.999999 ,1.000000, 1.000001],[ -1.000000, 1.000000 ,1.000000],[ -1.000000, 1.000000, -1.000000]
        self.edges = [0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]
        self.faces = [0,1,2,3],[4,5,6,7],[0,1,5,4],[2,3,7,6],[0,3,7,4],[1,2,6,5]
        self.translate3d()
    def translate3d(self,pos):
        dx,dy,dz = pos
        for i in range(0,len(self.vertex)):
            self.vertex[i][0] += dx
            self.vertex[i][1] += dy
            self.vertex[i][2] += dz
    def rotate3d(axis,dtheta):
        c,s = math.cos(dtheta),math.sin(dtheta)
        if axis == 'x':
            for i in range(0,len(verts)):
                temp = verts[i][1]
                verts[i][1] =  verts[i][1]*c + verts[i][2]*s
                verts[i][2] =  temp*s + verts[i][2]*c
        if axis == 'y':
            for i in range(0,len(verts)):
                temp = verts[i][0]
                verts[i][0] =  verts[i][0]*c - verts[i][2]*s
                verts[i][2] = temp*s + verts[i][2]*c
        if axis == 'z':
            for i in range(0,len(verts)):
                temp = verts[i][0]
                verts[i][0] =  verts[i][0]*c + verts[i][1]*s
                verts[i][1] = -temp*s + verts[i][1]*c
    #def scale3d(self):
'''
==========================================
    display function
==========================================
'''    
def display(mode,_object_):
    if mode == 'vertex':
       for x,y,z in vertex:
           z+=5
           f = 200/z
           x,y = x*f,y*f
           pygame.draw.circle(screen,BLACK,(cx+int(x),cy+int(y)),3)
    if mode == 'edge':
        # put the cube on screen edge
        for edge in edges:
            points = []
            for x,y,z,in (verts[edge[0]],verts[edge[1]]):
                x -=cam.pos[0]
                y -=cam.pos[1]
                z +=cam.pos[2]
                f = 200/z
                    
                x,y = x*f,y*f
                points +=  [(cx+int(x),cy+int(y))]

            pygame.draw.line(screen,WHITE,points[0],points[1],1)
    if mode == 'face':
        # convert 3d vertex to 2d screen coords
        screen_verts=[]
        for x,y,z in verts:
            x-= cam.pos[0]; y-=cam.pos[1];z+=cam.pos[2]
            f= 200/z
            x,y = x*f,y*f
            screen_verts += [(cx+int(x),cy+int(y))]
        # filling the vertex in face list
        face_list =[]
        for face in faces:
            vertex_list = []
            #print face
            for v in face:
                 #print v,verts[v]
                 vertex_list.append(screen_verts[v])
            face_list.append(vertex_list)
        # displaying the cube 
        for i in range(0,len(face_list)):
            print face_list[i],"\n\n"
            pygame.draw.polygon(screen,colors[i],face_list[i])

'''
==========================================

==========================================
'''           
def rotate3d(axis,theta):

    c,s = math.cos(theta),math.sin(theta)
    
    if axis == 'x':
        for i in range(0,len(verts)):
            temp = verts[i][1]
            verts[i][1] =  verts[i][1]*c + verts[i][2]*s
            verts[i][2] =  temp*s + verts[i][2]*c
    if axis == 'y':
        for i in range(0,len(verts)):
            temp = verts[i][0]
            verts[i][0] =  verts[i][0]*c - verts[i][2]*s
            verts[i][2] = temp*s + verts[i][2]*c
    if axis == 'z':
        for i in range(0,len(verts)):
            temp = verts[i][0]
            verts[i][0] =  verts[i][0]*c + verts[i][1]*s
            verts[i][1] = -temp*s + verts[i][1]*c

def mouseTracker(LastPosition):
    CurrentPosition = pygame.mouse.get_pos()
    dx = CurrentPosition[0] -LastPosition[0]
    dy = CurrentPosition[1] -LastPosition[1]
    return dx,dy
def translate3d(pos):
    dx,dy,dz = pos
    
    for i in range(0,len(verts)):

       verts[i][0] +=  dx
       verts[i][1] +=  dy   
       verts[i][2] +=  dz
       
class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
    def update(self,dt,key):
        s = dt*10
        if key[pygame.K_q]: self.pos[2]-=s
        if key[pygame.K_e]: self.pos[2]+=s

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
    screen.fill(BLACK)
    
    

    # convert 3d vertex to 2d screen coords
    screen_verts=[]
    for x,y,z in verts:
        x-= cam.pos[0]; y-=cam.pos[1];z+=cam.pos[2]
        f= 200/z
        x,y = x*f,y*f
        screen_verts += [(cx+int(x),cy+int(y))]
    # filling the vertex in face list
    face_list =[]
    for face in faces:
        vertex_list = []
        #print face
        for v in face:
             #print v,verts[v]
             vertex_list.append(screen_verts[v])
        face_list.append(vertex_list)
    # displaying the cube 
    for i in range(0,len(face_list)):
        print face_list[i],"\n\n"
        pygame.draw.polygon(screen,colors[i],face_list[i])
    pygame.display.flip()

    
    # put the cube on screen edge
    for edge in edges:
        points = []
        for x,y,z,in (verts[edge[0]],verts[edge[1]]):
            x -=cam.pos[0]
            y -=cam.pos[1]
            z +=cam.pos[2]
            f = 200/z
                
            x,y = x*f,y*f
            points +=  [(cx+int(x),cy+int(y))]

        pygame.draw.line(screen,WHITE,points[0],points[1],1)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_t]:
        dx = input("\nEnter the translation in x:")
        dy = input("\nEnter the translation in y:")
        dz = input("\nEnter the translation in z:")
        translate3d((dx,dy,dz))
    if key[pygame.K_r]:
        axis = input("\nEnter the axis :")
        
        theta = math.pi/10
        rotate3d(axis,theta)

    if key[pygame.K_v]:
        print verts
    if key[pygame.K_m]:
       lpos = pygame.mouse.get_pos()
       print mouseTracker(lpos)
       
    cam.update(dt,key)






