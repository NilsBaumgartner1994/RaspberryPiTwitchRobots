import time 
from credentials import *
import os
from subprocess import call

imagename = 'CameraImageCapture'

def startStream():
    streamKey = TwitchStreamKey    

    bashCommand = "ffmpeg -loop 1 -framerate 15 -i "+imagename+".jpg -c:v libx264 -preset fast -pix_fmt yuv420p -threads 0 -f flv rtmp://live-fra.twitch.tv/app/"+streamKey
    os.system(bashCommand)

if __name__ == "__main__":
    startStream()
