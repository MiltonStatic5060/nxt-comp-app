import robotMain as robot
try:
    brick1 = robot.get_brick1()
    robot1 = robot.RobotMain(brick1)
    robot1.testCommand()
except:
    print "Program Failed"