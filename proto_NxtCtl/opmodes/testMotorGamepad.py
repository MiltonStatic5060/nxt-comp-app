import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.find_one_brick()

mx = nxt.Motor(b, nxt.PORT_A)

def turnmotor(m, power, degrees):
	m.turn(power, degrees)
#how long from start until the last instruction is ended
length = 5

def runinstruction():
	#THIS IS THE IMPORTANT PART!
	thread.start_new_thread(
		turnmotor,
		(mx, 127, 90))
seconds = 0
while 1:
	turnmotor(mx,127,90)
	print seconds
	seconds = seconds + 1
	time.sleep(.1)
