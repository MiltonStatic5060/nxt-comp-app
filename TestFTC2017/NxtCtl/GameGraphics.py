import pygame
import thread
import time


class TextDisplay(object):
    def __init__(self,name):
        #takes in 1 argument of a name
        self.arr = [name]
        self.name = name
    def reset(self):
        self.arr = [self.name]
    def addData(self,input0,input1=""):
        if input1 != "":
            input1 = " : "+str(input1)
        self.arr.append(str(input0)+str(input1))
    def updater(self):
        thread.start_new_thread(self.update,())
    def update(self):
        pygame.init()
        screen = pygame.display.set_mode((50, 50))
        pygame.display.set_caption(self.name)

        boxHeight = 0
        boxWidth = 0
        # Event loop
        while 1:
            # Set size of background
            background = pygame.Surface((boxWidth,boxHeight))
            background = background.convert()
            # Reset Background
            background.fill(pygame.Color(255,255,255))
            # Initilize the Font object
            font = pygame.font.Font(None, int(20))
            # Set the list of Strings to display
            textArr = self.arr
            # Reset window's size
            boxHeight = 0
            boxWidth = 0
            for word in textArr:
                text = font.render(word, 1, (0,0,0))
                textpos = text.get_rect()
                boxHeight+=textpos.height
                if boxWidth<=textpos.width:
                    boxWidth=textpos.width
                textpos.centerx = textpos.width/2
                textpos.centery = boxHeight-textpos.height/2
                background.blit(text, textpos)
            # Adapt screen size to the text's collective size
            screen = pygame.display.set_mode((boxWidth, boxHeight))
            # Blit everything to the screen
            screen.blit(background, (0, 0))
            pygame.display.flip()

telemetry = TextDisplay("First Display")
telemetry.updater()


#while 1:
    #time.sleep(.001)
    #telemetry.reset()
    #telemetry.addData("")
    #telemetry.addData("left trigger",gamepad1.left_trigger)
    #print(gamepad1.left_trigger)
