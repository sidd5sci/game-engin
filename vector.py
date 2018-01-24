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
    def set_(self,pos):
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
        x,y,z = vctr.x,vctr.y,vctr.z
        x1,y1,z1 = self.x,self.y,self.z
        x *= x1; y *= y1; z *= z1
        result = x+y+z
        return result
    def multV(self,vctr):
        x = (vctr.y*self.z - vctr.z*self.y)
        y = (vctr.x*self.z - vctr.z*self.x)
        z = (vctr.x*self.y - vctr.y*self.x)
        
        v = vector((0,0,0),(0,0,0))
        v.assign(x,y,z)
        self.copy(v)
        self.magCal()
        return v        
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
    def rotate(self,axis,angle=0):
        if axis == 'x':
            pass
    def isAlong(self,vect):
        # returns True if both the vectors are along same line
        x,y,z = self.x,self.y,self.z
        x1,y1,z1 = vect.x,vect.y,vect.z
        x *= x1; y *= y1; z *= z1
        if x != 0:
            return True
        elif y != 0:
            return True
        elif z != 0:
            return True
        else:
            return False
    def isPerp(self,vect):
        # returns True if both the vectors are perpendicular to each other
        x,y,z = self.x,self.y,self.z
        x1,y1,z1 = vect.x,vect.y,vect.z

        x *= x1; y *= y1; z *= z1

        if x == 0:
            if y != 0:
                if z != 0:
                    return True
        else:
            return False
    def getAngle(self,vect):
        # this returns the angle between the two vectors
        angle  = math.acos(self.multS(vect)/(self.magCal()*vect.magCal()))
        return angle
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
    def reverse(self):
        self.x,self.y,self.z = -self.x,-self.y,-self.z
    def get(self):
        return self.x,self.y,self.z


######################################################

def makeVector(mag,_dir_):
    v = vector((0,0,0),(0,0,0))
    v.x,v.y,v.z = _dir_.x,_dir_.y,_dir_.z
    v.normalized()
    v.mult(1/mag)
    v.magCal()
    return v
def getAngle(vctr1,vctr2):
        # this returns the angle between the two vectors
        m = vctr1.magCal()*vctr2.magCal()
        angle  = math.acos(dot(vctr1,vctr2)/(m))
        return angle
def dot(vctr,vctr1):
        x,y,z = vctr.x,vctr.y,vctr.z
        x1,y1,z1 = vctr1.x,vctr1.y,vctr1.z
        x *= x1; y *= y1; z *= z1
        result = x+y+z
        return result
def cross(vctr,vctr1):
        x = (vctr.y*vctr1.z - vctr.z*vctr1.y)
        y = (vctr.x*vctr1.z - vctr.z*vctr1.x)
        z = (vctr.x*vctr1.y - vctr.y*vctr1.x)
        
        v = vector((0,0,0),(0,0,0))
        v.x,v.y,v.z = x,y,z
        return v

# =================================
#   global variables
# =================================
# zero vertex
ZERO_VERTEX = vertex(0,0,0)
UNIT_VERTEX = vertex(1,1,1)
# zero vertex
ZERO_VECTOR = vector((0,0,0),(0,0,0))
UNIT_VECTOR = vector((0,0,0),(1,1,1))

if __name__ == '__main__':
    pass
