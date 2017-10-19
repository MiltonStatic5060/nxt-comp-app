#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *
from NxtCtl.React import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *

#--Initialize--
b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
# b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
gamepadA = gamepad1
gamepadB = gamepad2

motorLeft = nxt.Motor(b,nxt.PORT_A)
motorRight = nxt.Motor(b,nxt.PORT_B)


while 1:
    
    # if(gamepadA.left_bumper):
    #     set_val("motorLeft_pow",[2*(gamepadA.left_trigger-0.5)*99, 0])
    # if(gamepadA.right_bumper):
    #     set_val("motorRight_pow",[2*(gamepadA.right_trigger-0.5)*99, 0])
    
    if(react.is_diff("motorLeft_pow",0,gamepadA.left_stick_y*99)):
        print react.CURRSTATE
        motorLeft.run(react.get_val("motorLeft_pow"))
    if(react.is_diff("motorRight_pow",0,gamepadA.right_stick_y*99)):
        print react.CURRSTATE
        motorRight.run(react.get_val("motorRight_pow"))
    
    

motorLeft.idle()
motorRight.idle()