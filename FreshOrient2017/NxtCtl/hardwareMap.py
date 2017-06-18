import nxt, thread, time
from nxt.sensor.hitechnic import *

class DcMotor(MotorCon):
    def __init__(self, brick, port, motorport):
        super(DcMotorController,self).__init__(brick, port)
        self.motorport = motorport
    def set_power(self,power):
        super(DcMotorController,self).set_power(motorport,power)
    def setPower(self,power):
        super(DcMotorController,self).set_power(motorport,power)
    def get_power(self,power):
        super(DcMotorController,self).get_power(motorport,power)
    def getPower(self,power):
        super(DcMotorController,self).get_power(motorport,power)

class Servo(ServoCon):
    def __init__(self, brick, port, servoport):
        super(Servo,self).__init__(brick,port)
        self.servoport = servoport
    def set_pos(self, pos):
        super(Servo,self).set_pos(self.servoport, pos)
