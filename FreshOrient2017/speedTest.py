#import packages for Gamepad Control and Motor Controls
from NxtCtl import SoundBrick, hardwareMap, Range
from NxtCtl.GamePad import *

#import nxt-python packages to connect to robot and bluetooth
import nxt, thread
import nxt.bluesock # Make sure you remember this!
from nxt.sensor.hitechnic import *
from time import sleep
#--Initialize--
b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
#b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
soundplayer = SoundBrick.Player(b)
def soundPlayer():
    #Sound Controller
    arr = [gamepadA.a,gamepadA.b,gamepadA.y,gamepadA.x]
    for i in range(len(arr)):
		if arr[i]:
			soundplayer.playSoundSample(i,120)

gamepadA = gamepad1
gamepadB = gamepad2

soundplayer.success()
while 1:
    soundPlayer()
