
from vector import *

'''
==========================================
    Gloable constants of Physics
==========================================
'''
# universal gravitational constant 
G = 6.673e-11 # unit  [N m2 kg-2]
# Unit charge
e = 8.85e-32 # unit
# earth mass
MassEearth = 6e24  # kg
'''
==========================================
    physics class
==========================================
'''
class physics(object):

    def __init__(self):

        # mass
        self.mass = 1.0 # kg
        # motion physics / newton physics
        self.pos      = vertex(0,0,0)
        self.velocity = vector((0,0,0),(0,0,0))
        self.acc      = vector((0,0,0),(0,0,0))
        self.force    = vector((0,0,0),(0,0,0))
        self.time     = 0.0
        self.dt       = 0.15
        # material physics
        self.IR = 0.0
        self.rigidity = 0.0
        self.color = []
    def assign_dt(self,dt):
        # this dt controls the change of speed of display of the change in the object position
        self.dt = dt
    def applyForce1(self,mag,direction):
        # create a new zero vector
        temp = vector((0,0,0),(0,0,0))
        # copying the direction vector to the temprary vector 
        temp.x,temp.y,temp.z = direction       
        # multiplying the vector to the magnitude
        temp.mult(mag)
        # copying the temp force to the force
        self.force.add(temp)
        # updating the acc
        self.updateAcc()
    def applyForce2(self,mag,direction):
        # create a new zero vector
        temp = vector((0,0,0),(0,0,0))
        # copying the direction vector to the temprary vector 
        temp.x,temp.y,temp.z = direction.x,direction.y,direction.z
        # multiplying the vector to the magnitude
        temp.mult(mag)
        # copying the temp force to the force
        self.force.add(temp)
        # updating the acc
        self.updateAcc()
    def applyForce(self,force):
        # adding force to object must be vector
        self.force.add(force)
        # dividing force by mass of object
        self.force.divide(self.mass)
        self.acc.add(self.force)
        # multipling the acc to delta time
        self.acc.mult(self.dt)
        self.velocity.add(self.acc)
    def copyForce(self,force):
        # adding force to object
        self.force.add(force)
        # updating the acc
        self.updateAcc()
    def realTimeForces(self,earthMass,dist):
        gravitation = (G * self.mass * earthMass)/ (dist**2)
        gForce = vector(0,-1,0)
        gForce.mult(gravitation)
        self.applyForce(gForce)
    def applyG(self):
        g = vector((0,0,0),(0,0,0))
        g.assign((0,0,0),(0,9.8,0))
        self.acc.add(g)
        
        # update the velocity
        self.updateVelocity()
    def applyAcc(self,acc):
        self.acc.add(acc)
        # multipling the acc to delta time
        # formula a = v/t
        self.acc.mult(self.dt)
        # update the velocity
        self.updateVelocity()
        #self.velocity.add(self.acc)
    def bound2d(self,window = []):
        # right
        if self.pos.x >= window[0] :
            
            self.velocity.reverseDir('x')
        #left    
        if self.pos.x <= 0 :
            
            self.velocity.reverseDir('x')
        #bottom    
        if self.pos.y >= window[1] :
            #self.pos.y = window[1]
            self.velocity.reverseDir('y')
        #top    
        if self.pos.y <= 0 :
            #sself.pos.y = 0
            self.velocity.reverseDir('y')
    def bound2d_swap(self,window = []):
        # right
        if self.pos.x >= window[0] :
            
            self.pos.x = 0+1
        #left    
        if self.pos.x <= 0 :
            
            self.pos.x = window[0]-1
        #bottom    
        if self.pos.y >= window[1] :
            #self.pos.y = window[1]
            self.pos.y = 0+1
        #top    
        if self.pos.y <= 0 :
            #sself.pos.y = 0
            self.pos.y = window[1]-1
    def bound3d_swap(self,mx,my,mz):
        # right
        if self.pos.x >= mx :
            
            self.pos.x = 0+1
        #left    
        if self.pos.x <= 0 :
            
            self.pos.x = mx-1
        #bottom    
        if self.pos.y >= my :
            #self.pos.y = window[1]
            self.pos.y = 0+1
        #top    
        if self.pos.y <= 0 :
            #sself.pos.y = 0
            self.pos.y = my-1
        # back
        if self.pos.z >= mz :
            self.pos.z = -mz+1
        # front
        if self.pos.z <= -mz:
            self.pos.z = mz-1
    def collision(self,window):
        # right
        if self.pos.x >= window[0] :
            self.pos.x = window[0]
            temp = vector((0,0,0),(0,0,0))
            temp.copy(self.acc)
            temp.mult(self.mass)
            direction = vector((0,0,0),(0,0,0))
            direction.copy(self.velocity)
            direction.normalized()
            direction.reverseDir('x')          
            self.applyForce2(temp.magCal(),direction)
        #left    
        if self.pos.x < 0 :
            self.pos.x = 0
            temp = vector((0,0,0),(0,0,0))
            temp.copy(self.acc)
            temp.mult(self.mass)
            direction = vector((0,0,0),(0,0,0))
            direction.copy(self.velocity)
            direction.normalized()
            direction.reverseDir('x')                
            self.applyForce2(temp.magCal(),direction)
        #bottom    
        if self.pos.y >= window[1] :
            self.pos.y = window[1]
            temp = vector((0,0,0),(0,0,0))
            temp.copy(self.acc)
            temp.mult(self.mass)
            direction = vector((0,0,0),(0,0,0))
            direction.copy(self.velocity)
            direction.normalized()
            direction.reverseDir('y')                
            self.applyForce2(temp.magCal(),direction)
        #top    
        if self.pos.y < 0 :
            self.pos.y = 0
            temp = vector((0,0,0),(0,0,0))
            temp.copy(self.acc)
            temp.mult(self.mass)
            direction = vector((0,0,0),(0,0,0))
            direction.copy(self.velocity)
            direction.normalized()
            direction.reverseDir('y')                
            self.applyForce2(temp.magCal(),direction)
    def updateAcc(self):
        # formula a = f/m
        # create a temp vector
        temp = vector((0,0,0),(0,0,0))
        # copying force in the temp
        temp.copy(self.force)
        # dividing force by mass of object
        temp.divide(self.mass)
        # copy the instatneous acc 
        self.acc.add(temp)
        # update the velocity
        self.updateVelocity()
    def updateVelocity(self):
        # formula v = u + (a* deltaT)
        # create a temp variable
        temp = vector((0,0,0),(0,0,0))
        # copy the acc to the temp
        temp.copy(self.acc)
        # multipling the acc to delta time
        temp.mult(self.dt)
        # updateing the velocity
        self.velocity.add(temp)
        # update the time
        self.time += self.dt
        
    def updatePos(self):

        if self.velocity.x != 0 or self.velocity.y != 0 or self.velocity.z != 0:
            self.pos.x += self.velocity.x*self.dt
            self.pos.y += self.velocity.y*self.dt
            self.pos.z += self.velocity.z*self.dt

