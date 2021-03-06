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
    servoArm0.setPosition(Range.clip(gamepad.right_stick_y*-200,0,255))
    servoArm1.setPosition(Range.clip(gamepad.right_stick_x*-255/2,0,255))

soundplayer = SoundBrick.Player(b)
servoController = ServoCon(b,PORT_1)
servoController.set_pwm(0)
#servoController.set_pos(1,200)



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

deltaY = 15
deltaX = 15
posY = 255.0/2
posX = 0
while 1:
    posY += -gamepad1.right_stick_y * deltaY
    #posY += -gamepad1.right_stick_y * deltaY
    posX += -gamepad1.right_stick_x * deltaX
    posY = Range.clip(posY,0,220)
    posX = Range.clip(posX,0,255)
    print posY
    print posX
    servoArm0.setPosition(posY)
    servoArm1.setPosition(posX)
    servoController.set_pos(3,(gamepad1.right_trigger*125+130))


    #print servoController.DATA

    # servoController.set_pos(1,Range.clip((gamepad1.left_stick_y-1)*-255.0/2,0,255))
    # servoController.set_pos(2,Range.clip((gamepad1.left_stick_x-1)*-255.0/2,0,255))
    #servoController.set_pos(1,Range.clip((gamepad1.right_stick_y-1)*-255.0/2,0,255))
    #servoController.set_pos(2,Range.clip((gamepad1.right_stick_y-1)*-255.0/2,0,255))
    #servoController.set_pos(1,Range.clip((gamepad1.right_stick_x+1)*255.0/2,0,255))
    #sleep(0.001)
    soundsamples()
    #servoMinionArm(gamepad1)
