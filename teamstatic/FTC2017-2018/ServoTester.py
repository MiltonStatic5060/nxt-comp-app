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
# b1 = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060

gamepadA = gamepad1
gamepadB = gamepad2


nxt_port = nxt.PORT_1
dev_port = 3
brick_num = 1
START_VAL = 255*.54

servo = hardwareMap.Servo(b,nxt.PORT_1,3)
servo.set_pwm(0)
try:
    while 1:
        servo.set_pos(Range.clip((gamepadA.left_trigger*.4+.6)*255,0,255))
        print gamepadA.left_trigger
except:
    pass