'''
================================================================================
================================================================================
'''
def isSamePos(pos1,pos2):
    if pos1.x == pos2.x:
        if pos1.y == pos2.y:
            if pos1.z == pos2.z:
                return True
            else:
                return False
        else: return False
    else:
        return False

def dist(p1,p2):
    return math.sqrt(((p2.x-p1.x)**2) +((p2.y-p1.y)**2)+((p2.z-p1.z)**2))

'''
==========================================
    2d collision
==========================================
'''
x,y = 100,100

# clock wise order

surface1 = [[x+0,0+y],[x+100,0+y],[x+100,100+y],[x+0,100+y]]
surface2 = [[x+0+210,0+y+10],[x+100+210,0+y+10],[x+100+210,100+y+10],[x+0+210,100+y+10]]

def IsPointInside(x,y,left,right,top,bottom):


    if x > left and x < right:
        if y > top and y < bottom:
            return True
    else:
        return False
def IsPointInside(x,y,rect,h,w):


    if x > rect[0] and x < rect[0]+w:
        if y > rect[1] and y < rect[1]+h:
            return True
    else:
        return False


def IsCollied(rect1,rect2):
    # it returns true if rectangles collied each other

    left,right,top,bottom = rect2[0][0],rect2[1][0],rect2[1][1],rect2[3][1]

    for i in range(0,4):
        t = IsPointInside(rect1[i][0],rect1[i][1],left,right,top,bottom)
        if t == True:
            break
    if t == True:
        return True
    else:
        return False
# collision of two circular objects
def isInsideCir(pos1,r1,pos2,r2):
    if dist(pos1,pos2) > r1+r2:
        return False
    if dist(pos1,pos2) <= r1+r2:
        return True
#print IsCollied(surface1,surface2)
