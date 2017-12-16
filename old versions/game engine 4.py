import pygame
from pygame.locals import *
import time,random
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from physics import *
from geometry import *



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
        if key[pygame.K_DOWN]: self.pos[2] -= s
        if key[pygame.K_UP]: self.pos[2] += s

        if key[pygame.K_q]: self.pos[1] += s
        if key[pygame.K_e]: self.pos[1] -= s

        if key[pygame.K_LEFT]: self.pos[0] -= s
        if key[pygame.K_RIGHT]: self.pos[0] += s 
   
    def rotateCam(self,dt,key,dtheta): 
         
        c1,s1 = math.cos(dtheta),math.sin(dtheta)
        c2,s2 = math.cos(-dtheta),math.sin(-dtheta)
        
        if key[pygame.K_w]:
                temp = self.pos[1]
                self.pos[1] =  self.pos[1]*c1 - self.pos[2]*s1
                self.pos[2] =  temp*s1 + self.pos[2]*c1
        if key[pygame.K_s]:
                temp = self.pos[1]
                self.pos[1] =  self.pos[1]*c2 - self.pos[2]*s2
                self.pos[2] =  temp*s2 + self.pos[2]*c2
        if key[pygame.K_a]:
                temp = self.pos[0]
                self.pos[0] =  self.pos[0]*c1 - self.pos[2]*s1
                self.pos[2] =  temp*s1 + self.pos[2]*c1
        if key[pygame.K_d]:
                temp = self.pos[0]
                self.pos[0] =  self.pos[0]*c2 - self.pos[2]*s2
                self.pos[2] =  temp*s2 + self.pos[2]*c2
        if key[pygame.K_c]:
                temp = self.pos[0]
                self.pos[0] =  self.pos[0]*c1 + self.pos[1]*s1
                self.pos[1] = -temp*s1 + self.pos[1]*c1

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
        self.RED = (254,0,0)
        self.BLUE = (0,0,254)
        self.GREEN = (0,254,0)
        self.GRAY = (100,100,100)
        self.YELLOW = (254,254,0)
        self.MAGENTA = (254,0,254)

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
            # _object_.pos = vel
            translate3d(_object_,vel)


def mouseTracker(LastPosition):
    CurrentPosition = pygame.mouse.get_pos()
    dx = CurrentPosition[0] -LastPosition[0]
    dy = CurrentPosition[1] -LastPosition[1]
    return dx,dy

# dstance claculator function
def calDistance(a,b):
    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)+((a[2]-b[2])**2))

# this function finds the geometrical center of the surface
def calCenter(surface):
    xc,yc,zc = 0.0,0.0,0.0
    for vert in surface:
        xc += vert[0]; yc += vert[1]; zc += vert[2]
    return xc/len(surface),yc/len(surface),zc/len(surface)

def screenToWorld(cords):
    global pixelFactor,scalex,scaley
    x,y,z = cords[0],cords[1],0
    
    x,y = x/pixelFactor,y/pixelFactor
    x,y = scalex/2+x,scaley/2+y
    x,y = x+cam.pos[0],y+cam.pos[1]
    return [x,y,z]
def worldToScreen(cords):
    global pixelFactor,cx,cy
    x,y,z = cords[0],cords[1],cords[2]
    
    x,y = x-cam.pos[0],y-cam.pos[1]
    x,y = x*pixelFactor,y*pixelFactor
    x,y = cx+int(x),cy+int(y)
    #x,y = scalex/2+x,scaley/2+y
    return [x,y]
'''
==========================================
    input function
==========================================
'''

def _input_():
    global cube1,pointer3d,point
    
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type == pygame.QUIT:
            #if it is quit the game
            
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
                p = pygame.mouse.get_pos()
                # convert the screen coordinates to world co-ordinates
                loc = screenToWorld(p)
                
                translate3d(pointer3d,(loc[0],loc[1],loc[2]))
                print p
        if event.type == pygame.MOUSEBUTTONUP:
                pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LCTRL:
                pass
            if event.key == pygame.K_x:
               rotate3d(cube1,'x',dtheta)
            if event.key == pygame.K_y:
               rotate3d(cube1,'y',dtheta)
            if event.key == pygame.K_z:
               rotate3d(cube1,'z',dtheta)
            if event.key == pygame.K_g:
               scale3d(cube1,(0.5,0.5,0.5))
            if event.key == pygame.K_f:
               translate3d_t(cube1,(1,0,0))
               print 'cube pos: ',cube1.pos.get()
            if event.key == pygame.K_h:
               translate3d_t(cube1,(0,1,0))
               print 'cube pos: ',cube1.pos.get()   
            if event.key == pygame.K_p:
               translate3d(cube1,(1,0,0))
               print 'cube pos: ',cube1.pos.get()
            if event.key == pygame.K_n:
               createNewObject('cube')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
def createCube():
    createNewObject('cube')
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

