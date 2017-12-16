
import Tkinter as tk
from Tkinter import *
import os
#from tkFileDilog import askopenfilename






################################################################
def key(event):
    print "key",repr(event.char)

def buttons():
    pass
def newObject():
    print 'objects list '
def newFile():
    print 'new file'

def fileOpen():
    print 'open file'
def about():
    
    print 'about the game engin'
################################################################
#initilise the GUI of tkinter
root = tk.Tk()
buttonwin = tk.Frame(root, width = 200, height = 600)
buttonwin.pack(side = LEFT)
embed = tk.Frame(root, width = 800, height = 600) #creates embed frame for pygame window
embed.grid(columnspan = 600, rowspan = 400, row=4,column=1) # Adds grid

buttonwin.bind_all("<Key>",key)
embed.pack(side = LEFT,fill=Y) #packs window to the left
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'


from opengl_loader import *


# creating the menu for GUI
menu = Menu(root)
root.config(menu=menu)
# file menu option
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label = "New" , command=newFile)
filemenu.add_command(label = "Open" , command=fileOpen)
filemenu.add_command(label = "Create" , command=newObject)
filemenu.add_separator()
filemenu.add_command(label = "Exit" , command=root.quit)
# create menu
createmenu = Menu(menu)
menu.add_cascade(label="Create", menu=createmenu)
createmenu.add_command(label="Cube", command=about)
createmenu.add_command(label="Cone", command=about)
createmenu.add_command(label="Cylinder", command=about)
createmenu.add_command(label="Sphere", command=about)
createmenu.add_command(label="Plane", command=about)
createmenu.add_command(label="Human", command=about)
createmenu.add_separator()
createmenu.add_command(label="Light", command=about)
createmenu.add_command(label="Spot light", command=about)
createmenu.add_command(label="Area light", command=about)
createmenu.add_separator()
createmenu.add_command(label="Camera", command=about)
# help menu option
helpmenu = Menu(menu)
menu.add_cascade(label="Help" ,menu = helpmenu)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Version", command=about)
helpmenu.add_command(label="Update", command=about)



       
if __name__ == '__main__':

    
    while (1):
       main()
       root.update()
