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
gamepadA = gamepad1
gamepadB = gamepad2

#Front motors?
motorRight = hardwareMap.DcMotor( b, nxt.PORT_1, 1)
motorLeft = hardwareMap.DcMotor( b, nxt.PORT_1, 2)
#Back motors?
motorRight1 = hardwareMap.DcMotor( b, nxt.PORT_2, 1)
motorLeft1 = hardwareMap.DcMotor( b, nxt.PORT_2, 2)

minionLights = hardwareMap.DcMotor( b, nxt.PORT_3, 1)

servoX = hardwareMap.Servo( b, nxt.PORT_4, 2)
servoY = hardwareMap.Servo( b, nxt.PORT_4, 1)
servoClaw = hardwareMap.Servo( b, nxt.PORT_4, 3)

deltaY = 30
deltaX = 30
posY = 0
posX = 0

soundplayer = SoundBrick.Player(b)

def r_motorPower(): # Multicontroller admin-dpad&left_stick user-left_stick

    #admin dpad has cardinal control
    left_stick_x = 1 if gamepadA.dpad_right else 0
    left_stick_y = 1 if gamepadA.dpad_down else 0
    left_stick_x -= 1 if gamepadA.dpad_left else 0
    left_stick_y -= 1 if gamepadA.dpad_up else 0

    #user and admin have left stick normal control
    right_stick_x = gamepadB.left_stick_x + gamepadA.left_stick_x
    right_stick_y = gamepadB.left_stick_y + gamepadA.left_stick_y


    left_x = Range.clip(left_stick_x,-1,1)
    left_y = Range.clip(left_stick_y,-1,1)
    right_x  = Range.clip(right_stick_x,-1,1)
    right_y = Range.clip(right_stick_y,-1,1)

    #left stick controls cardinal direction.  right stick has forward/back and rotation
    #Front power
    powRight =  Range.clip( left_y + right_y + left_x + right_x , -1 , 1 )
    powLeft =   Range.clip( left_y + right_y - left_x - right_x , -1 , 1 )
    #Back power
    powRight1 = Range.clip( left_y + right_y - left_x + right_x , -1 , 1 )
    powLeft1 =  Range.clip( left_y + right_y + left_x - right_x , -1 , 1 )

    motorRight.setPower(-powRight)
    motorLeft.setPower(powLeft)
    motorRight1.setPower(-powRight1)
    motorLeft1.setPower(powLeft1)
def soundPlayer(): # Multicontroller Controllers abxy for both user and admin
    #Sound Controller

    sound1 = gamepadA.a or gamepadB.a
    sound2 = gamepadA.b or gamepadB.b
    sound3 = gamepadA.y or gamepadB.y
    sound4 = gamepadA.x or gamepadB.x

    arr = [sound1,sound2,sound3,sound4]
    for i in range(len(arr)):
		if arr[i]:
			soundplayer.playSoundSample(i,120)
def r_minionLights(): #Multicontroller right_trigger for both user and admin
    right_trigger = gamepadA.right_trigger + gamepadB.right_trigger
    minionLights.setPower(Range.clip(abs(right_trigger),0,1))
def r_servoArm(): #Multicontroller Stepper-User Control Override-Admin
    global deltaY
    global deltaX
    global posY
    global posX

    dpad_up = gamepadB.dpad_up
    dpad_down = gamepadB.dpad_down
    dpad_left = gamepadB.dpad_left
    dpad_right = gamepadB.dpad_right

    right_stick_y = gamepadA.right_stick_y
    right_stick_x = gamepadA.right_stick_x

    if(dpad_up): posY += deltaY
    if(dpad_down): posY -= deltaY
    if(dpad_left): posX += deltaX
    if(dpad_right): posX -= deltaX

    if(right_stick_y==-1): posY += deltaY
    if(right_stick_y==1): posY -= deltaY
    if(right_stick_x==-1): posX += deltaX
    if(right_stick_x==1): posX -= deltaX

    if(gamepadA.right_bumper):  # Admin reset to home with back button
        posY = abs(right_stick_y*250)
        posX = abs(right_stick_x*250)

    posY = Range.clip(posY,0,220)
    posX = Range.clip(posX,0,255)
    print posY
    print posX
    servoY.setPosition(posY)
    servoX.setPosition(posX)
    servoClaw.set_pos(gamepadA.left_trigger*125+130)

ServoCon(b,PORT_4).set_pwm(0)

SoundBrick.Player(b).success()
while 1:
    r_motorPower() # left and right stick to control driving
    r_minionLights() # right_trigger to control lights
    r_servoArm() # dpad to move arm up and down.  left_trigger opens claw
    soundPlayer() # a b x y to control sounds
    # left_bumper right_bumper do something? maybe with servos?
    # guide? back?
