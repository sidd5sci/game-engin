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





# object animation scripter
# here the


import sys,os
from objloader import *


class OBJ:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        material = None
        
        filepath = sys.path[0] # current directory path
        directory = os.path.normpath(filepath)
        for subdir, dirs, files in os.walk(directory):
            print subdir,dirs
            for file in files:
                #if file.endswith(".obj"):
                    if file == filename+'.obj':
                        print 'hg'
                        for line in open(os.path.join(subdir, file), "r"):
                            if line.startswith('#'): continue
                            values = line.split()
                            if not values: continue
                            if values[0] == 'v':
                                v = map(float, values[1:4])
                                if swapyz:
                                    v = v[0], v[2], v[1]
                                self.vertices.append(v)
                            elif values[0] == 'vn':
                                v = map(float, values[1:4])
                                if swapyz:
                                    v = v[0], v[2], v[1]
                                self.normals.append(v)
                            elif values[0] == 'vt':
                                self.texcoords.append(map(float, values[1:3]))
                            elif values[0] in ('usemtl', 'usemat'):
                                material = values[1]
                            elif values[0] == 'mtllib':
                                #self.mtl = MTL(values[1])
                                pass
                            elif values[0] == 'f':
                                face = []
                                texcoords = []
                                norms = []
                                for v in values[1:]:
                                    w = v.split('/')
                                    face.append(int(w[0]))
                                    if len(w) >= 2 and len(w[1]) > 0:
                                        texcoords.append(int(w[1]))
                                    else:
                                        texcoords.append(0)
                                    if len(w) >= 3 and len(w[2]) > 0:
                                        norms.append(int(w[2]))
                                    else:
                                        norms.append(0)
                                self.faces.append((face, norms, texcoords, material))

                
def export(filename,ext,_class_object_,header_content):
    name_ext = filename+ext
    with open(name_ext,'w') as f:
         f.write(header_content)
         f.write(_class_object_)
         f.close()

def _import(filename,ext,header_length):
    name_ext = filename + ext
    with open(name_ext,'r') as f:
         header = f.read(header_length)
         _class_object_ = f.read()
         f.close()

def loadObject(name,ext):
    filename = input("Enter filename")
    obj = OBJ(filename)
    header_content = "vertex list/face list"
    name_ext = name+ext
    with open(name_ext,'w') as f:
         f.write(header_content)
         f.write("vertices")
         for v in obj.vertices:
             f.write(str(v))
             f.write('\n')
         f.write("faces")
         for face in obj.faces:
             f.write(str(face[0]))
             f.write('\n')
         f.close()

if __name__ == '__main__':
    path = sys.argv[0] # path of this file 
    path1 = sys.path[0] # current directory path
    path1 = path1+'\object_lib'
    print path1,'\n'
    loadObject('circle','.burn')
    
