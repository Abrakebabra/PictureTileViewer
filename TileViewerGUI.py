import tkinter as tk

import ImageHandler

#import os
#picturePaths = []  # clear data
#directory = "/Users/keithlee/Documents/Python/Photos"
#files = os.listdir(directory)
#for i in files:
#    if i.lower().endswith(".jpg") or\
#       i.lower().endswith(".jpeg") or\
#       i.lower().endswith("gif"):
#        picturePaths.append(os.path.join(directory, i))


class Canvas():

    def __init__(self, imagePathList):
        self.root = tk.Tk()
        self.wRatio = 0.90
        self.hRatio = 0.90
        self.getScreenWidth = self.root.winfo_screenwidth()
        self.getScreenHeight = self.root.winfo_screenheight()
        self.sW = self.wRatio * self.getScreenWidth
        self.sH = self.hRatio * self.getScreenHeight
        self.sX = (self.getScreenWidth / 2) - (self.sW / 2)
        self.sY = (self.getScreenHeight / 2) - (self.sH / 2)

        self.root.title("Main Window")
        self.root.geometry("%dx%d+%d+%d" % (self.sW, self.sH,
                                            self.sX, self.sY))
        self.c = tk.Canvas(self.root, width=self.sW, height=self.sH,
                           highlightthickness=0)
        self.c.place(x=0, y=0)

        self.imageHandler = ImageHandler.ImageHandler(imagePathList)
        self.images = None

    def clearCanvas(self):
        self.c.delete("all")

    def drawImages(self):
        self.clearCanvas()
        self.images = self.imageHandler.imageMulti(self.sW, self.sH)
        for i in range(0, len(self.images)):
            self.c.create_image(int(self.images[i]["xPos"]), int(self.images[i]["yPos"]),
                                image=self.images[i]["image"], anchor="nw")

    def destroyRoot(self):
        self.root.destroy()

    def windowClosed(self):
        self.root.protocol("WM_DELETE_WINDOW", self.destroyRoot)

    def refresh(self, *args):
        print("refresh")
        self.drawImages()
        
    def mainLoop(self):
        self.windowClosed()
        self.root.bind("<Up>", self.refresh)
        self.root.mainloop()


#testCanvas = Canvas(picturePaths)
#testCanvas.drawImages()
#testCanvas.mainLoop()
