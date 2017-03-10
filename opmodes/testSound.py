import SoundBrick
import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
#from NxtCtl.r_Gamepad import *
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
print("Brick connected")
SoundBrick.playSound(b,SoundBrick.csvToSong("victory"),120)