def createNewObject(objectType):
    if objectType == 'arrow':
        newObject = Arrow(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'cube':
        newObject = Cube(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'plane':
        newObject = Plane(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'pointer':
        newObject = Cube(pointer3d.pos.get())
        fillObjectSequence(newObject,'edge',True)
    if objectType == 'cone':
        newObject = Cone(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'Cylinder':
        newObject = Cylinder(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'sphere':
        newObject = Sphere(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'donought':
        newObject = Donought(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'Teapot':
        newObject = Teapot(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'pointer3d':
        newObject = Pointer3d(pointer3d.pos.get())
        fillObjectSequence(newObject,'vertex',True)
    if objectType == 'man':
        newObject = Man(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'women':
        newObject = Women(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'ak47':
        newObject = Ak47(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
def fillObjectSequence(_object_,mode,state=False):
    global _object_sequence_
    i = len(_object_sequence_)
    _object_sequence_.append((i,_object_,mode,state))

def showObject():
    global _object_sequence_
    for o in _object_sequence_:
        display(o[2],o[1])

def loadObject():
    global _object_sequence_depth_buffer_
    for o in _object_sequence_depth_buffer_:
        display(o[0],o[1])

###########################################        
def display(mode,_object_):
    global color
    if mode == 'edit':
        pass
    if mode == 'selected':
        pass
    # display the object in its vertex mode
    if mode == 'vertex':
       for v,c in zip(_object_.vertex,_object_.vertexColor):
           x,y,z = v
           z += 5
           #print v           
           x -= cam.pos[0]
           y -= cam.pos[1]
           z += cam.pos[2]
           
           f = 200/z
           x,y = x*f,y*f
           pygame.draw.circle(screen,c,(cx+int(x),cy+int(y)),2)
    if mode == 'edge':
        # put the cube on screen edge
        for edge,c in zip(_object_.edges,_object_.edgeColor):
            points = []
            for x,y,z,in (_object_.vertex[edge[0]],_object_.vertex[edge[1]]):
                x -=cam.pos[0]
                y -=cam.pos[1]
                z +=cam.pos[2]
                f = 200/z
                    
                x,y = x*f,y*f
                
                points +=  [(cx+int(x),cy+int(y))]

            pygame.draw.line(screen,c,points[0],points[1],1)
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
        for f,c in zip(face_list,_object_.faceColor):
            pygame.draw.polygon(screen,c,f)        


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
            
def updateScreenScales():
    global pixelFactor,scalex,scaley,cam
    pixelFactor = 200/cam.pos[2]
    scalex,scaley = -width/pixelFactor,-height/pixelFactor
    
############################################################
#display section 2d 
def pointer():
    global point
    x,y,z = point.get()
    z += 5
    #print x,y,z           
    x -= cam.pos[0]
    y -= cam.pos[1]
    z += cam.pos[2]
      
    f = 200/z
    #x,y = x*f,y*f
    pygame.draw.circle(screen,color.RED,(cx+int(x),cy+int(y)),2)
   


#print help(Cube)
print "\n==================help==================n"
print "press [a w s d e q]  to control camera motion\n\n"
print "press [x y z] to rotate the cube | press [g] scale the cube\n [f] apply force"

def main():
    
    # initilize the main loop
    #while True:
        # setting the smallest time variation
        dt = float(clock.tick(60))/1000
        clock.tick(60)
            
        # Fill the background color to screen as black
        if Gmode == 'openGL':
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        else:
            screen.fill(color.BLACK)
        
        
        # display the objects on the screen 
        if Gmode =='openGL':
            displayGL('face',cube1)
            displayGL('edge',cube2)
            displayGL('edge',cube3)
            coords()
        else:
            display('edge',plane)
            showObject()
            display('edge',wCenter)
            display('edge',pointer3d)
         
        # all animation show by timeline
        timeline(cube1)
        
        
        
        # update the pygame window
        pygame.display.flip()
       

        # get the input
        key = pygame.key.get_pressed()
        _input_()
        mouse_rel = pygame.mouse.get_rel()
        mouse_buttons = pygame.mouse.get_pressed()
        # test the output area
        if key[pygame.K_RCTRL]:
            print 'hello'
            print pointer3d.pos.get()
            print cube1.centerOfBody.get()
            #mainloop()
        # update the camera
        if Gmode == 'openGL':
            cam.updateGL(mouse_buttons,mouse_rel,key)
        else:
            cam.update(dt,key)
            cam.rotateCam(dt,key,dtheta)
            updateScreenScales()
        #root.update()

        
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
        screen.fill(pygame.Color(255,255,255))
        pygame.display.init()
        pygame.display.update()
        return screen

#########################################################
    
#########################################################





# initilize the pygame
pygame.init()
# screen height and width
width ,height = 800,600
# center of the screen | environment cooords
cx,cy,cz = width/2,height/2, -5
# loading the icon  
pygame.display.set_icon(pygame.image.load('Icon.png'))
# init the name of the window
pygame.display.set_caption("Game engin - testing 2017")
# initilise the clock
clock = pygame.time.Clock()
# graphics mode
Gmode = 'openGL6' 
screen = init(Gmode)

'''
==========================================
    Global constants
==========================================
'''
dt = 0.015
dtheta = 0.055
'''
==========================================
    global variables
==========================================
'''   
# sequence of all the objects in decending order of the
# z buffer from the point of the projection 
_object_sequence_depth_buffer_ = list()
# this sequence is vector of the physical and drawing objects
# in the 3D world environment
_object_sequence_ = list()
# initilise the color object
color = colors()
# initilise the main camera
cam = Cam((-0,0,-30))
# world screen scales
pixelFactor = 200/cam.pos[2]
scalex,scaley = -width/pixelFactor,-height/pixelFactor
# create the default 3d plane and cordinates of the 3d world
plane = Plane((0,0,0))
wCenter = Pointer((0,0,0))
# 3d pointer
pointer3d = Mark((8,0,0))
# create objects of some geometry
cube1 = Cube((0,0,0))
cube2 = Cube((5,0,0))
cube3 = Cube((5,-10,-3))
# appending the objects to the object sequence buffer
fillObjectSequence(cube1,'face')
fillObjectSequence(cube2,'vertex')
fillObjectSequence(cube3,'edge')

print 'Pointer ',pointer3d.pos.get(),'scales',scalex,scaley



if __name__ == '__main__':
    
    
    main()
    
    
