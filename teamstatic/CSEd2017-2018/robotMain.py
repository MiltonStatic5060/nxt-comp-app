#import packages for Gamepad Control and Motor Controls
from nxttools import sound as SoundBrick
from nxttools import rangetools as Range
from nxttools import hardware as hardwareMap
from nxttools.gamepad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *

#--Initialize--
# b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
gamepadA = gamepad1
gamepadB = gamepad2

#Front motors
motorRight = hardwareMap.DcMotor( b, nxt.PORT_1, 1)
motorLeft = hardwareMap.DcMotor( b, nxt.PORT_1, 2)
#Back motors
motorRight1 = hardwareMap.DcMotor( b, nxt.PORT_2, 1)
motorLeft1 = hardwareMap.DcMotor( b, nxt.PORT_2, 2)

#Block Grabber
ServoCon(b,PORT_4).set_pwm(0)
blockGrabL = hardwareMap.Servo( b, nxt.PORT_4, 1)
blockGrabR = hardwareMap.Servo( b, nxt.PORT_4, 2)
blockLift = hardwareMap.DcMotor( b, nxt.PORT_3, 1)
relicLift = hardwareMap.DcMotor( b, nxt.PORT_3, 2)

blockLift.set_mode(4) # reset encoder
blockLift.set_enc_target(0) # set target to 0
blockLift.set_mode(3) # run to position

relicLift.set_mode(4) # reset encoder
relicLift.set_enc_target(0) # set target to 0
relicLift.set_mode(3) # run to position

armSwitch = False

relicLift.setPower(0.5)
blockLift.setPower(0.5)
def r_grabber():
    global armSwitch
    #blockGrabL blockGrabR blockLift
    right_trigger = gamepadA.right_trigger
    if(react.is_diff("blockGrabL",0,Range.clip(right_trigger*255,0,255-130))):
        blockGrabL.setPosition(react.get_val("blockGrabL"))
    if(react.is_diff("blockGrabR",255,Range.clip((1.0-right_trigger)*255,130,255))):
        blockGrabR.setPosition(react.get_val("blockGrabR"))
    
    #TEMPORARY
    # right_stick_y = gamepadA.right_stick_y
    if(not armSwitch):
        if(react.is_diff("blockLift",0,gamepadA.left_trigger*-2880)):
            blockLift.set_enc_target(react.get_val("blockLift"))
    armSwitch = gamepad1.back
    if(gamepad1.guide):
        blockLift.set_power(gamepad1.right_stick_y)
    # print blockLift.get_enc_current(),
    # print blockLift.get_enc_target()
    # blockLift.setPower(0.5)
    # relicLift.setPower(0.5)
    if(armSwitch):
        if(react.is_diff("relicLift",0,gamepadA.left_trigger*1440/4.0)):
            relicLift.set_enc_target(react.get_val("relicLift"))
    

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

    if(react.is_diff("motorRight",0,-powRight)):
        motorRight.setPower(-powRight)

    if(react.is_diff("motorLeft",0,powLeft)):
        motorLeft.setPower(powLeft)
        
    if(react.is_diff("motorRight1",0,-powRight1)):
        motorRight1.setPower(-powRight1)

    if(react.is_diff("motorLeft1",0,powLeft1)):
        motorLeft1.setPower(powLeft1)
counter = 0