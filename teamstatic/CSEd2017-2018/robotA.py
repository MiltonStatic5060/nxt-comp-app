

import robotMain
import nxt.bluesock # Make sure you remember this!

# --Initialize--
brick1 = nxt.bluesock.BlueSock('00:16:53:16:12:02').connect() #5060-S
brick2 = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #5060

robot1 = robotMain.RobotMain(brick1)
robot1.testCommand()

robot2 = robotMain.RobotMain(brick2)
robot2.testCommand()

