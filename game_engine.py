'''
Copyright {2017} {siddhartha singh | sidd5sci@gmail.com}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

#if __name__ == '__main__':from GUI_layout import *

import pygame
from pygame.locals import *
import time,random
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from geometry import *
from import_export import *
from GA import *

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
   
    def rotateCam(self,dt,key,dtheta,radius=1): 
         
        c1,s1 = math.cos(dtheta),math.sin(dtheta)
        c2,s2 = math.cos(-dtheta),math.sin(-dtheta)
        d = math.sqrt((self.pos[0]**2)+(self.pos[1]**2)+(self.pos[2]**2))
        
        if key[pygame.K_w]:
                temp = self.pos[1]
                #self.pos[1] =  d*c1 - d*s1
                #self.pos[2] =  temp*s1 + d*c1
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
        
        #if key[pygame.K_c]:
        #        temp = self.pos[0]
        #        self.pos[0] =  self.pos[0]*c1 + self.pos[1]*s1
        #        self.pos[1] = -temp*s1 + self.pos[1]*c1

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

def timeline():
    global _object_sequence_
    for _object_ in _object_sequence_:
        
        if _object_[1].velocity.isnull() == False:
        
            oldPos = _object_[1].pos.get()
            _object_[1].updatePos()
            
            newPos = _object_[1].pos.get()
            dx,dy,dz = newPos[0]-oldPos[0],newPos[1]-oldPos[1],newPos[2]-oldPos[2]
            translate3d_t(_object_[1],(dx,dy,dz))
            
        if _object_[1].omega.isnull() == False:
            oldPos = _object_[1].theta.get()
            _object_[1].updateTheta()
            newPos = _object_[1].theta.get()
            dx,dy,dz = newPos[0]-oldPos[0],newPos[1]-oldPos[1],newPos[2]-oldPos[2]
            rotate3d(_object_[1],'x',dx)
            rotate3d(_object_[1],'y',dy)
            rotate3d(_object_[1],'z',dz)

def mouseTracker(LastPosition):
    CurrentPosition = pygame.mouse.get_pos()
    dx = CurrentPosition[0] -LastPosition[0]
    dy = CurrentPosition[1] -LastPosition[1]
    return dx,dy
# dstance claculator function
def calDistance(a,b):
    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2)+((a[2]-b[2])**2))
def calDistance2d(a,b):
    return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
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
    
    x,y,z = x-cam.pos[0],y-cam.pos[1],z+cam.pos[2]
    #pixelFactor = (pixelFactor*cam.pos[2])/z
    f = 200/z
    #x,y = x*pixelFactor,y*pixelFactor
    x,y = x*f,y*f
    x,y = cx+int(x),cy+int(y)
    #x,y = scalex/2+x,scaley/2+y
    return [x,y]
'''
==========================================
    input function
