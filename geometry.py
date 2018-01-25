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





# importing the physics
from physics import *
from transformations import *

'''
==========================================
    objects joining  
==========================================
'''
class joints:
    def __init__(self,_id_,_type_= 'rigid',conn = 0,length = 1,angle = 0):
        self.type = _type_ # 1->rigid | 2->physical | 3-> logical
        self.connection = conn # 0-> forword | 1-> backword
        self.object_id = _id_ # defaul is not set
        self.length = length
        self.angle = angle 
    def calData(self,):
        for j in _object_.joints:
            _id_ = j.object_id
            slave = fetchObjectById(_id_)
            p2 = worldToScreen([slave.pos.x,slave.pos.y,slave.pos.z])
            p1 = worldToScreen([_object_.pos.x,_object_.pos.y,_object_.pos.z])  
    def rotate(self):
        pass
    def move(self):
        pass
    def scale(self):
        pass
'''
==========================================
    axis class
==========================================
'''
class axis():
    def __init__(self,center,rot,size):
        self.center = center # vertex
        self.angles = list(rot)
        self.size = size
        # by default every axis always align to (0,0,0) to the world cordinates
        self.ends = [1,0,0],[0,1,0],[0,0,1]
        #self.rotate(self.angles)
        self.calEnds()
        
    def calEnds(self):
        for i in range(0,3):
            self.ends[i][0] = self.center.x + self.ends[i][0]*self.size 
            self.ends[i][1] = self.center.y + self.ends[i][1]*self.size 
            self.ends[i][2] = self.center.z + self.ends[i][2]*self.size 
    def translate(self,t):
        self.center.x += t[0]
        self.center.y += t[1]
        self.center.z += t[2]
        for i in range(0,3):
            self.ends[i][0] = t[0] + self.ends[i][0]
            self.ends[i][1] = t[1] + self.ends[i][1]
            self.ends[i][2] = t[2] + self.ends[i][2] 
    def rotate(self,rot):
        if len(rot):
            # axis is rotated 
            if rot[0] != 0:
                c,s = math.cos(rot[0]),math.sin(rot[0])
                temp = self.ends[1]
                self.ends[1] = - self.ends[1]*c - self.ends[2]*s
                self.ends[2] = - temp*c + self.ends[2]*s
            if rot[1] != 0:
                c,s = math.cos(rot[1]),math.sin(rot[1])
                temp = self.ends[0]
                self.ends[0] = - self.ends[0]*c - self.ends[2]*s
                self.ends[2] = - temp*c + self.ends[2]*s
            if rot[2] != 0:
                c,s = math.cos(rot[2]),math.sin(rot[2])
                temp = self.ends[0]
                self.ends[0] = - self.ends[0]*c - self.ends[1]*s
                self.ends[1] = - temp*c + self.ends[1]*s

'''
==========================================
    object classes
==========================================
'''
## guns and bombs

class Ak47(physics):
    def __init__(self,pos):
        super(Ak47,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]
        
## living objects

class Women(physics):
    def __init__(self,pos):
        super(Women,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]
class Man(physics):
    def __init__(self,pos):
        super(Man,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

##  basic geometry

class Arrow(physics):
    def __init__(self,pos):
        super(Arrow,self).__init__()
        self.vertex = {[1,0,1],[1,0,-1],[-1,0,-1],[-1,0,1],  
                      [1,5,1],[1,5,-1],[-1,5,-1],[-1,5,1],
                      [0,7,0]}
        self.edges = [0,1],[1,2],[2,3],[3,0],
                     
        self.faces = [0,1,2,3]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]
class Pointer(physics):
    def __init__(self,pos):
        super(Pointer,self).__init__()
        self.vertex = [0,0,0],[1,0,0],[0,1,0],[0,0,1]
        self.edges = [0,1],[0,2],[0,3]
        self.faces = []
        self.vertexColor = [100,00,00]
        self.edgeColor = [[200,0,0],[0,200,0],[0,0,200]]
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]
# mark
class Mark(physics):
    def __init__(self,pos):
        super(Mark,self).__init__()
        self.vertex = [0,0,0],[1,0,0],[0,1,0],[0,0,1]
        self.edges = [0,1],[0,2],[0,3]
        self.faces = []
        self.vertexColor = [100,00,00]
        self.edgeColor = [[200,0,0],[0,200,0],[0,0,200]]
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

