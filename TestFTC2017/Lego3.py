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

def rigthToTarget(target):
    current = motorRight.get_tacho().tacho_count
    distance = target-current
    if (distance == 0):
        distance = 1
    direction = distance/abs(distance)
    closeness = Range.clip(abs(distance), 0 , 500 )
    rightPower((50+closeness*50.0/500.0)*direction)
    if (abs(distance)<10):
        motorRight.brake()
    
def rightPower(power):
    if(react.is_diff("motorRight_pow",0,power)):
        print react.CURRSTATE
        motorRight.run(react.get_val("motorRight_pow"))
    
counter = 0
x=0
while 1:
    counter+=1
    if(react.is_diff("motorRight_enc",0,motorRight.get_tacho().tacho_count)):
        print react.get_val("motorRight_enc")
    if(gamepadA.a):
        x=1000
    if(gamepadA.b):
        x=0
    if(gamepadA.y):
        x=100
    if(gamepadA.x):
        x=20
    # if(gamepadA.left_bumper):
    #     set_val("motorLeft_pow",[2*(gamepadA.left_trigger-0.5)*99, 0])
    # if(gamepadA.right_bumper):
    #     set_val("motorRight_pow",[2*(gamepadA.right_trigger-0.5)*99, 0])
    
    # if(react.is_diff("motorLeft_pow",0,gamepadA.left_stick_y*99)):
    #     print react.CURRSTATE
    #     motorLeft.run(react.get_val("motorLeft_pow"))
    # if(react.is_diff("motorRight_pow",0,gamepadA.right_stick_y*99)):
    #     print react.CURRSTATE
    #     motorRight.run(react.get_val("motorRight_pow"))
    
    # count to 10 and then get run inside
    rigthToTarget(x)
    # if(counter%10==0):
    #     print motorLeft.get_tacho().tacho_count
    #     print motorRight.get_tacho().tacho_count
        

motorLeft.idle()
motorRight.idle()

