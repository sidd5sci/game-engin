


def translate3d(_object_,pos):
        # calculate the translations dx,dy,dz
        dx = pos[0]-_object_.pos.x
        dy = pos[1]-_object_.pos.y
        dz = pos[2]-_object_.pos.z
        #print _object_,dx,dy,dz
        _object_.pos.x,_object_.pos.y,_object_.pos.z = pos
        if dx!= 0 or dy!= 0 or dz!= 0:
            for i in range(0,len(_object_.vertex)):
                _object_.vertex[i][0] += dx
                _object_.vertex[i][1] += dy
                _object_.vertex[i][2] += dz
                
def translate3d_t(_object_,pos):
        # calculate the translations dx,dy,dz
        dx,dy,dz = pos
        #print _object_,dx,dy,dz
        _object_.pos.x += pos[0]
        _object_.pos.y += pos[1]
        _object_.pos.z += pos[2]
        if dx!= 0 or dy!= 0 or dz!= 0:
            for i in range(0,len(_object_.vertex)):
                _object_.vertex[i][0] += dx
                _object_.vertex[i][1] += dy
                _object_.vertex[i][2] += dz
                
def rotate3d(_object_,axis,dtheta,radius = 0):
        dx,dy,dz  = _object.pos.get()
        translate3d_t(_object_,(-dx,-dy,-dz))
        c,s = math.cos(dtheta),math.sin(dtheta)
        if axis == 'x':
            for i in range(0,len(_object_.vertex)):
                temp = _object_.vertex[i][1]
                _object_.vertex[i][1] =  _object_.vertex[i][1]*c - _object_.vertex[i][2]*s
                _object_.vertex[i][2] =  temp*s + _object_.vertex[i][2]*c
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
        translate3d_t(_object_,(dx,dy,dz))
def scale3d(_object_,scale):
        sx,sy,sz = scale
        for i in range(0,len(_object_.vertex)):
            _object_.vertex[i][0] += _object_.vertex[i][0]*sx
            _object_.vertex[i][1] += _object_.vertex[i][1]*sy
            _object_.vertex[i][2] += _object_.vertex[i][2]*sz 
