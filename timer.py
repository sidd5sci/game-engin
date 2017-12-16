
'''
timer controls different assets of game 
for how long the asset remain in the game
'''
class timer:

    def __init__(self,name = 'none',beg = 100.0,end = 00.0,rate = 5.0):
        self.name = name
        self.begAt = beg # beg value is > 0
        self.timer = beg
        self.endAt = end # end value is < 100
        self.rate = rate # rate vale can be any
    def update(self):
        self.timer -= self.rate
        self.checkEnd()
    def checkEnd(self):
        if self.timer <= self.endAt:
           self.timer = self.endAt
    def beginTimer(self,name = 'none',beg = 100.0,end = 00.0,rate = 5.0):
        self.name = name
        self.begAt = beg # beg value is > 0
        self.timer = beg
        self.endAt = end # end value is < 100
        self.rate = rate # rate vale can be any
    def setEnd(self,endAt):
        self.endAt = endAt
    def setbeg(self,beg):
        self.begAt = beg
    def setName(self,name):
        self.name = name
