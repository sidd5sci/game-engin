import math
from decimal import *

class vertex(object):
    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z
    def assign(self,x,y,z):
        self.x,self.y,self.z = x,y,z
    def get(self):
        return self.x,self.y,self.z
    def get2d(self):
        return self.x,self.y
'''
==========================================
    vector class
==========================================
'''
class vector(object):
    def __init__(self,initialPos,finalPos):
        # vector components
        x1,y1,z1 = initialPos
        x2,y2,z2 = finalPos
        # clock wise order        
        self.x = (x2 - x1)
        self.y = (y2 - y1)
        self.z = (z2 - z1)
        # some usefull quantities
        self.mag = 0.0
        self.alpha = 0.0
        self.beta = 0.0
        self.gama = 0.0
        self.magCal()
    def set(self,pos):
        x,y,z = pos
        self.x = x
        self.y = y
        self.z = z
        self.magCal()
    def assign(self,initialPos,finalPos):
        self.x = (finalPos.x - initialPos.x)
        self.y = (finalPos.y - initialPos.y)
        self.z = (finalPos.z - initialPos.z)
        self.magCal()
    def assign(self,initialPos,finalPos):
        x1,y1,z1 = initialPos
        x2,y2,z2 = finalPos
        
        self.x = (x2 - x1)
        self.y = (y2 - y1)
        self.z = (z2 - z1)
        self.magCal()
    def copy(self,vctr):
        self.x,self.y,self.z = vctr.x,vctr.y,vctr.z
    def magCal(self):
        self.mag = math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    def magCal(self):
        self.mag = math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
        return self.mag
    def add(self,vctr):
        self.x += vctr.x; self.y += vctr.y; self.z += vctr.z
        self.magCal()
    def sub(self,vctr):
        self.x += vctr.x; self.y += vctr.y; self.z += vctr.z
        self.magCal()
    def multS(self,vctr):
        self.x *= vctr.x; self.y *= vctr.y; self.z *= vctr.z
        self.magCal()
    def multV(self,vctr):
        self.x *= (self.y*vctr.z - self.z*vctr.y)
        self.z *= (self.x*vctr.z - self.z*vctr.x)
        self.z *= (self.x*vctr.z - self.y*vctr.x)
        self.magCal()
    def divide(self,qt):# dividing vector by scaler quantity
        self.x /= qt; self.y /= qt; self.z /= qt
        self.magCal()
    def mult(self,qt): # multiply the vector with scaler quantity
        self.x *= qt; self.y *= qt; self.z *= qt
        self.magCal()
    def normalized(self):
        self.magCal()
        self.x /= self.mag
        self.y /= self.mag
        self.z /= self.mag
        self.magCal()
    def isUnit(self):
        self.magCal()
        if self.mag == 1:
            return True
        else:
            return False
    def isnull(self):
        # check the vector is null/zero or not
        if self.x == 0 and self.y == 0 and self.z == 0:
            return True
        else:
            return False
    def reverseDir(self,axis):
        if axis == "x":
            self.x = -self.x
        if axis == "y":
            self.y = -self.y
        if axis == "z":
            self.z = -self.z
    def get(self):
        return self.x,self.y,self.z

# =================================
#   global variables
# =================================
# zero vertex
ZERO_VERTEX = vertex(0,0,0)
UNIT_VERTEX = vertex(1,1,1)
# zero vertex
ZERO_VECTOR = vector((0,0,0),(0,0,0))
UNIT_VECTOR = vector((0,0,0),(1,1,1))
