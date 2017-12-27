# import robotMain as robot
try:
    # Connects to our "brick" computer on robot
    brick1 = robot.get_brick1()

    # Creates a programmable robot from the "brick"
    robot1 = robot.RobotMain(brick1)

    # Give Some Commands
    robot1.moveForward(time=10)      # Move Forward  for 10 seconds
    robot1.moveBackward(time=10)     # Move Backward for 10 seconds

    # Define a FUNCTION - It's Like Defining a Word
    def driveInASquare():
        robot1.moveForward(time=4)   # Move Forward  for 10 seconds
        robot1.moveRight(time=4)     # Move Right    for 10 seconds
        robot1.moveBackward(time=4)  # Move Backward for 10 seconds
        robot1.moveLeft(time=4)      # Move Left     for 10 seconds

    # USE the function - It's Like Actually Saying the Word Out Loud
    driveInASquare()
except:
    pass
# print("I am a sentence.")
# print("I am also a group of words.")

def printASentence():
    print("I am printASentence.")

printASentence()
input("")