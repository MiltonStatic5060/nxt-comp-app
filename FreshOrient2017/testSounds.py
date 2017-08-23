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

def soundsamples():
    songs_list = "carelesswhisper.csv einsteins.csv numberone.csv runningnineties.csv xfiles.csv gamecube.csv".split(" ")
    x = 1 if gamepad1.a or gamepad1.b else 0
    x += 2 if gamepad1.x else 0
    x += 3 if gamepad1.y else 0
    if gamepad1.left_bumper:
        soundplayer.playSound(SoundBrick.csvToSong(songs_list[x]),240)

def multiGamepadTemplate(gArr):
    for gamepad in gArr:
        pass


servoArm0 = hardwareMap.Servo(b,PORT_1,1) #Shoulder
servoArm1 = hardwareMap.Servo(b,PORT_1,2) #Elbow


def servoMinionArm(gamepad):
    pass

soundplayer = SoundBrick.Player(b)
servoController = ServoCon(b,PORT_1)
servoController.set_pwm(0)
#servoController.set_pos(1,200)

deltaY = 0.1
deltaX = 0.1
posY = 0
posX = 0

# servoController.set_pos(3,255)
# print servoController.DATA
# x = input()
# servoController.set_pos(5,255)
# print servoController.DATA
# x = input()
# servoController.set_pos(3,125)
# print servoController.DATA
# x = input()
# servoController.set_pos(5,125)
# print servoController.DATA

while 1:
    x = 1 if gamepad1.a or gamepad1.b else 1
    x += 2 if gamepad1.x else 0
    x += 4 if gamepad1.y else 0
    # posY += gamepad1.right_stick_y * deltaY
    # posX += gamepad1.right_stick_x * deltaX
    #
    # posY = Range.clip(posY,0,255)
    # posX = Range.clip(posX,0,255)
    # servoArm0.setPosition(posX)
    # servoArm1.setPosition(posY)
    #print servoController.DATA
    servoController.set_pos(1,0)
    servoController.set_pos(2,Range.clip((gamepad1.left_stick_y-1)*-255.0/2,0,255))
    servoController.set_pos(3,Range.clip((gamepad1.left_stick_x-1)*-255.0/2,0,255))
    #servoController.set_pos(1,Range.clip((gamepad1.right_stick_y-1)*-255.0/2,0,255))
    #servoController.set_pos(2,Range.clip((gamepad1.right_stick_y-1)*-255.0/2,0,255))
    #servoController.set_pos(1,Range.clip((gamepad1.right_stick_x+1)*255.0/2,0,255))
    sleep(0.1)
    soundsamples()
    #servoMinionArm(gamepad1)
