#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *

#--Initialize--
#b1 = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060

# motorRight = DcMotor( b, nxt.PORT_1, 1)
# motorLeft = DcMotor( b, nxt.PORT_1, 2)
# motorRight1 = DcMotor( b, nxt.PORT_2, 1)
# motorLeft1 = DcMotor( b, nxt.PORT_2, 2)
#
# minionLights = DcMotor( b, nxt.PORT_3, 1)

def r_motorPower():
    left_x = Range.clip(gamepad1.left_stick_x,-1,1)
    left_y = Range.clip(gamepad1.left_stick_y,-1,1)
    right_x  = Range.clip(gamepad1.right_stick_x,-1,1)
    right_y = Range.clip(gamepad1.right_stick_y,-1,1)

    powRight =  Range.clip( left_y + right_y + left_x - right_x , -1 , 1 )
    powLeft =   Range.clip( left_y + right_y - left_x + right_x , -1 , 1 )
    powRight1 = Range.clip( left_y + right_y + left_x + right_x , -1 , 1 )
    powLeft1 =  Range.clip( left_y + right_y - left_x - right_x , -1 , 1 )

    motorRight.setPower(powRight)
    motorLeft.setPower(powLeft)
    motorRight1.setPower(powRight1)
    motorLeft1.setPower(powLeft1)
def soundPlayer():
    #Sound Controller
    arr = [gamepad1.dpad_up,gamepad1.dpad_right,gamepad1.dpad_down,gamepad1.dpad_left]
    for i in range(len(arr)):
		if arr[i]:
			SoundBrick.Player(b).playSoundSample(i,120)
SoundBrick.Player(b).success()
while 1:
    #r_motorPower()
    #minionLights.setPower(Range.clip(gamepad1.left_trigger+gamepad1.right_trigger,-1,1))
    soundPlayer()
