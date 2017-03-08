
from nxt.sensor import *
from nxt.sensor.hitechnic import *
import nxt, time
import nxt.bluesock # Make sure you remember this!
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.find_one_brick()

MotorCon(b,PORT_4,0).set_power(1,10)
MotorCon(b,PORT_4,1).set_power(1,10)

while 1:
    time.sleep(.01)
    print('Touch:', Touch(b, PORT_1).get_sample())
    print('Sound:', Sound(b, PORT_2).get_sample())
    print('Light:', Light(b, PORT_3).get_sample())
#print('Ultrasonic:', Ultrasonic(b, PORT_4).get_sample())
