from tkinter import *
from PIL import Image, ImageTk
import glob
import shutil

unproccessedImages = glob.glob("Unproccessed Images/*") #assuming all files are image files
i = 0
class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # change title
        self.master.title("Manual Image Filter")
        self.pack(fill=BOTH, expand=1)

        discardButton = Button(self, text="Discard", command=self.discard)
        discardButton.grid(row=1, column=0, sticky=W+E+S)
        keepButton = Button(self, text="Keep", command=self.keep)
        keepButton.grid(row=1, column=1, stick=W+E+S)
        zooButton = Button(self, text="Keep", command=self.keepZoo)
        zooButton.grid(row=1, column=2, stick=W+E+S)

        self.showImg()

    def showImg(self):
        load = Image.open(unproccessedImages[i])
        load = load.resize((1000, 650), Image.ANTIALIAS)  # resize the image
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.grid(row=0, columnspan=3, sticky=W+E+N+S)


    def discard(self):
        self.changeImage() 
        self.moveImageToReject()
        
    
    def keep(self):
        self.changeImage()
        self.moveImageToAccept()

    def keepZoo(self):
        self.changeImage()
        self.moveImageToZoo()

    def changeImage(self):
        global i 
        i += 1  
        if (i >= len(unproccessedImages)):
            print("There are no more unprocessed images")
            img = Label(self, text="There are no more unprocessed images")
            img.grid(row=0, columnspan=2, sticky=W+E+N+S)
            return
        self.showImg()

    def moveImageToAccept(self):
        shutil.move(unproccessedImages[i-1], "Accept/")

    def moveImageToReject(self):
       shutil.move(unproccessedImages[i-1], "Reject/")
    
    def moveImageToZoo(self):
       shutil.move(unproccessedImages[i-1], "Zoo/") 
    





root = Tk()
root.geometry('1000x700')
app = Window(root)
root.mainloop()
