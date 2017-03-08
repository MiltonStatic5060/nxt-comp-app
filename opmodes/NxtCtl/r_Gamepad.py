import inputs
import thread
import time
import progressbar

class Range(object):
    @staticmethod
    def clip(input,min,max):
        if(input<=min):
            return min
        elif(input>=max):
            return max
        else:
            return round(input,2)

class ul_Gamepad(object):
    def __init__(self, x=None):
        run = True
        if x is None:
            run = False
        if run:
            self.events = inputs.DeviceManager().gamepads[x]
        self.start = False #BTN_START
        self.back = False #BTN_SELECT
        self.guide = False #BTN_MODE
        #Colorful buttons on right side
        self.a = False #BTN_SOUTH
        self.b = False #BTN_EAST
        self.x = False #BTN_NORTH
        self.y = False #BTN_WEST
        #Dpad on the left
        self.dpad_up = False    #ABS_HAT0Y,-1
        self.dpad_down = False  #ABS_HAT0Y, 1
        self.dpad_left = False  #ABS_HAT0X,-1
        self.dpad_right = False #ABS_HAT0X, 1
        #Shoulder buttons
        self.left_bumper = False    #BTN_TL
        self.right_bumper = False   #BTN_TR
        self.left_trigger  = 0 #ABS_Z
        self.right_trigger = 0 #ABS_RZ

        #Joysticks
        self.left_stick_button = False   #BTN_THUMBL
        self.right_stick_button = False  #BTN_THUMBR
        self.left_stick_y = 0 #ABS_Y
        self.left_stick_x = 0 #ABS_X
        self.right_stick_y = 0 #ABS_RY
        self.right_stick_x = 0 #ABS_RX

    def update(self):
        while 1:
            for event in self.events.read():
                #Dpad on the left
                if(event.code=="ABS_HAT0Y"):
                    if(event.state==-1):
                        self.dpad_up = True
                    if(event.state==0):
                        self.dpad_down = False
                        self.dpad_up = False
                    if(event.state==1):
                        self.dpad_down = True
                if(event.code=="ABS_HAT0X"):
                    if(event.state==-1):
                        self.dpad_left = True
                    if(event.state==0):
                        self.dpad_right = False
                        self.dpad_left = False
                    if(event.state==1):
                        self.dpad_right = True
                #Colorful Buttons on the right
                if(event.code=="BTN_SOUTH"):
                    if(event.state==1):
                        self.a = True
                    if(event.state==0):
                        self.a = False
                if(event.code=="BTN_EAST"):
                    if(event.state==1):
                        self.b = True
                    if(event.state==0):
                        self.b = False
                if(event.code=="BTN_NORTH"):
                    if(event.state==1):
                        self.x = True
                    if(event.state==0):
                        self.x = False
                if(event.code=="BTN_WEST"):
                    if(event.state==1):
                        self.y = True
                    if(event.state==0):
                        self.y = False
                #Buttons in the center part
                if(event.code=="BTN_START"):
                    if(event.state==1):
                        self.start = True
                    if(event.state==0):
                        self.start = False
                if(event.code=="BTN_MODE"):
                    if(event.state==1):
                        self.guide = True
                    if(event.state==0):
                        self.guide = False
                if(event.code=="BTN_SELECT"):
                    if(event.state==1):
                        self.back = True
                    if(event.state==0):
                        self.back = False
                #Joysticks
                if(event.code=="ABS_Y"):
                    self.left_stick_y = Range.clip((event.state+129)/32600.0,-1,1)
                if(event.code=="ABS_X"):
                    self.left_stick_x = Range.clip((event.state-128)/32600.0,-1,1)
                if(event.code=="ABS_RY"):
                    self.right_stick_y = Range.clip((event.state+129)/32600.0,-1,1)
                if(event.code=="ABS_RX"):
                    self.right_stick_x = Range.clip((event.state-128)/32600.0,-1,1)
                if(event.code=="BTN_THUMBR"):
                    if(event.state==1):
                        self.right_stick_button = True
                    if(event.state==0):
                        self.right_stick_button = False
                if(event.code=="BTN_THUMBL"):
                    if(event.state==1):
                        self.left_stick_button = True
                    if(event.state==0):
                        self.left_stick_button = False
                #Shoulder Buttons
                if(event.code=="ABS_Z"):
                    self.left_trigger = Range.clip((event.state)/255.0,0,1)
                if(event.code=="ABS_RZ"):
                    self.right_trigger = Range.clip((event.state)/255.0,0,1)
                if(event.code=="BTN_TL"):
                    if(event.state==1):
                        self.left_bumper = True
                    if(event.state==0):
                        self.left_bumper = False
                if(event.code=="BTN_TR"):
                    if(event.state==1):
                        self.right_bumper = True
                    if(event.state==0):
                        self.right_bumper = False
