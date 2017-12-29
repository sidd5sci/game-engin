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




from transformations import *
from vector import *

'''
==========================================
    camera class
==========================================
'''          
class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0),center=(0,0,0)):
        self.pos = vertex(pos[0],pos[1],pos[2])   #The sphere's center
        self.rot = list(rot)   #The spherical coordinates' angles (degrees).
        self.radius = 3.0      #The sphere's radius
        self.center = list(center)
    def update(self,dt,key):
        s = dt*10
        if key == 'down': self.pos[2] -= s
        if key == 'up': self.pos[2] += s

        if key == 'front': self.pos[1] += s
        if key == 'back': self.pos[1] -= s

        if key == 'left': self.pos[0] -= s
        if key == 'right': self.pos[0] += s 
   
    def rotateCam(self,dt,key,dtheta): 
         
        c1,s1 = math.cos(dtheta),math.sin(dtheta)
        c2,s2 = math.cos(-dtheta),math.sin(-dtheta)
        d = math.sqrt((self.pos.x**2)+(self.pos.y**2)+(self.pos.z**2))
        if key == 'x+': # horiontal x,z
                temp = self.pos[1]

                self.pos[1] =  d*c1 - d*s1
                self.pos[2] =  temp*s1 + d*c1
        if key == 'x-': # horizontal x,z
                temp = self.pos[1]
                self.pos[1] =  d*c2 - d*s2
                self.pos[2] =  temp*s2 + d*c2
        if key == 'y+': # virtical y,z
                temp = self.pos[0]
                self.pos[0] =  self.pos[0]*c1 - self.pos[2]*s1
                self.pos[2] =  temp*s1 + self.pos[2]*c1
        if key == 'y-': # virtical y,z
                temp = self.pos[0]
                self.pos[0] =  self.pos[0]*c2 - self.pos[2]*s2
                self.pos[2] =  temp*s2 + self.pos[2]*c2
    
    def rotate3d(self,axis,dtheta,radius = 0):
        dx,dy,dz  = self.pos[0],self.pos[1],self.pos[2]
        #translate3d_t(_object_,(-dx,-dy,-dz))
        c,s = math.cos(dtheta),math.sin(dtheta)
        if axis == 'x':
                temp = self.pos
                self.pos[1] =  _object_.vertex[i][1]*c - _object_.vertex[i][2]*s
                self.pos[2] =  temp*s + _object_.vertex[i][2]*c
        if axis == 'y':
            for i in range(0,len(_object_.vertex)):
                temp = _object_.vertex[i][0]
                _object_.vertex[i][0] =  _object_.vertex[i][0]*c - _object_.vertex[i][2]*s
                _object_.vertex[i][2] = temp*s + _object_.vertex[i][2]*c
        if axis == 'z':
            for i in range(0,len(_object_.vertex)):
                temp = _object_.vertex[i][0]
                _object_.vertex[i][0] =  _object_.vertex[i][0]*c + _object_.vertex[i][1]*s
                _object_.vertex[i][1] = -temp*s + _object_.vertex[i][1]*c
        # translating the object to the its location
        #translate3d_t(_object_,(dx,dy,dz))
