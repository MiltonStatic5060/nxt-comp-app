#import packages for Gamepad Control and Motor Controls
from nxttools import sound as SoundBrick
from nxttools import rangetools as Range
from nxttools import hardware as hardwareMap
from nxttools import reactcore
from nxttools.gamepad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *

# --Initialize--
b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
# b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
gamepadA = gamepad1
gamepadB = gamepad2

motorLeft = nxt.Motor(b, nxt.PORT_A)
motorCenter = nxt.Motor(b, nxt.PORT_B)
motorRight = nxt.Motor(b, nxt.PORT_C)

def r_drive():
    power = Range.clip(gamepadA.left_stick_y,-1,1) * 100  # +gamepadA.right_stick_y 
    turn = Range.clip(gamepadA.left_stick_x,-1,1) * 80 # +gamepadA.right_stick_x
    
    powLeft = power - turn
    powRight = power + turn

    if(reactcore.reactctl.is_diff("powRight",0,Range.clip(powRight,-127,126))):
        motorCenter.run(-reactcore.reactctl.get_val("powRight"))
    if(reactcore.reactctl.is_diff("powLeft",0,Range.clip(powLeft,-127,126))):
        motorRight.run(-reactcore.reactctl.get_val("powLeft"))

while 1:
    r_drive()
    
    if(reactcore.reactctl.is_diff("powArm",0,Range.clip(gamepadA.right_stick_y*100,-127,126))):
        motorLeft.run(reactcore.reactctl.get_val("powArm"))


    # if(gamepadA.dpad_down):
    #     motorLeft.run(127/1.5)
    # elif(gamepadA.dpad_up):
    #     motorLeft.run(-127/1.5)
    # else:
    #     motorLeft.run(0)