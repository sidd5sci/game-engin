import pygame
from pygame.locals import *
import time,math,random
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

def init(mode):
    if mode == 'openGL':
        
        # initilize the screen
        screen = pygame.display.set_mode((width,height),OPENGL|DOUBLEBUF)
    
        gluPerspective(45, width/height, 0.1,100.0)
        glTranslate(0,0,-35)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        return screen
    else:
        
        # initilize the screen
        screen = pygame.display.set_mode((width,height))
        return screen

# initilize the pygame
pygame.init()
# screen height and width
width ,height = 600,400
# center of the screen | environment cooords
cx,cy,cz = width/2,height/2, -5
# loading the icon  
pygame.display.set_icon(pygame.image.load('Icon.png'))
# init the name of the window
pygame.display.set_caption("Game engin - testing 2017")
# graphics mode
Gmode = 'openGL' 
screen = init(Gmode)
'''
==========================================
    Global constants
==========================================
'''
# universal gravitational constant
G = 6.67408e-11 # m3 kg-1 s-2
# earth mass
MassEearth = 6e24  # kg
# mass
# initilize the clock
clock = pygame.time.Clock()
'''
==========================================
    vector class
==========================================
'''
class vector(object):
    def __init__(self,x,y,z):
        # vector components
        self.x,self.y,self.z = x,y,z
        # some usefull quantities
        self.mag = 0.0
        self.alpha = 0.0
        self.beta = 0.0
        self.gama = 0.0
        self.cal_mag()
    def asign(self,x,y,z):
        self.x,self.y,self.z = x,y,z
        self.cal_mag()
    def cal_mag(self):
        return  math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    def add(self,vctr):
        self.x += vctr.x; self.y += vctr.y; self.z += vctr.z
    def sub(self,vctr):
        self.x += vctr.x; self.y += vctr.y; self.z += vctr.z
    def multS(self,vctr):
        self.x *= vctr.x; self.y *= vctr.y; self.z *= vctr.z
    def multV(self,vctr):
        self.x *= (self.y*vctr.z - self.z*vctr.y)
        self.z *= (self.x*vctr.z - self.z*vctr.x)
        self.z *= (self.x*vctr.z - self.y*vctr.x)
    def divide(self,qt):# dividing vector by scaler quantity
        self.x /= qt; self.y /= qt; self.z /= qt
    def mult(self,qt): # multiply the vector with scaler quantity
        self.x *= qt; self.y *= qt; self.z *= qt
    def isnull(self):
        # check the vector is null/zero or not
        if self.x == 0 and self.y == 0 and self.z == 0:
            return True
        else:
            return False
    
    def get(self):
        return self.x,self.y,self.z
'''
==========================================
    physics class
==========================================
'''
class physics(object):
    
    def __init__(self,pos):
        
        # mass
        self.mass = 1.0 # kg
        # motion physics / newton physics
        self.pos = list(pos)
        self.velocity = vector(0,0,0)
        self.acc = vector(0,0,0)
        self.force = vector(0,0,0)
        self.time = 0.0
        self.dt = 0.0015
        # material physics
        self.IR = 0.0
        self.rigidity = 0.0
        self.color = []
    def applyForce(self,force):
        # adding force to object
        self.force.add(force)
        # dividing force by mass of object
        self.force.divide(self.mass)
        self.acc.add(self.force)
        # multipling the acc to delta time
        self.acc.mult(self.dt)
        self.velocity.add(self.acc)
    def RealTimeForces(self,earthMass,dist):
        gravitation = (G * self.mass * earthMass)/ (dist**2)
        gForce = vector(0,-1,0)
        gForce.mult(gravitation)
        self.applyForce(gForce)
    def applyG(self):
        g = vector(0,-9.8,0)
        self.applyAcc(g)
    def applyAcc(self,acc):
        self.acc.add(acc)
        # multipling the acc to delta time
        self.acc.mult(self.dt)
        self.velocity.add(self.acc)
    def Collision(self,_object_):
        pass
