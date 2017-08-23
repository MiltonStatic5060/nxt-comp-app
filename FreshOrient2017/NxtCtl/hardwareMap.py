import nxt, thread, time
from nxt.sensor.hitechnic import *

class DcMotor(MotorCon):
    def __init__(self, brick, port, motorport):
        super(DcMotor,self).__init__(brick, port)
        self.motorport = motorport
    def set_power(self,power):
        """power is originally -100 to 100
        use decimal value -1 to 1"""
        super(DcMotor,self).set_power(motorport,power*100.0)
    def setPower(self,power):
        """power is originally -100 to 100
        use decimal value -1 to 1"""
        self.set_power(power)
    def get_power(self):
        """power is originally -100 to 100
        return decimal value -1 to 1"""
        return super(DcMotor,self).get_power(motorport)/100.0
    def getPower(self,power):
        """power is originally -100 to 100
        return decimal value -1 to 1"""
        return self.get_power()

class Servo(ServoCon):
    def __init__(self, brick, port, servoport):
        super(Servo,self).__init__(brick,port)
        self.servoport = servoport
    def set_pos(self, pos):
        """pos(position) is originally (0 to 255)
        """
        super(Servo,self).set_pos(self.servoport, pos)
    def setPosition(self, pos):
        """pos(position) is originally (0 to 255)
        """
        self.set_pos(pos)