==========================================
'''
def fetchKey():
    global _key_sequence
    for k in _key_sequence_:
        _key_sequence_.remove(k)
        break;return k
        
def pushKey():
    global _key_sequence_
    if pygame.key.get_pressed():
        _id_ = -1
        for k in _key_sequence_:
            _id_ = k[0][0]
            break
        _id_ = _id_ + 1
        key = pygame.key.get_pressed()
        _key_sequence_.append([_id_,key])
def keyOpration():
    global _key_sequence_
    # _key_sequence_ [_id_,key,hit_time]
    k = fetchKey()
    if k[1] == pygame.K_a:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_b:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_c:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_d:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_e:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_f:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_g:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_h:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_i:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_j:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_k:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_l:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_m:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_n:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_o:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_p:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_q:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_r:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_s:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_t:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_u:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_v:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_w:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_x:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_y:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_z:
        _key_sequence_.remove(k)
    elif k[1] == pygame.K_RCTRL or k[1] == pygame.K_LCTRL :
        _key_sequence_.remove(k)
        k2 = fetchKey()
        if k2[1] == pygame.K_a:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_b:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_c:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_d:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_e:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_f:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_g:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_h:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_i:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_j:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_k:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_l:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_m:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_n:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_o:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_p:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_q:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_r:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_s:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_t:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_u:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_v:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_w:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_x:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_y:
            _key_sequence_.remove(k)
        elif k2[1] == pygame.K_z:
            _key_sequence_.remove(k)
        
def _input_(key,mouse_rel,mouse_buttons):
    global cube1,pointer3d,point,_object_sequence_
    if key[pygame.K_x]:
        for o in _object_sequence_:
            if o[3] == True:
                rotate3d(o[1],'x',dtheta)
    if key[pygame.K_y]:
        for o in _object_sequence_:
            if o[3] == True:
                rotate3d(o[1],'y',dtheta)
    if key[pygame.K_z]:
        for o in _object_sequence_:
            if o[3] == True:
                rotate3d(o[1],'z',dtheta)
    if key[pygame.K_f]:
        for o in _object_sequence_:
            if o[3] == True:
                translateConnectedObjects(o[1],[0,1,0])
    if key[pygame.K_h]:
        for o in _object_sequence_:
            if o[3] == True:
                translateConnectedObjects(o[1],[1,0,0])
    if key[pygame.K_g]:
        for o in _object_sequence_:
            if o[3] == True:
                scale3d(o[1],(0.1,0.1,0.1))
    if key[pygame.K_p]:
        for o in _object_sequence_:
            if o[3] == True:
                if len(o[1].joints):
                    print o[1].joints 
                else:
                    translate3d(o[1],(1,0,0))
    if key[pygame.K_n]:createNewObject('cube') # creating the  new object 
    if key[pygame.K_l]:
        v = vector((0,1,0),(0,0,0))
        for o in _object_sequence_:
            if o[3] == True:
                o[1].applyAcc(9.87,v)# apply gravity
    if key[pygame.K_o]:
        v = vector((0,4,0),(0,0,0))
        for o in _object_sequence_:
            if o[3] == True:
                o[1].applyForce1((1,1,0),1,v) # apply the torque
    if key[pygame.K_u]:
        v = vector((0,1,1),(0,0,0))
        for o in _object_sequence_:
            if o[3] == True:
                o[1].applyAngAcc(0.11,v)# apply gravity
    if key[pygame.K_v]:deselectAllObjects()# deselects all the objects 
    if key[pygame.K_k]:gaHolder.append(initGA())
    if key[pygame.K_j]:livePopulation()
    if key[pygame.K_c]:
        # printing out the data of all the objects
         for o in _object_sequence_:
            print (o[0],' | ',o[2],' | ',o[3])
    if key[pygame.K_t]:
        #_selected_object_sequence_
        s = _selected_object_sequence_[-1]
        # fetch the last selected object as master
        master  =  fetchObjectById(s)
        # filling the master joints 
        for o in _object_sequence_:
            if o[0] != s:
                # found the object 
                if o[3] == True: # if the object is selected 
                    l = calDistance([master.pos.x,master.pos.y,master.pos.z],[o[1].pos.x,o[1].pos.y,o[1].pos.z])
                    j = joints(o[0],'rigid',0,l) # creating a new joint
                    master.joints.append(j) # appened a new joint in the list of joints
            
    if mouse_buttons[0]:
        # getting the current position of the mouse 
        p = pygame.mouse.get_pos()
        # convert the screen coordinates to world co-ordinates
        loc = screenToWorld(p)
        # translatting the 3d pointer to the location of the mouse
        translate3d(pointer3d,(loc[0],loc[1],loc[2]))
        # print the  mouse position for any use
        print p
    if mouse_buttons[2]:
        #print "right key confirmed"
        p = pygame.mouse.get_pos()
        # convert the screen coordinates to world co-ordinates
        loc = screenToWorld(p)
        # searching for objects those are under the radius of pointer (screen coords)
        for o in _object_sequence_:
            pos = o[1].pos # getting the postion of the object  
            # converting the object's cords to screen cords
            src_pos = worldToScreen([pos.x,pos.y,pos.z])
            # updating the selection 
            if calDistance2d(p,src_pos) <= 10:
               o[3] = True
               _selected_object_sequence_.append(o[0])
              


##    # loop through the events
##    for event in pygame.event.get():
##        #check if the event is the x button
##        if event.type == pygame.QUIT:
##            #if it is quit the game
##            
##            pygame.quit()
##            exit(0)
##        if event.type == pygame.MOUSEBUTTONDOWN:
##                p = pygame.mouse.get_pos()
##                # convert the screen coordinates to world co-ordinates
##                loc = screenToWorld(p)
##                
##                translate3d(pointer3d,(loc[0],loc[1],loc[2]))
##                print p
##        if event.type == pygame.MOUSEBUTTONUP:
##                pass
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                pass
##            if event.key == pygame.K_RIGHT:
##                pass
##            if event.key == pygame.K_UP:
##                pass
##            if event.key == pygame.K_DOWN:
##                pass
##            if event.key == pygame.K_LCTRL:
##                pass
##            if event.key == pygame.K_x:
##               rotate3d(cube1,'x',dtheta)
##            if event.key == pygame.K_y:
##               rotate3d(cube1,'y',dtheta)
##            if event.key == pygame.K_z:
##               rotate3d(cube1,'z',dtheta)
##            if event.key == pygame.K_g:
##               scale3d(cube1,(0.5,0.5,0.5))
##            if event.key == pygame.K_f:
##               translate3d_t(cube1,(1,0,0))
##               print 'cube pos: ',cube1.pos.get()
##            if event.key == pygame.K_h:
##               translate3d_t(cube1,(0,1,0))
##               print 'cube pos: ',cube1.pos.get()   
##            if event.key == pygame.K_p:
##               translate3d(cube1,(1,0,0))
##               print 'cube pos: ',cube1.pos.get()
##            if event.key == pygame.K_n:
##               createNewObject('cube')
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT:
##                pass
##            if event.key == pygame.K_RIGHT:
##                pass
##            if event.key == pygame.K_UP:
##                pass
##            if event.key == pygame.K_DOWN:
##                pass
def createCube():
    createNewObject('cube')
def createPlane():
    createNewObject('plane')
def createCircle():
    createNewObject('circle')

#################################################
#            genral function 
#################################################
def createNewObject(objectType):
    if objectType == 'arrow':
        newObject = Arrow(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'cube':
        newObject = Cube(pointer3d.pos.get())
        fillObjectSequence(newObject,'face',True)
    if objectType == 'plane':
        newObject = Plane(pointer3d.pos.get())
        fillObjectSequence(newObject,'edge',True)
    if objectType == 'circle':
        newObject = Circle(pointer3d.pos.get())
        fillObjectSequence(newObject,'vertex',True)
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
    # fills the object in a list as [id , object , display mode ,select state]
    global _object_sequence_
    i = len(_object_sequence_)
    #  state True-> selected
    _object_sequence_.append([i,_object_,mode,state])
def deselectAllObjects():
    global _object_sequence_,_selected_object_sequence_
    # desecting all the object the view
    for o in _object_sequence_:
        o[3] = False
    # empty the selected sequence of the object  
    for s in _selected_object_sequence_:
        _selected_object_sequence_.remove(s)
def fetchObjectById(_id_):
    for o in _object_sequence_:
        if o[0] == _id_:
            return o[1]
def showObject():
    global _object_sequence_
    for o in _object_sequence_:
        display(o[2],o[1],o[3])
def showObjectGL():
    global _object_sequence_
    for o in _object_sequence_:
        displayGL(o[2],o[1])
def loadObject():
    global _object_sequence_depth_buffer_
    for o in _object_sequence_depth_buffer_:
        display(o[0],o[1])
def findSelectedObject():
    global _object_sequence_
    for o in _object_sequence_:
        if o[3] == True:
            o[2].mode = 'selected'
def search_object(_id_):
    global _object_sequence_
    for o in _object_sequence_:
        if o[0] == _id_:
            return o[1]
        
#################################################
#            Genatic algorithms
#################################################
def initGA():
    print 'Starting genetic sequence'
    ga = GA()
    # strating the random population
    objType = 'cube'
    ga.createRandomPopulation(10)
    for i in range(0,len(ga.Population)):
        createNewObject(objType)
        translate3d_t(pointer3d,(4,0,0))    
        obj = _object_sequence_[len(_object_sequence_)-1]
        ga.Population[i].objectId = obj[0]
    return ga
def livePopulation():
    global gaHolder
    print 'Genetic simulator running...'
    # fetching the GA
    for ga in gaHolder:
        # run the GA simulation in physical world
        ga.Genration()
        for i in range(0,len(ga.Population)):
            
            objResult = search_object(ga.Population[i].objectId)
            
            if ga.genration == 1:
                v = vector((0,0,0),(random.uniform(-5,5),0,random.uniform(-5,5)))
                objResult.applyVelocity(0.2,v)
                objResult.applyAngAcc(0.1,v)
                
            #for i in range(0,10000000):
                #ga.naturalSelection(task,**args)
            
            ga.findBestFitesest()
            ga.crossOverEngine()
            ga.mutation()
            ga.regenration()
#################################################
#            forword/ inverse kinemetics
#################################################

def translateConnectedObjects(_object_,t):
    translate3d_t(_object_,t) # translating the master
    _object_.axis.translate(t) # translating the axis of the obejct
    if len(_object_.joints): # checking the master have any joints
        for j in _object_.joints: # fetching the joints 
            s = fetchObjectById(j.object_id) # fetching the jointed object 
            translateConnectedObjects(s,t) # recursivly translating the object
def rotateConnectedObjects(_obejct,axis,rot):
    rotate3d(_object_,axis,rot) # rotate the object about the axis
    _object_.axis.rotate(axis,rot) # rotate the axis too

################################################
#           Display function
################################################
def display(mode,_object_,select = False,edit = False,display = True):
    global color
    if display == True:
        if select == True:# if object is selected
            
            # display the object in its vertex mode
            if mode == 'vertex':
                for v,c in zip(_object_.vertex,_object_.vertexColor):
                    x,y,z = v
                    #z += 5        
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
            # high lighting the vertex of the objects
            for v,c in zip(_object_.vertex,_object_.vertexColor):
                x,y,z = v
                #z += 5        
                x -= cam.pos[0]
                y -= cam.pos[1]
                z += cam.pos[2]
                
                f = 200/z
                x,y = x*f,y*f
                if select == True:
                    pygame.draw.circle(screen,color.RED,(cx+int(x),cy+int(y)),2)
            # displaying the joints between the objects 
            if len(_object_.joints): 
                # if object have any joit the code will work
                for j in _object_.joints:
                    _id_ = j.object_id
                    slave = fetchObjectById(_id_)
                    
                    p2 = worldToScreen([slave.pos.x,slave.pos.y,slave.pos.z])
                    p1 = worldToScreen([_object_.pos.x,_object_.pos.y,_object_.pos.z])    
                    pygame.draw.line(screen,color.GRAY,p1,p2,1)
            # displaying the axis of the object
           
            pygame.draw.line(screen,color.RED,worldToScreen(_object_.axis.center.getAsList()),worldToScreen(_object_.axis.ends[0]),1)
            pygame.draw.line(screen,color.GREEN,worldToScreen(_object_.axis.center.getAsList()),worldToScreen(_object_.axis.ends[1]),1)
            pygame.draw.line(screen,color.BLUE,worldToScreen(_object_.axis.center.getAsList()),worldToScreen(_object_.axis.ends[2]),1)
           
            
        ########################################################################
        else:# if object is not selected 

            # display the object in its vertex mode
            if mode == 'vertex':
                for v,c in zip(_object_.vertex,_object_.vertexColor):
                    x,y,z = v
                    #z += 5        
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
            # displaying the joints between the objects 
            if len(_object_.joints): 
                # if object have any joit the code will work
                for j in _object_.joints:
                    _id_ = j.object_id
                    salve = fetchObjectById(_id_)
                    p2 = worldToScreen([salve.pos.x,salve.pos.y,salve.pos.z])
                    p1 = worldToScreen([_object_.pos.x,_object_.pos.y,_object_.pos.z])           
                    pygame.draw.line(screen,color.GRAY,p1,p2,1)
def displayGL(mode,_object_):
    if mode =='vertex':
        glBegin(GL_POINTS)
        for v in _object_.vertex:
                glColor3f(0.5,0,0.40)
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
                glColor3f(0.5,0,0.40)
                glVertex3fv(vertex)
        glEnd()
def updateScreenScales():
    global pixelFactor,scalex,scaley,cam
    pixelFactor = 200/cam.pos[2]
    scalex,scaley = -width/pixelFactor,-height/pixelFactor
    
################################################
#       display section 2d 
################################################
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
print "press [a w s d e q]  [< ^ > v ]to control camera motion\n\n"
print "press [x y z] to rotate the cube | press [g] scale the cube\n [f] apply force"





def init(mode):
    if mode == 'openGL':
        
        # initilize the screen
        screen = pygame.display.set_mode((width,height),OPENGL|DOUBLEBUF)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width/height, 0.1,100.0)
        glTranslate(0,0,-35)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Add ambient light:
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT,[0.2,0.2,0.2,1.0])
        
        #Add positioned light:
        glLightfv(GL_LIGHT0,GL_DIFFUSE,[2,2,2,1])
        glLightfv(GL_LIGHT0,GL_POSITION,[4,8,1,1])

        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        return screen
    else:
        
        # initilize the screen
        screen = pygame.display.set_mode((width,height))
        screen.fill(pygame.Color(255,255,255))
        pygame.display.init()
        pygame.display.update()
        return screen

##################################################
#           initilising 
##################################################


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
Gmode = 'openGL1' 
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
_object_sequence_ = list()#[id , object , display mode ,select state]
# initilise the color object
color = colors()
# initilise the main camera
cam = Cam((-0,0,-30))
# world screen scales
pixelFactor = 200/cam.pos[2]
scalex,scaley = -width/pixelFactor,-height/pixelFactor
# create the default 3d plane and cordinates of the 3d world
plane = PlaneWire((0,0,0))
wCenter = Pointer((0,0,0))
# 3d pointer
pointer3d = Mark((8,0,0))
# create objects of some geometry
cube1 = Cube((0,0,0))
cube2 = Cube((5,0,0))
cube3 = Cube((5,-10,-3))
# appending the objects to the object sequence buffer
fillObjectSequence(cube1,'face',True)
fillObjectSequence(cube2,'vertex')
fillObjectSequence(cube3,'edge')
# selected object
_selected_object_sequence_ = list()
# GA object holder for global use
gaHolder = []
# selecting the first object 
_selected_object_sequence_.append(_object_sequence_[0][0])
# key input queue 
_key_sequence_ = list()


print 'Pointer ',pointer3d.pos.get(),'scales',scalex,scaley
#print 'wire\n',plane.vertex




x =0
def main():
       global x
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
##            displayGL('face',cube1)
##            displayGL('edge',cube2)
##            displayGL('edge',cube3)
            showObjectGL()
            coords()
       else:
            display('vertex',plane)
            showObject()
            display('edge',wCenter)
            display('edge',pointer3d)
         
       # all animation show by timeline
       timeline()
    
       
       
       pygame.draw.circle(screen,color.WHITE,(int(x),int(200)),4)
       
       if Gmode == 'openGL':
           # screen update
           pygame.display.flip()
       else:
           # update the screen
           pygame.display.update()
           
       # get the input
       key = pygame.key.get_pressed()
       mouse_rel = pygame.mouse.get_rel()
       mouse_buttons = pygame.mouse.get_pressed()
       _input_(key,mouse_rel,mouse_buttons)
       if key[pygame.K_RCTRL]:
           #translate3d_t(pointer3d,(1,0,0))
           #print 'linear:',cube1.pos.get(),cube1.velocity.get(),cube1.acc.get()
           #print 'rotate:',cube1.theta.get(),cube1.omega.get(),cube1.angAcc.get()
           print _selected_object_sequence_[0]
       # update the camera
       if Gmode == 'openGL':
            cam.updateGL(mouse_buttons,mouse_rel,key)
       else:
            cam.update(dt,key)
            cam.rotateCam(dt,key,dtheta,calDistance((0,0,0),cam.pos))
            updateScreenScales()
       
       
       x+=1
       
if __name__ == '__main__':
   while 1:
        main()
        # loop through the events
        for event in pygame.event.get():
            #check if the event is the x button
            if event.type == pygame.QUIT:
                #if it is quit the game
                
                pygame.quit()
                exit(0)



   