# pointer 3d is pointer in 3d world used as current active point for all the oprations

class Pointer3d(physics):
    def __init__(self,pos):
        super(Pointer3d,self).__init__()
        self.vertex = [[0,0,0]]
        self.edges = []
        self.faces = []
        self.vertexColor = [[50,200,00]]
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

class Teapot(physics):
    def __init__(self,pos):
        super(Teapot,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

class Donought(physics):
    def __init__(self,pos):
        super(Donought,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

class Sphere(physics):
    def __init__(self,pos):
        super(Sphere,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

class PlaneWire(physics):
    def __init__(self,pos):
        super(PlaneWire,self).__init__()
        self.vertex = [-10,0,10],[-8,0,10],[-6,0,10],[-4,0,10],[-2,0,10],[0,0,10],[2,0,10],[4,0,10],[6,0,10],[8,0,10],[10,0,10],[-10,0,8],[-8,0,8],[-6,0,8],[-4,0,8],[-2,0,8],[0,0,8],[2,0,8],[4,0,8],[6,0,8],[8,0,8],[10,0,8],   [-10,0,6],[-8,0,6],[-6,0,6],[-4,0,6],[-2,0,6],[0,0,6],[2,0,6],[4,0,6],[6,0,6],[8,0,6],[10,0,6],[-10,0,4],[-8,0,4],[-6,0,4],[-4,0,4],[-2,0,4],[0,0,4],[2,0,4],[4,0,4],[6,0,4],[8,0,4],[10,0,4],[-10,0,2],[-8,0,2],[-6,0,2],[-4,0,2],[-2,0,2],[0,0,2],[2,0,2],[4,0,2],[6,0,2],[8,0,2],[10,0,2],[-10,0,0],[-8,0,0],[-6,0,0],[-4,0,0],[-2,0,0],[0,0,0],[2,0,0],[4,0,0],[6,0,0],[8,0,0],[10,0,0],    [-10,0,-10],[-8,0,-10],[-6,0,-10],[-4,0,-10],[-2,0,-10],[0,0,-10],[2,0,-10],[4,0,-10],[6,0,-10],[8,0,-10],[10,0,10],[-10,0,-8],[-8,0,-8],[-6,0,-8],[-4,0,-8],[-2,0,-8],[0,0,-8],[2,0,-8],[4,0,-8],[6,0,-8],[8,0,-8],[10,0,-8],      [-10,0,-6],[-8,0,-6],[-6,0,-6],[-4,0,-6],[-2,0,-6],[0,0,-6],[2,0,-6],[4,0,-6],[6,0,-6],[8,0,-6],[10,0,-6],[-10,0,-4],[-8,0,-4],[-6,0,-4],[-4,0,-4],[-2,0,-4],[0,0,-4],[2,0,-4],[4,0,-4],[6,0,-4],[8,0,-4],[10,0,-4],[-10,0,-2],[-8,0,-2],[-6,0,-2],[-4,0,-2],[-2,0,-2],[0,0,-2],[2,0,-2],[4,0,-2],[6,0,-2],[8,0,-2],[10,0,-2]

        self.edges = [0,1],[1,2],[2,3],[3,0]
        self.faces = [0,1,2,3]
        self.vertexColor = [[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100]]
        self.edgeColor = [[100,100,100],[100,100,100],[100,100,100],[100,100,100]]
        self.faceColor = [[200,200,200]]
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        self.axis = axis(self.centerOfBody,[0,0,0],5) # axis of the object
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

class Plane(physics):
    def __init__(self,pos):
        super(Plane,self).__init__()
        self.vertex = [10,0,10],[10,0,-10],[-10,0,-10],[-10,0,10]
        self.edges = [0,1],[1,2],[2,3],[3,0]
        self.faces = [0,1,2,3]
        self.vertexColor = [[100,100,100],[100,100,100],[100,100,100],[100,100,100]]
        self.edgeColor = [[100,100,100],[100,100,100],[100,100,100],[100,100,100]]
        self.faceColor = [[200,200,200]]
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        self.axis = axis(self.centerOfBody,[0,0,0],5) # axis of the object
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]
class Circle(physics):
    def __init__(self,pos):
        super(Circle,self).__init__()
        self.vertex = [0.780777, -0.336171, -2.35336],[0.585687, -0.336171, -2.334146],[0.398094, -0.336171, -2.27724],[0.225207, -0.336171, -2.18483],[0.07367, -0.336171, -2.060467],[-0.050693, -0.336171, -1.90893],[-0.143103, -0.336171, -1.736044],[-0.200008, -0.336171, -1.54845],[-0.219223, -0.336171, -1.35336],[-0.200008, -0.336171, -1.15827],[-0.143103, -0.336171, -0.970677],[-0.050693, -0.336171, -0.79779],[0.07367, -0.336171, -0.646253],[0.225207, -0.336171, -0.521891],[0.398094, -0.336171, -0.429481],[0.585687, -0.336171, -0.372575],[0.780777, -0.336171, -0.35336],[0.975868, -0.336171, -0.372575],[1.163461, -0.336171, -0.429481],[1.336348, -0.336171, -0.521891],[1.487884, -0.336171, -0.646254],[1.612247, -0.336171, -0.797791],[1.704657, -0.336171, -0.970677],[1.761562, -0.336171, -1.158271],[1.780777, -0.336171, -1.353361],[1.761562, -0.336171, -1.548452],[1.704656, -0.336171, -1.736045],[1.612246, -0.336171, -1.908931],[1.487883, -0.336171, -2.060468],[1.336346, -0.336171, -2.184831],[1.163459, -0.336171, -2.27724],[0.975866, -0.336171, -2.334146]
        self.edges = [0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,0]
        self.faces = [0,1,2,3,4,5,6,7]
        self.vertexColor = [[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100]]
        self.edgeColor = [[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100]]
        self.faceColor = [[200,200,200]]
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        self.axis = axis(self.centerOfBody,[0,0,0],5) # axis of the object
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]


class Cylinder(physics):
    def __init__(self,pos):
        super(Cylinder,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        self.axis = axis(self.centerOfBody,[0,0,0],5) # axis of the object
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

class Cone(physics):
    def __init__(self,pos):
        super(Cone,self).__init__()
        self.vertex = [],[]
        self.edges = [],[]
        self.faces = [],[]
        self.vertexColor = []
        self.edgeColor = []
        self.faceColor = []
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
        self.joints = list() # store the id and joint type data 
        self.axis = axis(self.centerOfBody,[0,0,0],5) # axis of the object
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]

class Cube(physics):
    def __init__(self,pos):
        super(Cube,self).__init__()
        self.vertex = [1.000000 ,-1.000000, -1.000000],[ 1.000000, -1.000000, 1.000000],[ -1.000000 ,-1.000000 ,1.000000],[ -1.000000, -1.000000 ,-1.000000],[ 1.000000, 1.000000, -0.999999],[ 0.999999 ,1.000000, 1.000001],[ -1.000000, 1.000000 ,1.000000],[ -1.000000, 1.000000, -1.000000]
        self.edges = [0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]
        self.faces = [0,1,2,3],[4,5,6,7],[0,1,5,4],[2,3,7,6],[0,3,7,4],[1,2,6,5]
        self.vertexColor = [[253,170,0],[253,170,0],[253,170,0],[253,170,0],[253,170,0],[253,170,0],[253,170,0],[253,170,0]]
        self.edgeColor = [[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100]]
        self.faceColor = [[200,200,200],[200,200,200],[200,200,200],[200,200,200],[200,200,200],[200,200,200]]
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(pos[0],pos[1],pos[2])
        self.centerOfGravity = vertex(pos[0],pos[1],pos[2])
        self.joints = list() # store the id and joint type data 
        self.axis = axis(self.centerOfBody,[0,0,0],5) # axis of the object 
        # translating the object from origin to given position
        if self.pos.x!= 0 or self.pos.y!= 0 or self.pos.z!= 0:
            for i in range(0,len(self.vertex)):
                self.vertex[i][0] += pos[0]
                self.vertex[i][1] += pos[1]
                self.vertex[i][2] += pos[2]
                    
    
    
    

if __name__ == '__main__':
    c = Cube((0,0,0))
    print c.centerOfBody.get(),c.centerOfGravity.get(),c.pos.get()
    translate3d(c,(0,0,0))
    print c
    p = PlaneWire((0,0,0))
    print p
    translate3d(c,(10,2,5))
    print c.pos.get()
    
    
