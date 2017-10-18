#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *

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

class ReactCtl(object):
    # "id":{"func":func,"values":[value1,value2]}
    CURRSTATE = {}
    PREVSTATE = {}
    def __init__(self):
        pass
    def update(self):
        # changes a value in CURRSTATE
        pass
    def run(self):
        # run functions if CURRSTATE is different PREVSTATE
        pass
CURRSTATE = {"motorLeft_pow":[0],"motorRight_pow":[0]}
PREVSTATE = CURRSTATE.copy()

def is_diff(ident):
    # returns boolean of whether the values of CURRSTATE and PREVSTATE
    # have changed at all at the identity given
    global CURRSTATE
    global PREVSTATE
    result = CURRSTATE[ident]==PREVSTATE[ident]
    PREVSTATE[ident] = CURRSTATE[ident]
    return not result
def get_val(ident):
    global CURRSTATE
    return CURRSTATE[ident]
def set_val(ident,arr):
    global CURRSTATE
    CURRSTATE[ident] = arr

while 1:
    set_val("motorLeft_pow",[gamepadA.left_stick_y*99, 0])
    set_val("motorRight_pow",[gamepadA.right_stick_y*99, 0])
    if(gamepadA.left_bumper):
        set_val("motorLeft_pow",[2*(gamepadA.left_trigger-0.5)*99, 0])
    if(gamepadA.right_bumper):
        set_val("motorRight_pow",[2*(gamepadA.right_trigger-0.5)*99, 0])
    
    if(is_diff("motorLeft_pow")):
        print CURRSTATE
        motorLeft.run(get_val("motorLeft_pow")[0])
    if(is_diff("motorRight_pow")):
        print CURRSTATE
        motorRight.run(get_val("motorRight_pow")[0])
    
    

motorLeft.idle()
motorRight.idle()