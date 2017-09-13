# Block Manipulation
back pressed=block manipulation mode

blockLift = motor/servo  
left_trigger (0=lowest point, 1=highest point)

blockGrab = servo (with 2 connections)  
right_trigger (0=closed, 1=open)

# Relic Manipulation
guide pressed=relic manipulation mode

relicArm = motor  
left_trigger (0=closest point , 1=farthest point)

relicGrab = servo  
right_trigger (0=closed, 1=open)  

# Autonomous Jewel/Vuforia Sensing
Vuforia to the top left of the jewels (always)  

# Autonomous Block Moving
Blue 1 = Shelving to the right of the jewels  maybe half foot

Red 1 = Shelving to the left of the jewels maybe half foot  

Blue 2 = rotate 90 degrees clockwise shelving a few feet in front and half foot to the right  

Red 2 = rotate 90 degrees counterclockwise shelving a few feet in front and half foot to the left  

Rotate first (if rotateNeeded)  
Horizontal 6 in (left-red or right-blue)
Move forward (if forwardNeeded) until lines detected.
Place block accordingly.
Park in triangle.