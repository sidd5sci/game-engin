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
