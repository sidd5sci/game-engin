import wx
from wx import glcanvas

class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self,parent):
        glcanvas.GLCanvas.__init__(self,parent,-1,size=(1120,630))


class MyFrame(wx.Frame):
    def __init__(self):
        self.size = (1280,720)
        wx.Frame.__init__(self,None,title="",size=self.size)
        self.canvas = OpenGLCanvas(self)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
