from NxtCtl import SoundBrick
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
from NxtCtl.GamePad import *
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #replace the string with the one you got earlier
#b = nxt.find_one_brick()
motorLeft = nxt.Motor(b, nxt.PORT_A)
motorRight = nxt.Motor(b, nxt.PORT_B)
motorCenter = nxt.Motor(b, nxt.PORT_C)
seconds = 0
M1POS = motorCenter.get_tacho().tacho_count


def runToPosition(newPos):
	oldPos = M1POS
	diff = oldPos-newPos

	if (cercaDe(motorCenter.get_tacho().tacho_count,newPos,3)):
		motorCenter.brake()
		diff = 0
	motorCenter.run(Range.clip(diff*2,-90,90))
def cercaDe(first, second, difference):
	return abs(first-second)<=difference
motorCenter.reset_position(True)

soundPlayer = SoundBrick.Player(b)

while 1:
	#print "Tick %d" % seconds
	power = gamepad1.left_stick_y
	direction = gamepad1.left_stick_x
	right = power - direction
	left = power + direction
	motorLeft.run(Range.clip(left*100,-100,100))
	motorRight.run(Range.clip(right*100,-100,100))
	#motorCenter
	motorCenter.run(Range.clip(gamepad1.left_trigger*-200+100,-64,64))

	if(gamepad1.start and gamepad1.guide):
		motorCenter.run(0)
		break

	arr = [gamepad1.a, gamepad1.b,gamepad1.y,gamepad1.x,gamepad1.dpad_down,gamepad1.dpad_up]
	#if(gamepad1.y):
	#	soundPlayer.playSound(SoundBrick.csvToSong("victory"),120)
	#if(gamepad1.x):
	#	soundPlayer.playSoundSample(0,120)

	for i in range(len(arr)):
		if arr[i]:
			soundPlayer.playSoundSample(i,120)
			#noteArr = "lg a b c d e f g".split(" ")
			#soundPlayer.playNote(noteArr[i],200,gamepad1.right_trigger)
	if(gamepad1.back):
		soundPlayer.playSound(SoundBrick.csvToSong("mario"),120)
	padDisplay.reset()
	gamepad1.show_status()
	gamepad1.show_status()

	seconds = seconds + 1
	time.sleep(.001)
