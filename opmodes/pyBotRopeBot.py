from NxtCtl import SoundBrick
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *
from NxtCtl.GamePad import *
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #replace the string with the one you got earlier

while 1:
    MotorCon(b,PORT_1).setPower(1,gamepad2.left_stick_y)
    ServoCon(b,PORT_2).setPower(1,gamepad2.left_trigger*250)
    
