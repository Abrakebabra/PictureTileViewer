from PIL import Image
from PIL import ImageTk
import random


class ImageHandler():
    def __init__(self, imagePathList):
        self.imagePathList = imagePathList
        self.randSelection = list()
        self.images = list()

    def randGen(self):
        return random.randint(0, len(self.imagePathList) - 1)

    def randSelect(self):
        randNum = self.randGen()
        while randNum in self.randSelection:
            randNum = self.randGen()

        self.randSelection.append(randNum)

        return randNum

    def getSetImage(self, imagePath, sW, sH):
        imageFile = Image.open(imagePath)
        imgW, imgH = imageFile.size
        halfHeight = int(sH / 2)

        if imgW < imgH:
            if len(self.images) == 0:
                imgWP = int(imgW * (sH / imgH))
                imageResized = imageFile.resize(
                                                (imgWP, int(sH)),
                                                Image.ANTIALIAS
                                                )
            else:
                imgWP = int(imgW * (halfHeight / imgH))
                imageResized = imageFile.resize(
                                                (imgWP, halfHeight),
                                                Image.ANTIALIAS
                                                )
        elif imgW > imgH or imgW == imgH:
            imgWP = int(imgW * (halfHeight / imgH))
            imageResized = imageFile.resize(
                                            (imgWP, halfHeight),
                                            Image.ANTIALIAS
                                            )

        imageFile.close()

        return {"image": ImageTk.PhotoImage(imageResized),
                "width": imageResized.size[0],
                "height": imageResized.size[1]}

    def imageMulti(self, sW, sH):
        self.randSelection = []
        self.images = []
        widthTopRemain = sW
        widthBottomRemain = sW
        anotherImage = True
        if len(self.imagePathList) < 1:
            anotherImage = False

        while anotherImage is True:
            n = self.randSelect()
            print("image: " + str(n) + " of " + str(len(self.imagePathList)))
            imageReturn = self.getSetImage(self.imagePathList[n], sW, sH)
            image = imageReturn["image"]
            imgWidth = imageReturn["width"]
            imgHeight = imageReturn["height"]

            if widthTopRemain > 0:
                if imgHeight == sH:
                    xPos = sW - widthTopRemain
                    yPos = 0
                    widthTopRemain -= imgWidth
                    widthBottomRemain -= imgWidth
                else:
                    xPos = sW - widthTopRemain
                    yPos = 0
                    widthTopRemain -= imgWidth
            elif widthTopRemain <= 0:
                xPos = sW - widthBottomRemain
                yPos = sH / 2
                widthBottomRemain -= imgWidth



            if widthBottomRemain <= 0:
                anotherImage = False

            self.images.append({"image": image,
                                "xPos": xPos, "yPos": yPos})

        return self.images
