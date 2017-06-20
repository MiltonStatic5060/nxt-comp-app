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

motorA = nxt.Motor(b,nxt.PORT_A)

angA = 0 #0 to 720

motorA.reset_position(True)
#Operating loop
while 1:
    print motorA.get_tacho()
    diffState = 0
    diffState = 0-motorA.get_tacho().tacho_count
    print diffState*2
    print Range.clip(diffState/3,-127,127)
    if gamepad1.b:
        #go to absolute origin
        motorA.run(Range.clip(diffState/3,-127,127))
    else:
        motorA.run(0)
    if gamepad1.y:
        motorA.reset_position(True)
