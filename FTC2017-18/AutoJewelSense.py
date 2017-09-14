#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *

#--Initialize--
#b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
gamepadA = gamepad1
gamepadB = gamepad2

#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *

#--Initialize--
#b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
gamepadA = gamepad1
gamepadB = gamepad2

#Front motors?
motorRight = hardwareMap.DcMotor( b, nxt.PORT_1, 1)
motorLeft = hardwareMap.DcMotor( b, nxt.PORT_1, 2)
#Back motors?
motorRight1 = hardwareMap.DcMotor( b, nxt.PORT_2, 1)
motorLeft1 = hardwareMap.DcMotor( b, nxt.PORT_2, 2)

def r_motorPower(): # Multicontroller admin-dpad&left_stick user-left_stick
    #admin dpad has cardinal control
    left_stick_x = 1 if gamepadA.dpad_right else 0
    left_stick_y = 1 if gamepadA.dpad_down else 0
    left_stick_x -= 1 if gamepadA.dpad_left else 0
    left_stick_y -= 1 if gamepadA.dpad_up else 0

    #user and admin have left stick normal control
    right_stick_x = gamepadB.left_stick_x + gamepadA.left_stick_x
    right_stick_y = gamepadB.left_stick_y + gamepadA.left_stick_y


    left_x = Range.clip(left_stick_x,-1,1)
    left_y = Range.clip(left_stick_y,-1,1)
    right_x  = Range.clip(right_stick_x,-1,1)
    right_y = Range.clip(right_stick_y,-1,1)

    #left stick controls cardinal direction.  right stick has forward/back and rotation
    #Front power
    powRight =  Range.clip( left_y + right_y + left_x + right_x , -1 , 1 )
    powLeft =   Range.clip( left_y + right_y - left_x - right_x , -1 , 1 )
    #Back power
    powRight1 = Range.clip( left_y + right_y - left_x + right_x , -1 , 1 )
    powLeft1 =  Range.clip( left_y + right_y + left_x - right_x , -1 , 1 )

    motorRight.setPower(-powRight)
    motorLeft.setPower(powLeft)
    motorRight1.setPower(-powRight1)
    motorLeft1.setPower(powLeft1)
def r_senseTest():
    pass
while 1:
    pass
    r_motorPower()
    r_senseTest()
    if(gamepadA.left_stick_button or gamepadA.right_stick_button):
        print motorLeft.get_battery_voltage()