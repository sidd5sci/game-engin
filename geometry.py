# importing the physics
from physics import *
from transformations import *
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(0,0,0)
        self.centerOfGravity = vertex(0,0,0)
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
        self.pos.x,self.pos.y,self.pos.z = pos[0],pos[1],pos[2]
        self.centerOfBody = vertex(pos[0],pos[1],pos[2])
        self.centerOfGravity = vertex(pos[0],pos[1],pos[2])
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
    translate3d(c,(10,2,5))
    print c.pos.get()
    
    
