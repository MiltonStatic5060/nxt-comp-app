from NxtCtl.r_Gamepad import *
from nxt.sensor import *
from nxt.sensor.hitechnic import *
import nxt, time
import nxt.bluesock # Make sure you remember this!
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.find_one_brick()

#motCon1 = MotorCon(b,PORT_4,0)


while 1:
    
    MotorCon(b,PORT_2).set_power(1,gamepad1.left_stick_y*100)
    print "tick"
