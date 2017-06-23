# object animation scripter
# here the

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