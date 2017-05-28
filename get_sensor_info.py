import nxt.locator
from nxt.sensor import *
b = nxt.locator.find_one_brick()
for p in [PORT_1,PORT_2,PORT_3,PORT_4]:
	s = nxt.BaseDigitalSensor(b,p)
	print s.get_sensor_info()
	print str(p)