class ol_Gamepad(object):
    def __init__(self,n):

        self.status0 = False
        self.status1 = False
        self.id = n
        self.gamepads = []
        self.pad = ul_Gamepad()
        self.old = ul_Gamepad()
        self.numG = len(inputs.DeviceManager().gamepads)
        #center buttons
        self.start = False #BTN_START
        self.back = False #BTN_SELECT
        self.guide = False #BTN_MODE
        #Colorful buttons on right side
        self.a = False #BTN_SOUTH
        self.b = False #BTN_EAST
        self.x = False #BTN_NORTH
        self.y = False #BTN_WEST
        #Dpad on the left
        self.dpad_up = False    #ABS_HAT0Y,-1
        self.dpad_down = False  #ABS_HAT0Y, 1
        self.dpad_left = False  #ABS_HAT0X,-1
        self.dpad_right = False #ABS_HAT0X, 1
        #Shoulder buttons
        self.left_bumper = False    #BTN_TL
        self.right_bumper = False   #BTN_TR
        self.left_trigger  = 0 #ABS_Z
        self.right_trigger = 0 #ABS_RZ

        #Joysticks
        self.left_stick_button = False   #BTN_THUMBL
        self.right_stick_button = False  #BTN_THUMBR
        self.left_stick_y = 0 #ABS_Y
        self.left_stick_x = 0 #ABS_X
        self.right_stick_y = 0 #ABS_RY
        self.right_stick_x = 0 #ABS_RX
    def button(self,x):
        if x==0:
            return "a"
        if x==1:
            return "b"
        if x==2:
            return "y"
        if x==3:
            return "x"
    def other_buttons(self,x):
        arr = "a b y x".split(" ")
        del arr[x]
        return arr
    def status(self):
        while 1:
            if(self.status0==self.status1):
                if(not self.status0):
                    #print("Gamepad "+str(self.id+1)+" Unassigned")
                if(self.status0):
                    #print("Gamepad "+str(self.id+1)+" Assigned")
                self.status0 = not self.status1
    def update(self):
        for item in range(self.numG):
            self.gamepads.append(ul_Gamepad(item))
            thread.start_new_thread(self.gamepads[item].update,())
        print("Gamepad "+str(self.id+1)+" Initialized")
        while (self.id<=self.numG):
            for item in range(self.numG):
                if(self.gamepads[item].start and self.gamepads[item].__dict__[self.button(self.id)]):
                    self.pad = self.gamepads[item]
                    self.status1 = True
                for f in range(3):
                    if(self.pad.start and self.pad.__dict__[self.other_buttons(self.id)[f]]):
                        self.pad = self.old
                        self.status1 = False
            self.start = self.pad.start
            self.back = self.pad.back
            self.guide = self.pad.guide
            self.a = self.pad.a
            self.b = self.pad.b
            self.x = self.pad.x
            self.y = self.pad.y
            self.dpad_up = self.pad.dpad_up
            self.dpad_down = self.pad.dpad_down
            self.dpad_left = self.pad.dpad_left
            self.dpad_right = self.pad.dpad_right
            self.left_bumper = self.pad.left_bumper
            self.right_bumper = self.pad.right_bumper
            self.left_trigger = self.pad.left_trigger
            self.right_trigger = self.pad.right_trigger
            self.left_stick_button = self.pad.left_stick_button
            self.right_stick_button = self.pad.right_stick_button
            self.left_stick_y = self.pad.left_stick_y
            self.left_stick_x = self.pad.left_stick_x
            self.right_stick_y = self.pad.right_stick_y
            self.right_stick_x = self.pad.right_stick_x


    def updater(self):
        thread.start_new_thread(self.update,())
        thread.start_new_thread(self.status,())

gamepad1 = ol_Gamepad(0)
gamepad2 = ol_Gamepad(1)
gamepad1.updater()
gamepad2.updater()
