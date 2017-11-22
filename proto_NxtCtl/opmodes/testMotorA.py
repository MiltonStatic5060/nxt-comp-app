import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from NxtCtl.r_Gamepad import *
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.find_one_brick()

mx = nxt.Motor(b, nxt.PORT_A)
my = nxt.Motor(b, nxt.PORT_B)

def turnmotor(m, power, degrees):
	m.turn(power, 5)
#how long from start until the last instruction is ended
length = 1

def runinstruction():
	#THIS IS THE IMPORTANT PART!
	thread.start_new_thread(
		turnmotor,
		(mx, 127, 10))
seconds = 0
while 1:
	print "Tick %d" % seconds
	power = gamepad1.left_stick_y
	direction = gamepad1.left_stick_x
	left = power - direction
	right = power + direction
	mx.run(Range.clip(left*100,-100,100))
	my.run(Range.clip(right*100,-100,100))
	#runinstruction()
	seconds = seconds + 1
	time.sleep(.001)
