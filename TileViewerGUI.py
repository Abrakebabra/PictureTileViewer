import tkinter as tk

import ImageHandler


class Canvas():

    def __init__(self, imagePathList):
        self.root = tk.Tk()
        self.wRatio = 1
        self.hRatio = 0.97
        self.getScreenWidth = self.root.winfo_screenwidth()
        self.getScreenHeight = self.root.winfo_screenheight()
        self.sW = self.wRatio * self.getScreenWidth
        self.sH = self.hRatio * self.getScreenHeight
        self.sX = (self.getScreenWidth / 2) - (self.sW / 2)
        self.sY = 0

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
            self.c.create_image(int(self.images[i]["xPos"]),
                                int(self.images[i]["yPos"]),
                                image=self.images[i]["image"], anchor="nw")

    def destroyRoot(self):
        self.root.destroy()

    def windowClosed(self):
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        print("Root Destroyed")

    def refresh(self, *args):
        print("Refresh")
        self.drawImages()

    def close(self, *args):
        print("Close")
        self.root.destroy()

    def mainLoop(self):
        self.windowClosed()
        self.root.bind("<Up>", self.refresh)
        self.root.bind("<Down>", self.close)
        self.root.mainloop()
