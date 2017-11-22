
from nxt.sensor import *
from nxt.sensor.hitechnic import *
import nxt, time
import nxt.bluesock # Make sure you remember this!
from NxtCtl.GamePad import *
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.find_one_brick()

m1 = MotorCon(b,PORT_4,0)
#m2 = MotorCon(b,PORT_4,1)
i=0
print("Brick Connected")
while 1:
    i+=1

    m1.set_power(1,gamepad1.left_stick_y*100)
    if(gamepad1.dpad_up):
        m1.I2C_DEV = 0x02
        print(m1.I2C_DEV)
    if(gamepad1.dpad_right):
        m1.I2C_DEV = 0x45
        print(m1.I2C_DEV)
    if(gamepad1.dpad_down):
        m1.I2C_DEV = 0x46
        print(m1.I2C_DEV)
    if(gamepad1.dpad_left):
        m1.I2C_DEV = 0x52
        print(m1.I2C_DEV)
    if(i%5==0):
        #m1.get_mode(1)
        if(gamepad1.right_stick_y == -1):
            m1.I2C_DEV += 1
            print(m1.I2C_DEV)
        if(gamepad1.right_stick_y == 1):
            m1.I2C_DEV -= 1
            print(m1.I2C_DEV)
    if(gamepad1.back):
        pid = m1.get_pid(1)
        print(pid.p,pid.i,pid.d)

#print('Ultrasonic:', Ultrasonic(b, PORT_4).get_sample())
