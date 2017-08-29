#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *

#--Initialize--
b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
#b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
gamepadA = gamepad3
gamepadB = gamepad4

motorLeft = nxt.Motor(b, nxt.PORT_A)
motorCenter = nxt.Motor(b, nxt.PORT_B)
motorRight = nxt.Motor(b, nxt.PORT_C)

motorRotate = hardwareMap.DcMotor(b, PORT_4, 2)
motorCat    = hardwareMap.DcMotor(b, PORT_4, 1)

touch1 = nxt.sensor.generic.Touch(b,PORT_1)
touch2 = nxt.sensor.generic.Touch(b,PORT_3)
ultrasonic   = nxt.sensor.generic.Ultrasonic(b,PORT_2)

soundplayer = SoundBrick.Player(b)
arr = []

def soundPlayer():
    #Sound Controller

    sound1 = gamepadA.a or gamepadB.a
    sound2 = gamepadA.b or gamepadB.b
    sound3 = gamepadA.y or gamepadB.y
    sound4 = gamepadA.x or gamepadB.x

    arr = [sound1,sound2,sound3,sound4]
    for i in range(len(arr)):
		if arr[i]:
			soundplayer.playSoundSample(i,120) # Multicontroller Controllers same for both user and admin
def r_motorPower(): # Multicontroller just admin now
    left_trigger  = Range.clip(gamepadA.left_trigger,0,1)
    right_trigger = Range.clip(gamepadA.right_trigger,0,1)
    left_bumper   = gamepadA.left_bumper
    right_bumper  = gamepadA.right_bumper

    motorCat.setPower(Range.clip(left_trigger-right_trigger,-1,1))
    if left_bumper:
        motorRotate.setPower(0.1)
    elif right_bumper:
        motorRotate.setPower(-0.1)
    else:
        motorRotate.setPower(0)
def r_nxtCtl(): # Multicontroller available
    dpad_up = gamepadA.dpad_up
    dpad_down = gamepadA.dpad_down
    left_stick_y = gamepadA.left_stick_y
    right_stick_y = gamepadA.right_stick_y

    powLeft = (Range.clip(left_stick_y*100,-100,100))
    powRight = (Range.clip(right_stick_y*100,-100,100))
    powCenter = 0
    if(dpad_up): powCenter += 99
    if(dpad_down): powCenter -= 99

    if(touch1.is_pressed()):
        powLeft = (Range.clip(ultrasonic.get_distance()*40.0/255.0+60,0,100))
        print powLeft
    if(touch2.is_pressed()):
        powRight = (Range.clip(ultrasonic.get_distance()*40.0/255.0+60,0,100))
        print powRight
    if( touch1.is_pressed() or touch2.is_pressed() ):
        powCenter = (-Range.clip(ultrasonic.get_distance()*40.0/255.0+60,0,100))
        print powCenter


    motorLeft.run(powLeft)
    motorRight.run(powRight)
    motorCenter.run(powCenter)

while 1:
    r_motorPower()
    r_nxtCtl()
    soundPlayer()