'''
==========================================
    camera class
==========================================
'''          
class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0),center=(0,0,0)):
        self.pos = list(pos)   #The sphere's center
        self.rot = list(rot)   #The spherical coordinates' angles (degrees).
        self.radius = 3.0      #The sphere's radius
        self.center = list(center)
    def update(self,dt,key):
        s = dt*10
        if key[pygame.K_q]: self.pos[2] -= s
        if key[pygame.K_e]: self.pos[2] += s

        if key[pygame.K_w]: self.pos[1] += s
        if key[pygame.K_s]: self.pos[1] -= s

        if key[pygame.K_a]: self.pos[0] -= s
        if key[pygame.K_d]: self.pos[0] += s        
    def updateGL(self,mouse_buttons,mouse_rel,key):
        if mouse_buttons[0]:
            self.rot[0] += mouse_rel[0]
            self.rot[1] += mouse_rel[1]
        s = 0.015*10
        if key[pygame.K_q]: self.pos[2] -= s
        if key[pygame.K_e]: self.pos[2] += s
'''
==========================================
    colors class
==========================================
'''  
class colors(object):
    def __init__(self):
        self.WHITE = (254,254,254)
        self.BLACK = (0,0,0)
        self.RED = (254,0,0,6)
        self.BLUE = (0,0,254)
        self.GREEN = (0,254,0)
        self.GRAY = (100,100,100)
        self.YELLOW = (254,254,0)
        self.MAGENTA = (254,0,254)


'''
==========================================
    object classes
==========================================
'''

class Cube(physics):
    def __init__(self,pos):
        super(Cube,self).__init__(pos)
        self.vertex = [1.000000 ,-1.000000, -1.000000],[ 1.000000, -1.000000, 1.000000],[ -1.000000 ,-1.000000 ,1.000000],[ -1.000000, -1.000000 ,-1.000000],[ 1.000000, 1.000000, -0.999999],[ 0.999999 ,1.000000, 1.000001],[ -1.000000, 1.000000 ,1.000000],[ -1.000000, 1.000000, -1.000000]
        self.edges = [0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]
        self.faces = [0,1,2,3],[4,5,6,7],[0,1,5,4],[2,3,7,6],[0,3,7,4],[1,2,6,5]
        self.translate3d(pos)
        
    def translate3d(self,pos):
        dx,dy,dz = pos
        if dx!= 0 or dy!= 0 or dz!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += dx
                self.vertex[i][1] += dy
                self.vertex[i][2] += dz
                
    def setPos3d(self,pos):
        pos = (-self.pos[0],-self.pos[1],-self.pos[2])
        self.translate3d(pos)
        print self.pos,'\n'
    def rotate3d(self,axis,dtheta,radius = 1):
        c,s = math.cos(dtheta),math.sin(dtheta)
        if axis == 'x':
            for i in range(0,len(self.vertex)):
                temp = self.vertex[i][1]
                self.vertex[i][1] =  radius*self.vertex[i][1]*c - radius*self.vertex[i][2]*s
                self.vertex[i][2] =  radius*temp*s + radius*self.vertex[i][2]*c
        if axis == 'y':
            for i in range(0,len(self.vertex)):
                temp = self.vertex[i][0]
                self.vertex[i][0] =  self.vertex[i][0]*c - self.vertex[i][2]*s
                self.vertex[i][2] = temp*s + self.vertex[i][2]*c
        if axis == 'z':
            for i in range(0,len(self.vertex)):
                temp = self.vertex[i][0]
                self.vertex[i][0] =  self.vertex[i][0]*c + self.vertex[i][1]*s
                self.vertex[i][1] = -temp*s + self.vertex[i][1]*c
    def scale3d(self,scale):
        sx,sy,sz = scale
        for i in range(0,len(self.vertex)):
            self.vertex[i][0] += self.vertex[i][0]*sx
            self.vertex[i][1] += self.vertex[i][1]*sy
            self.vertex[i][2] += self.vertex[i][2]*sz 
'''
==========================================
    global variables
==========================================
'''    
color = colors()
cam =Cam((-1,0,-40))
cube1 = Cube((0,0,0))
cube2 = Cube((5,0,0))
cube3 = Cube((5,-10,-3))
f = vector(-0.5,0,-0)
dt = 0.015
'''
==========================================
   global functions
==========================================
'''
def coords():
    #Start drawing lines.  Each subsequent pair of glVertex*() calls will draw one line.
    glBegin(GL_LINES)
    #Change the color to red.  All subsequent geometry we draw will be red.
    glColor3f(1,0,0)
    #Make two vertices, thereby drawing a (red) line.
    glVertex(0,0,0); glVertex3f(1,0,0)
    #Change the color to green.  All subsequent geometry we draw will be green.
    glColor3f(0,1,0)
    #Make two vertices, thereby drawing a (green) line.
    glVertex(0,0,0); glVertex3f(0,1,0)
    #Change the color to blue.  All subsequent geometry we draw will be blue.
    glColor3f(0,0,1)
    #Make two vertices, thereby drawing a (blue) line.
    glVertex(0,0,0); glVertex3f(0,0,1)
    #Change the color to white again.  All subsequent geometry we draw will be white.  Strictly
    #speaking this isn't required (since we reset the color on line 166 before we draw anything
    #again).  However, it is good practice to reset the color to white, since forgetting to can be a
    #hard-to-track-down bug (e.g. when combining with texturing).
    glColor3f(1,1,1)
    #We're done drawing lines; tell OpenGL so.
    glEnd()
