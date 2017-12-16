from vector import vertex

class Cursor():
    def __init__(self,pos,color):
        self.pos = vertex(pos)
        self.color = color
    def get(self):
        return self.pos.get()
    def setPos(self,pos):
        self.pos = vertex(pos)
    
