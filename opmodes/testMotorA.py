import nxt, thread, time

b = nxt.find_one_brick()

mx = nxt.Motor(b, nxt.PORT_A)

def turnmotor(m, power, degrees):
	m.turn(power, degrees)
#how long from start until the last instruction is ended
length = 5

def runinstruction():
	#THIS IS THE IMPORTANT PART!
	thread.start_new_thread(
		turnmotor,
		(mx, 50, 90))

while 1:
	print "Tick %d" % seconds
	runinstruction()
	seconds = seconds + 1
	if seconds >= length:
		break
	time.sleep(1)

