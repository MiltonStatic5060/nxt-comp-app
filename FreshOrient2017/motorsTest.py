#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *
from time import sleep
#--Initialize--
b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
#b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060

motorLeft = nxt.Motor(b, nxt.PORT_A)
motorCenter = nxt.Motor(b, nxt.PORT_B)
motorRight = nxt.Motor(b, nxt.PORT_C)
# .run() 0-100 value

touch = nxt.sensor.generic.Touch(b,PORT_1)
ultrasonic = nxt.sensor.generic.Ultrasonic(b,PORT_2)

while 1:
    if(touch.is_pressed()):
        motorLeft.run(Range.clip(ultrasonic.get_distance()*40.0/255.0+60,0,100))
        motorRight.run(Range.clip(ultrasonic.get_distance()*40.0/255.0+60,0,100))
        motorCenter.run(-Range.clip(ultrasonic.get_distance()*40.0/255.0+60,0,100))
    else:
        motorLeft.run(Range.clip(gamepad1.left_stick_y*100,-100,100))
        motorCenter.run(Range.clip(gamepad1.left_stick_y*100,-100,100))
        motorRight.run(Range.clip(gamepad1.right_stick_y*100,-100,100))

    print Range.clip(gamepad1.left_stick_y*100,-100,100)
