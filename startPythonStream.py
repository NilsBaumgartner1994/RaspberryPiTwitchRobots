
## This Python script sends picamera video output to stout,
## it is intended to be called from a bash script which pipes
## the output into ffmpeg
 
## Bash script is startPythonStream.sh
 
import os
import time
import picamera
import sys
from signal import pause
from datetime import datetime
 
sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)
 
#---------------------------------------------------------
 
## Start capturing video
 
with picamera.PiCamera() as camera:
  camera.resolution = (960, 540)
  camera.framerate = 25
  camera.vflip = True
  camera.hflip = True
  camera.start_recording(sys.stdout, bitrate = 500000, format='h264')
  while True:
      i = datetime.now()
      now = i.strftime('%d %b %Y - %H:%M:%S')
      camera.annotate_text = 'ExplorerPi 1 Cam - ' + now + ' '
      camera.wait_recording(0.2)
