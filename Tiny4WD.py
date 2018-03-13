#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
from explorerhat import motor
import time

class Tiny4WD:
    def __init__(self):
        self.maxPower  = 1.0
        self.power_left = 0.0
        self.power_right = 0.0
        self.x_axis = 0.0
        self.y_axis = 0.0

    def move_by_raw(self,right,left,seconds):
        motor.one.speed(-left)
        motor.two.speed(right)
        time.sleep(seconds)
        motor.stop()

    def forward(self):
        self.move_by_raw(100,100,.5)

    def backward(self):
	print("BT")
        self.move_by_raw(-100,-100,.5)
	print("BT END")

    def left(self):
        self.move_by_raw(-100,100,.25)

    def right(self):
        self.move_by_raw(100,-100,.25)

    def stop(self):
        motor.stop()


#def mixer(inYaw, inThrottle,):
#    left = inThrottle + inYaw
#    right = inThrottle - inYaw
#    scaleLeft = abs(left / 125.0)
#    scaleRight = abs(right / 125.0)
#    scaleMax = max(scaleLeft, scaleRight)
#    scaleMax = max(1, scaleMax)
#    out_left = int(constrain(left / scaleMax, -125, 125))
#    out_right = int(constrain(right / scaleMax, -125, 125))
#    results = [out_right, out_left]
#    return results

#def constrain(val, min_val, max_val):
#    return min(max_val, max(min_val, val))

#try:
#    print('Press CTRL+C to quit')
#    direction = 'F'

    # Loop indefinitely
#    while False:

#	if direction == 'F':
#	    y_axis = 200
 #           x_axis = 0
#
 #           mixer_results = mixer(x_axis, y_axis)
  #          #print (mixer_results)
   #         power_left = int((mixer_results[0] / 125.0)*100)
    #        power_right = int((mixer_results[1] / 125.0)*100)
     #       print("left: " + str(power_left) + " right: " + str(power_right))
#
 ##           motor.one.speed((-power_right * maxPower))
 #           motor.two.speed(power_left * maxPower)
#
#	    print("Sleep now")
#	    motor.stop()
#	    time.sleep(2)
#	    print("Wake up")
	    

#except KeyboardInterrupt:

    # CTRL+C exit, disable all drives
#    print("stop")
#    motor.stop()
#print("bye")
