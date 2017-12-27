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
def get_brick1():
    return nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
def get_brick2():
    return nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060
gamepadA = gamepad1
gamepadB = gamepad2

class RobotMain(object):
    
    gamepadA = gamepadA
    gamepadB = gamepadB
    react = reactcore.reactctl
    
    def __init__(self,brick):
        self.b = brick
        self.soundPlayer = SoundBrick.Player(brick)

    def testCommand(self):
        self.soundPlayer.playSoundSample(1,120)

    def initWheels(self,port1=nxt.PORT_1,port2=nxt.PORT_2):
        # Wheels - 2 Different Controllers
        self.motorFR = hardwareMap.DcMotor(self.b,port1,1)
        self.motorFL = hardwareMap.DcMotor(self.b,port1,2)
        self.motorBR = hardwareMap.DcMotor(self.b,port2,1)
        self.motorBL = hardwareMap.DcMotor(self.b,port2,2)
    
    def initLift(self,port=nxt.PORT_3):
        # BlockLift  - 1 Controller
        self.blockLift = hardwareMap.DcMotor(self.b,port,1)
        self.blockLift.set_mode(4) # reset encoder
        self.blockLift.set_enc_target(0) # set target to 0
        self.blockLift.set_mode(3) # run to position
        self.blockLift.setPower(0.5) # TODO: really should save this for the loop section
    
    def initArms(self,port=nxt.PORT_3):
        # PushArm RelicArm - 1 Controller
        self.pusherArm = hardwareMap.DcMotor(self.b, port, 1)
        self.relicLift = hardwareMap.DcMotor(self.b, port, 2)
        self.relicLift.set_mode(4) # reset encoder
        self.relicLift.set_enc_target(0) # set target to 0
        self.relicLift.set_mode(3) # run to position
        self.relicLift.setPower(0.5) # TODO: really should save this for the loop section

    def initClaws(self,port=nxt.PORT_4):
        # RelicClaw BlockGrabL BlockGrabR - 1 Controller
        self.blockGrabL = hardwareMap.Servo( self.b, port, 1)
        self.blockGrabR = hardwareMap.Servo( self.b, port, 2)
        self.relicClaw = hardwareMap.Servo( self.b, port, 3)

    def runWheels(self):
        """In an infinite loop, this function will assign the 
        left inputs to tank-style control and the
        right inputs to cardinal-style control (with holonomic wheels)"""
        # gamepadA -> left is left stick and right is right stick
        # gamepadB -> left is left stick and right is right stick
        left_y  = self.gamepadA.left_stick_y + self.gamepadB.left_stick_y
        right_y = self.gamepadA.right_stick_y + self.gamepadB.right_stick_y
        left_x  = self.gamepadA.left_stick_x + self.gamepadB.left_stick_x
        right_x = self.gamepadA.right_stick_x + self.gamepadB.right_stick_x

        powFR =  Range.clip( left_y + right_y + left_x + right_x , -1 , 1 )
        powFL =  Range.clip( left_y + right_y - left_x - right_x , -1 , 1 )
        powBR =  Range.clip( left_y + right_y - left_x + right_x , -1 , 1 )
        powBL =  Range.clip( left_y + right_y + left_x - right_x , -1 , 1 )

        if(self.react.is_diff("motorFR",0,-powFR)):
            self.motorFR.setPower(self.react.get_val("motorFR"))

        if(self.react.is_diff("motorFL",0,powFL)):
            self.motorFL.setPower(self.react.get_val("motorFL"))
            
        if(self.react.is_diff("motorBR",0,-powBR)):
            self.motorBR.setPower(self.react.get_val("motorBR"))

        if(self.react.is_diff("motorBL",0,powBL)):
            self.motorBL.setPower(self.react.get_val("motorBL"))

    def runLift(self):
        """In an infinite loop, this function will take the 
        left trigger and assign it to the block lifter"""
        if(self.react.is_diff("blockLift",0,self.gamepadA.left_trigger*-2880)):
            self.blockLift.set_enc_target(self.react.get_val("blockLift"))

    def runArms(self):
        """In an infinite loop, this function will take the
        left trigger and assign it to the relic arm and take the
        back and guid buttons and assign those to the pusher arm"""
        if(self.gamepadA.back):
            self.pusherArm.setPower(0.7) # Full power pull back
        elif(self.gamepadA.guide):
            self.pusherArm.setPower(-0.7) # Full power push forward
        if(self.react.is_diff("relicLift",0,self.gamepadA.left_trigger*1440.0/4.0)):
            self.relicLift.set_enc_target(self.react.get_val("relicLift"))
        
    def runClaws(self):
        """In an infinite loop, this function will take the 
        right trigger and assign it to the lift claws and take the 
        ____________  and assign it to the relic claw"""
        right_trigger = self.gamepadA.right_trigger
        right_bumper = self.gamepadA.right_bumper

        if(self.react.is_diff("relicClaw",0,Range.clip((0.8 if right_bumper else 0)*(255-130)+0,0,255-130))):
            self.relicClaw.setPosition(self.react.get_val("relicClaw"))
        
        if(self.react.is_diff("blockGrabL",0,Range.clip(right_trigger*(255-130)+0,0,255-130))):
            self.blockGrabL.setPosition(self.react.get_val("blockGrabL"))
        if(self.react.is_diff("blockGrabR",255,Range.clip((1.0-right_trigger)*(255-130)+130,130,255))):
            self.blockGrabR.setPosition(self.react.get_val("blockGrabR"))