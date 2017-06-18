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
#--Setup-- PORT_1 = ServoCon 000111; PORT_2 = MotorCon 0010; NXT Motors 111;

#--Catapult--
#catShoot tetrix motor PORT_1,2
#catBase  180servo PORT_2,2
catShoot = hardwareMap.DcMotor(b, nxt.PORT_2, 1)
catBase  = hardwareMap.Servo(b,nxt.PORT_1,3)
angCat = 90 #degrees 0 to 90/180; 0 is all the way left, 90/180 is all the way right

#--Robot Arm Controls--
#armElbow angElbow  nxt motor+string or strong servos PORT_A
#armShoul angShoul  nxt motor+string or strong servos PORT_B
#armBase  angBase   strong servo or none PORT_1,1
#armWrist angWrist  servo or nxt motor PORT_C
#servoClaw  angClaw servo PORT_1,2

angElbow = 0 #degrees 0 to 180; 0 is fully extended
angShoul = 0 #degrees 0 to 90; 0 is fully extended
angBase = 90 #degrees 0 to 90/180; 0 is all the way left, 90/180 is all the way right
angWrist = 90 #degrees 0 to 180; 0 is all the way up, 180 is all the way down; 90 starts in the middle
angClaw = 0 #degrees 0 to 90; 0 is closed position

armElbow = nxt.Motor(b, nxt.PORT_A)
armShoul = nxt.Motor(b, nxt.PORT_B)
armWrist = nxt.Motor(b, nxt.PORT_C)

armBase = hardwareMap.Servo(b, nxt.PORT_1, 1)
armClaw = hardwareMap.Servo(b, nxt.PORT_1,2)


#--Song for Attention--
#Any of the Preset Songs
soundPlayer = SoundBrick.Player(b)

seconds = 0
#--Initialization Success--
soundPlayer.success()
while 1:
    #Time control and management
    seconds = seconds + 1
    time.sleep(.001)

    #Catapult
    #left_trigger - shoot - catShoot.setPower()
    #left_bumper right_bumper - aim Catapult


    #Robot Arm
    #left_stick_y - arm extend outward/inward
    #left_stick_x - armBase rotate
    #right_stick_y - arm upwards/downwards
    #right_trigger - claw control open/close
    #a or b - toggle state open/close


    #Sound Controller
    arr = [gamepad1.dpad_up,gamepad1.dpad_right,gamepad1.dpad_down,gamepad1.dpad_left]
    for i in range(len(arr)):
		if arr[i]:
			soundPlayer.playSoundSample(i,120)