def timeline(_object_):
        if _object_.velocity.isnull() == False:
            _object_.velocity.divide(_object_.dt)
            vel = _object_.velocity.get()
            _object_.pos = vel
            _object_.translate3d(_object_.pos)
def setDomain(_object_,x = 5.0,y = 5.0 ,z = 5.0):
    
    if _object_.pos[0] >= x/2:
        pos = (-_object_.pos[0],-_object_.pos[1],-_object_.pos[2])
        _object_.translate3d(pos)
    if _object_.pos[0] <= -x/2:
        pos = (-_object_.pos[0],-_object_.pos[1],-_object_.pos[2])
        _object_.translate3d(pos)
        
    if _object_.pos[1] >= y/2:
        pos = (-_object_.pos[0],-_object_.pos[1],-_object_.pos[2])
        _object_.translate3d(pos)
    if _object_.pos[1] <= -y/2:
        pos = (-_object_.pos[0],-_object_.pos[1],-_object_.pos[2])
        _object_.translate3d(pos)
        
    if _object_.pos[2] >= z/2:
        pos = (-_object_.pos[0],-_object_.pos[1],-_object_.pos[2])
        _object_.translate3d(pos)
    if _object_.pos[2] <= -z/2:
        pos = (-_object_.pos[0],-_object_.pos[1],-_object_.pos[2])
        _object_.translate3d(pos)
def rotate_3d_environment(axis,theta):

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
def translate_3d_environment(pos):
    dx,dy,dz = pos
    # adding the translation to the environment coords
    cx +=  dx
    cy +=  dy  
    cz +=  dz

# dstance claculator function
def calDistance(a,b):
    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)+((a[2]-b[2])**2))
# this function finds the geometrical center of the surface
def calCenter(surface):
    xc,yc,zc = 0.0,0.0,0.0
    for vert in surface:
        xc += vert[0]; yc += vert[1]; zc += vert[2]
    return xc/len(surface),yc/len(surface),zc/len(surface)
'''
==========================================
    display function
==========================================
'''
def displayGL(mode,_object_):
    if mode =='vertex':
        glBegin(GL_POINTS)
        for v in _object_.vertex:
                glVertex3fv(v)
        glEnd()
    if mode =='edge':
        glBegin(GL_LINES)
        for edge in _object_.edges:
            for vertex in edge:
                glVertex3fv(_object_.vertex[vertex])
        glEnd()
    if mode == 'face':
        
        # filling the vertex in face list
        face_list =[]
        for face in _object_.faces:
            vertex_list = []
            for v in face:
                 vertex_list.append(_object_.vertex[v])
            face_list.append(vertex_list)

        glBegin(GL_QUADS)    
        for face in face_list:
            for vertex in face:
                glColor3fv(color.GRAY)
                glVertex3fv(vertex)
        glEnd()
