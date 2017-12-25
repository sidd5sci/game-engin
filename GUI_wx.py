
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





import wx

class MyFrame(wx.Frame):   
        def __init__(self):
            self.size = (600,400)
            wx.Frame.__init__(self,None,title="",size=self.size)
            
        def play(self, filename):
           import sys,os
            ##Note we call the GetHandle() method of a control in the window/frame, not the wxFrame itself
           self.hwnd = self.GetChildren()
           if sys.platform == "win32":
                os.environ['SDL_VIDEODRIVER'] = 'windib'
           os.environ['SDL_WINDOWID'] = str(self.hwnd) #must be before init
           from game_engine import *
           ## NOTE WE DON'T IMPORT PYGAME UNTIL NOW.  Don't put "import pygame" at the top of the file.
##           import pygame
##           pygame.display.init()
##    
##           self.movie = pygame.movie.Movie(filename)
##   
##           if self.movie.has_video():
##               w,h = self.movie.get_size()
##               if w<=0 or h<=0: w,h = 1,1
##           else:
##               #? need something to display if audio only.
##               #We can't have a 0,0 canvas, pygame/SDL doesn't like that.
##               w,h = 1,1
##           self.display = pygame.display.set_mode((w,h)) #size no matter
##      
##           self.movie.set_display(self.display)
##           self.movie.play()
        

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        frame.play('dfd')
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

    
