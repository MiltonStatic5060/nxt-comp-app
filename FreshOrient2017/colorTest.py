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

color = nxt.sensor.generic.Color20(b,PORT_1)
touch = nxt.sensor.generic.Touch(b,PORT_2)
sound = nxt.sensor.generic.Sound(b,PORT_3)
ultrasonic = nxt.sensor.generic.Ultrasonic(b,PORT_4)

x = 0
y = 0
while 1:
    if gamepad1.a: x = 0
    if gamepad1.b: x = 1
    if gamepad1.y: x = 2
    if gamepad1.x: x = 3
    if gamepad1.dpad_down: x = 4
    if gamepad1.dpad_up: x = 5

    colArr = [Type.COLORFULL,Type.COLORRED,Type.COLORBLUE,Type.COLORGREEN,Type.COLORNONE,Type.COLOREXIT]

    y = int(gamepad1.left_stick_y-1*-2.5)

    arr = []
    try:
        arr.append(color.get_light_color())
        arr.append(color.get_color())
        arr.append(touch.is_pressed())
        arr.append(sound.get_loudness())
        arr.append(ultrasonic.get_distance())
        arr.append(color.get_reflected_light(colArr[y]))
    except:
        print "sensor error"
    #COLORFULL COLORRED COLORBLUE COLORGREEN
    #COLORNONE COLOREXIT

    print(arr[x])
