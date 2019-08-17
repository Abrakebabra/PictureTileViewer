import tkinter
import os
import TileViewerGUI


currentDir = os.getcwd()
dataPaths = list()
data = list()
picturePaths = list()


class Explorer:

    def __init__(self):
        self.allList = list()  # list of all scanned items or item paths
        self.dirList = list()  # list of all folders or folder paths
        self.fileList = list()  # list of all files or files paths

    def clearData(self):
        self.allList = []
        self.dirList = []
        self.fileList = []

    def scanPaths(self, inputDir, depth=""):
        # a list of all folder and file names in inputDirectory
        surfaceItems = os.listdir(inputDir)

        for i in range(0, len(surfaceItems)):
            fullPath = os.path.join(inputDir, surfaceItems[i])
            self.allList.append(fullPath)

            if depth == "deep":
                # if there is a directory within another directory, recurse
                if os.path.isdir(fullPath):
                    self.scanPaths(fullPath, "deep")

    def splitItems(self):
        # separate items into separate lists of folders and files
        if len(self.dirList) == 0 or len(self.fileList) == 0:
            for i in range(0, len(self.allList)):
                if os.path.isdir(self.allList[i]):
                    self.dirList.append(self.allList[i])

                elif os.path.isfile(self.allList[i]):
                    self.fileList.append(self.allList[i])

    def itemNameOnly(self, dataList):
        # remove path names and only have base names
        if dataList == "allList":
            for i in range(0, len(self.allList)):
                self.allList[i] = os.path.basename(self.allList[i])

        if dataList == "allList" or "dirList":
            for i in range(0, len(self.dirList)):
                self.dirList[i] = os.path.basename(self.dirList[i])

        if dataList == "allList" or "fileList":
            for i in range(0, len(self.fileList)):
                self.fileList[i] = os.path.basename(self.fileList[i])

    def countItemType(self):
        # show count number for documents and files
        self.dirCount = int()
        self.fileCount = int()

        for i in self.allList:
            if os.path.isdir(i):
                self.dirCount += 1

            elif os.path.isfile(i):
                self.fileCount += 1

    def returnData(self, rType="print", rData="all", path=""):
        # with rType on rData:
        #   with "return", "print" or "length" (number of rData)
        #   on "all", "files" or "folers"
        #   path set to none, but if "yes", will print full path names
        # kind of information needed

        if rType == "return":
            if rData == "all":
                return self.allList

            elif rData == "files" or "folders":
                self.splitItems()

                if rData == "folders":
                    return self.dirList

                elif rData == "files":
                    return self.fileList

        elif rType == "print":
            self.splitItems()

            if rData == "all":
                if path == "noPath":
                    self.itemNameOnly("allList")
                print("===== Folders =====")
                print(*self.dirList, sep="\n")
                print("\n===== Files =====")
                print(*self.fileList, sep="\n")

            elif rData == "folders":
                if path == "noPath":
                    self.itemNameOnly("dirList")
                print("===== Folders =====")
                print(*self.dirList, sep="\n")

            elif rData == "files":
                if path == "noPath":
                    self.itemNameOnly("fileList")
                print("===== Files =====")
                print(*self.fileList, sep="\n")

        elif rType == "length":
            self.countItemType()
            if rData == "all":
                print(str(self.dirCount) + " folders")
                print(str(self.fileCount) + " files")

            elif rData == "folders":
                print(str(self.dirCount) + " folders")

            elif rData == "files":
                print(str(self.fileCount) + " files")


scanner = Explorer()

testVar1 = None
testVar2 = list()

def runProgram():
    global currentDir
    global dataPaths
    global data
    global testVar1
    global testVar2

    while True:
        print("\nCurrently in " + currentDir, end="\n\n")
        print("\nall, folders, files, count, pictures, <folder name>, back, exit")
        userInput = input()

        if userInput == "exit":
            print("Laters.")
            break

        elif userInput == "back":
            currentDir = os.path.dirname(currentDir)
            scanner.clearData()
            scanner.scanPaths(currentDir)
            scanner.returnData("print", "folders", "noPath")
            if len(scanner.dirList) == 0:
                print("No folders.")

        elif userInput == "count":
            scanner.clearData()
            scanner.scanPaths(currentDir, "deep")
            scanner.returnData("length", "all")

        elif userInput == "all":
            scanner.clearData()
            scanner.scanPaths(currentDir)
            scanner.returnData("print", "all", "noPath")

        elif userInput == "folders":
            scanner.clearData()
            scanner.scanPaths(currentDir)
            scanner.returnData("print", "folders", "noPath")
            if len(scanner.dirList) == 0:
                print("No folders.")

        elif userInput == "files":
            scanner.clearData()
            scanner.scanPaths(currentDir)
            scanner.returnData("print", "files", "noPath")

        elif userInput == "pictures":
            scanner.clearData()
            scanner.scanPaths(currentDir, "deep")
            picturePaths = []  # clear data
            files = scanner.returnData("return", "files")
            testVar1 = files
            for i in files:
                if i.lower().endswith(".jpg") or\
                   i.lower().endswith(".jpeg") or\
                   i.lower().endswith("gif"):
                    picturePaths.append(i)
                    testVar2.append(i)
            window = TileViewerGUI.Canvas(picturePaths)
            window.drawImages()
            window.mainLoop()

        else:
            if userInput in os.listdir(currentDir):
                if os.path.isdir(os.path.join(currentDir, userInput)):
                    currentDir = os.path.join(currentDir, userInput)
                    scanner.clearData()
                    scanner.scanPaths(currentDir)
                    scanner.returnData("print", "folders", "noPath")
                    if len(scanner.dirList) == 0:
                        print("No folders.")

            else:
                print("No such folder")
                continue


runProgram()
