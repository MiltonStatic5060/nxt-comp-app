import nxt, thread, time
from nxt.sensor.hitechnic import *

class DcMotor(MotorCon):
    def __init__(self, brick, port, motorport):
        super(DcMotor,self).__init__(brick, port)
        self.motorport = motorport
    def set_power(self,power):
        """power is -100 to 100"""
        super(DcMotor,self).set_power(motorport,power)
    def setPower(self,power):
        """power is -100 to 100"""
        super(DcMotor,self).set_power(motorport,power)
    def get_power(self,power):
        """power is -100 to 100"""
        super(DcMotor,self).get_power(motorport,power)
    def getPower(self,power):
        super(DcMotor,self).get_power(motorport,power)

class Servo(ServoCon):
    def __init__(self, brick, port, servoport):
        super(Servo,self).__init__(brick,port)
        self.servoport = servoport
    def set_pos(self, pos):
        """pos is (0 to 255)"""
        super(Servo,self).set_pos(self.servoport, pos)
    def setPosition(self, pos):
        """pos is (0 to 255)"""
        super(Servo,self).set_pos(self.servoport, pos)
