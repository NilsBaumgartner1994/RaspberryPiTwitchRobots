import time 
import threading
import os
from subprocess import call

imagename = 'CameraImageCapture'

def makeScreenShot():
    global imagename
    bashCommand = "raspistill -o "+imagename+".jpg"
    os.system(bashCommand)
    #call(["screencapture", imagename+"2.jpg"])
    #os.rename(imagename+"2.jpg", imagename+".jpg")

def startMain():
    while(True):
        makeScreenShot()
        time.sleep(10)    

if __name__ == "__main__":
    startMain()

