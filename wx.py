

import wx

class myFrame(wx.wxFrame):
   
    
        def play(self, filename):
           import sys
            ##Note we call the GetHandle() method of a control in the window/frame, not the wxFrame itself
           self.hwnd = self.GetChildren()[0].GetHandle()
           if sys.platform == "win32":
                os.environ['SDL_VIDEODRIVER'] = 'windib'
           os.environ['SDL_WINDOWID'] = str(self.hwnd) #must be before init
   
           ## NOTE WE DON'T IMPORT PYGAME UNTIL NOW.  Don't put "import pygame" at the top of the file.
           import pygame
           pygame.display.init()
    
           self.movie = pygame.movie.Movie(filename)
   
           if self.movie.has_video():
               w,h = self.movie.get_size()
               if w<=0 or h<=0: w,h = 1,1
           else:
               #? need something to display if audio only.
               #We can't have a 0,0 canvas, pygame/SDL doesn't like that.
               w,h = 1,1
           self.display = pygame.display.set_mode((w,h)) #size no matter
   
           self.movie.set_display(self.display)
           self.movie.play()