def display(mode,_object_):
    global color
    if mode == 'edit':
        pass
    # display the object in its vertex mode
    if mode == 'vertex':
       for x,y,z in _object_.vertex:
           z+=5
           
           x -=cam.pos[0]
           y -=cam.pos[1]
           z +=cam.pos[2]
           
           f = 200/z
           x,y = x*f,y*f
           pygame.draw.circle(screen,color.GRAY,(cx+int(x),cy+int(y)),3)
    if mode == 'edge':
        # put the cube on screen edge
        for edge in _object_.edges:
            points = []
            for x,y,z,in (_object_.vertex[edge[0]],_object_.vertex[edge[1]]):
                x -=cam.pos[0]
                y -=cam.pos[1]
                z +=cam.pos[2]
                f = 200/z
                    
                x,y = x*f,y*f
                points +=  [(cx+int(x),cy+int(y))]

            pygame.draw.line(screen,color.GRAY,points[0],points[1],1)
    if mode == 'face':
        # convert 3d vertex to 2d screen coords
        screen_verts=[]
        for x,y,z in _object_.vertex:
            x-= cam.pos[0]; y-=cam.pos[1];z+=cam.pos[2]
            f= 200/z
            x,y = x*f,y*f
            screen_verts += [(cx+int(x),cy+int(y))]
        # filling the vertex in face list
        face_list =[]
        for face in _object_.faces:
            vertex_list = []
            for v in face:
                 vertex_list.append(screen_verts[v])
            face_list.append(vertex_list)

        # displaying the cube 
        for i in range(0,len(face_list)):
            if i == 3:
                pygame.draw.polygon(screen,color.GRAY,face_list[i])
            elif i == 4:
                pygame.draw.polygon(screen,color.YELLOW,face_list[i])
            else:
                pygame.draw.polygon(screen,color.RED,face_list[i])

    if mode == 'face1':
        
        # convert 3d vertex to 2d screen coords
        screen_verts=[]
        for x,y,z in _object_.vertex:
            x-= cam.pos[0]; y-=cam.pos[1];z+=cam.pos[2]
            f= 200/z
            x,y = x*f,y*f
            screen_verts += [(cx+int(x),cy+int(y))]
            
        # filling the vertex in face list
        face_list =[];face_list3d = [] ;face_depth = []
        for face in _object_.faces:
            vertex_list3d = []; vertex_list = []
            for v in face:
                 vertex_list3d.append(_object_.vertex[v])
                 vertex_list.append(screen_verts[v])
            face_list3d.append(vertex_list3d)
            face_list.append(vertex_list)
            
        # calculating the depth of surfaces 
        
        for face in face_list3d:
            c = calCenter(face)
            dist = calDistance(c,cam.pos)
            face_depth.append(dist)
        # sorting the face according to the depth    
        for i in range(0,len(face_depth)):
            for j in range(0,len(face_list)):
                if face_depth[i] >face_depth[j]:
                    face_depth[i],face_depth[j] = face_depth[j],face_depth[i]
                    face_list[i] ,face_list[j]  = face_list[j], face_list[i]
        
        # displaying the cube 
        for i in range(0,len(face_list)):
            if i == 3:
                pygame.draw.polygon(screen,color.GRAY,face_list[i])
            elif i == 4:
                pygame.draw.polygon(screen,color.YELLOW,face_list[i])
            else:
                pygame.draw.polygon(screen,color.RED,face_list[i])
            



   


#print help(Cube)
print "\n==================help=================================\n"
print "press [a w s d e q]  to control camera motion\n\n"
print "press [x y z] to rotate the cube | press [g] scale the cube\n [f] apply force"

# initilize the main loop
while True:
    # setting the smallest time variation
    dt = float(clock.tick(60))/1000
    clock.tick(60)
        
    # Fill the background color to screen as black
    if Gmode == 'openGL':
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    else:
        screen.fill(color.BLACK)
    
    dtheta = 0.15
    # display the objects on the screen 
    if Gmode =='openGL':
        displayGL('face',cube1)
        displayGL('edge',cube2)
        displayGL('edge',cube3)
        coords()
    else:
        display('face',cube1)
        display('edge',cube2)
        display('edge',cube3)
    
    
    # all animation show by timeline
    timeline(cube1)
    # gravity apply on the object
    #cube1.applyG()
    
    setDomain(cube1,2,2,2)
    pygame.display.flip()
   
    
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type==pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if pygame.key == pygame.K_LEFT:
                pass
        #If the user "clicked" the scroll wheel forward or backward:
        if event.type == MOUSEBUTTONDOWN:
            #Zoom in
            if   event.button == 4: cam.radius *= 0.9
            #Or out.
            elif event.button == 5: cam.radius /= 0.9
    # get the input 
    key = pygame.key.get_pressed()
    mouse_rel = pygame.mouse.get_rel()
    mouse_buttons = pygame.mouse.get_pressed()
    # input events
    if key[pygame.K_x]: cube1.rotate3d('x',dtheta)
    if key[pygame.K_y]: cube1.rotate3d('y',dtheta)
    if key[pygame.K_z]: cube1.rotate3d('z',dtheta)
    if key[pygame.K_g]: cube1.scale3d((0.5,0.5,0.5))
    if key[pygame.K_f]: cube1.applyForce(f)
    if key[pygame.K_j]: cube1.setPos3d((10,10,0))
    
    
    # update the camera
    if Gmode == 'openGL':
        cam.updateGL(mouse_buttons,mouse_rel,key)
    else:
        cam.update(dt,key)

    
    






