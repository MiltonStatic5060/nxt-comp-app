import nxt, thread, time
from nxt.sensor.hitechnic import *

class DcMotor(MotorCon):
    def __init__(self, brick, port, motorport):
        super(DcMotor,self).__init__(brick, port)
        self.motorport = motorport
    
    def set_power(self,power):
        """power is originally -100 to 100
        use decimal value -1 to 1"""
        super(DcMotor,self).set_power(self.motorport,power*100.0)
    
    def setPower(self,power):
        """power is originally -100 to 100
        use decimal value -1 to 1"""
        self.set_power(power)
    
    def get_power(self):
        """power is originally -100 to 100
        return decimal value -1 to 1"""
        return super(DcMotor,self).get_power(self.motorport)/100.0

    def getPower(self,power):
        """power is originally -100 to 100
        return decimal value -1 to 1"""
        return self.get_power()

    def set_enc_target(self, val):
        """1440 units of an encoder is equivalent to 360 degrees angle"""
        super(DcMotor,self).set_enc_target(self.motorport,val)
    
    def get_enc_target(self):
        """Get the motor's current target degrees
        1440 units of an encoder is equivalent to 360 degrees angle"""
        return super(DcMotor,self).get_enc_target(self.motorport)
    
    def get_enc_current(self):
        """Get the motor's current degrees
        1440 units of an encoder is equivalent to 360 degrees angle"""
        return super(DcMotor,self).get_enc_current(self.motorport)
    
    def get_battery_voltage(self):
        """Get the battery's current voltage"""
        return super(DcMotor,self).get_battery_voltage()
    
    def set_mode(self,mode):
        """modes:
        1 - Run with power control only
        2 - Run with constant speed
        3 - Run to position
        4 - Reset current encoder"""
        modes = [0x00,0x01,0x02,0x03]
        super(DcMotor,self).set_mode(self.motorport,modes[mode-1])

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