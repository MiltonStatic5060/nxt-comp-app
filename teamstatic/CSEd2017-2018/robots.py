# robot.py
"""This code controls the big metal robot 1st Generation"""

#import packages for Gamepad Control and Motor Controls
from nxttools import sound as SoundBrick
from nxttools import rangetools as Range
from nxttools import hardware as hardwareMap
from nxttools.reactcore import reactctl
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

b = get_brick1()
def connect():
    """Just connects straight to the brick. Returns nothing and stores brick in local variable."""
    global b
    b = get_brick2() # do connect bluetooth command here
    print("Connect Front Motors to Port 1, Back Motors to Port 2,")
    print("Other Motors to Port 3, and Servos to Port 4.")
devices = {}
def start():
    # driving
    devices["motorFR"] = hardwareMap.DcMotor(b,nxt.PORT_1,1)
    devices["motorFL"] = hardwareMap.DcMotor(b,nxt.PORT_1,2)
    devices["motorBR"] = hardwareMap.DcMotor(b,nxt.PORT_2,1)
    devices["motorBL"] = hardwareMap.DcMotor(b,nxt.PORT_2,2)
    # grabbing
    devices["blockLift"] = hardwareMap.DcMotor(b,nxt.PORT_3,2)
    devices["blockGrabR"] = hardwareMap.Servo(b,nxt.PORT_4,1)
    devices["blockGrabL"] = hardwareMap.Servo(b,nxt.PORT_4,2)
    devices["blockLift"].set_mode(4) # reset encoder
    devices["blockLift"].set_enc_target(0) # set target to 0
    devices["blockLift"].setPower(.4)
    devices["blockGrabR"].set_pwm(0)

    # devices["relicLift"] = hardwareMap.DcMotor(b,nxt.PORT_3,1)
    # devices["relicGrab"] = hardwareMap.Servo(b,nxt.PORT_4,3)
def control():
    """Command loop that activates the game controller if controls"""
    mainDrive()
    mainBlock()
# Loop Functions

# Main Commands
def mainDrive(left_y=0,left_x=0,right_y=0,right_x=0):
    powFR = Range.clip(left_y + right_y + left_x + right_x,-1,1)
    powFL = Range.clip(left_y + right_y - left_x - right_x,-1,1)
    powBR = Range.clip(left_y + right_y - left_x + right_x,-1,1)
    powBL = Range.clip(left_y + right_y + left_x - right_x,-1,1)

    if(reactctl.is_diff("powFR",0,-powFR)):
        devices["motorFR"].setPower(reactctl.get_val("powFR"))
    if(reactctl.is_diff("powFL",0,powFL)):
        devices["motorFL"].setPower(reactctl.get_val("powFL"))
    if(reactctl.is_diff("powBR",0,-powBR)):
        devices["motorBR"].setPower(reactctl.get_val("powBR"))
    if(reactctl.is_diff("powBL",0,powBL)):
        devices["motorBL"].setPower(reactctl.get_val("powBL"))   
def mainLift(left_trigger):
    """left_trigger is a float value from 0 to 1"""
    if(reactctl.is_diff("blockLift",0,left_trigger*-2880)):
        devices["blockLift"].set_enc_target(reactctl.get_val("blockLift"))
def mainBlock(right_trigger):
    """right_trigger is a float value from 0 to 1"""    
    if(reactctl.is_diff("blockGrabL",0,Range.clip(right_trigger*(255-130)+0,0,255-130))):
            devices["blockGrabL"].setPosition(reactctl.get_val("blockGrabL"))
    if(reactctl.is_diff("blockGrabR",255,Range.clip((1.0-right_trigger)*(255-130)+130,130,255))):
        devices["blockGrabR"].setPosition(reactctl.get_val("blockGrabR"))

# Preset Commands
def moveForward(secs=50,power=-0.4):
    """time is in milliseconds.  it is the amount of time it will move for"""
    start_time = time.time()
    # your code
    elapsed_time = time.time() - start_time
    while(elapsed_time<=secs/100.0):
        elapsed_time = time.time() - start_time
        mainDrive(power) # set power to move
    mainDrive(0.01)
    time.sleep(0.25)
    mainDrive(0)
def moveBackward(secs=50,power=0.4):
    """time is in milliseconds.  it is the amount of time it will move for"""
    start_time = time.time()
    # your code
    elapsed_time = time.time() - start_time
    while(elapsed_time<=secs/100.0):
        elapsed_time = time.time() - start_time
        mainDrive(power) # set power to move
    mainDrive(0.01)
    time.sleep(0.25)
    mainDrive(0)
def moveRight(secs=100,power=0.4):
    """time is in milliseconds.  it is the amount of time it will move for"""
    start_time = time.time()
    # your code
    elapsed_time = time.time() - start_time
    while(elapsed_time<=secs/100.0):
        elapsed_time = time.time() - start_time
        mainDrive(left_x=power) # set power to move
    mainDrive(0.01)
    time.sleep(0.25)
    mainDrive(0)
def moveLeft(secs=100,power=-0.4):
    """time is in milliseconds.  it is the amount of time it will move for"""
    start_time = time.time()
    # your code
    elapsed_time = time.time() - start_time
    while(elapsed_time<=secs/100.0):
        elapsed_time = time.time() - start_time
        mainDrive(left_x=power) # set power to move
    mainDrive(0.01)
    time.sleep(0.25)
    mainDrive(0)
def rotateLeft(secs=60,power=-0.4):
    """time is in milliseconds.  it is the amount of time it will move for"""
    start_time = time.time()
    # your code
    elapsed_time = time.time() - start_time
    while(elapsed_time<=secs/100.0):
        elapsed_time = time.time() - start_time
        mainDrive(right_x=power) # set power to move
    mainDrive(0.01)
    time.sleep(0.25)
    mainDrive(0)
def rotateRight(secs=60,power=0.4):
    """time is in milliseconds.  it is the amount of time it will move for"""
    start_time = time.time()
    # your code
    elapsed_time = time.time() - start_time
    while(elapsed_time<=secs/100.0):
        elapsed_time = time.time() - start_time
        mainDrive(right_x=power) # set power to move
    mainDrive(0.01)
    time.sleep(0.25)
    mainDrive(0)



def liftUp():
    """Makes block lift move all the way up"""
    mainLift(0.8) # set target to top
def grab():
    """Makes block grabbers activate""" 
    pass
def ungrab():
    """Makes block grabbers release"""
    pass

def grab_release(secs=2000):
    """Makes block grabbers grab and release after time (milliseconds)"""
    grab()
    # wait for variable time
    ungrab()

def extend_arm(secs=1000,power=30):
    """Extends the pusher arm outwards for variable time (milliseconds) with power (0 to 100)"""
    pass

def retract_arm(secs=1000,power=30):
    """Retracts the pusher arm outwards for variable time (milliseconds) with power (0 to 100)"""
    pass

def raise_flag():
    pass
def drop_flag():
    pass