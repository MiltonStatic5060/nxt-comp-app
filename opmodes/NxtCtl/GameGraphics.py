import pygame
#from pygame.locals import *
def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))



    # Event loop
    while 1:
        # Display some text
        font = pygame.font.Font(None, int(36))
        text = font.render(str(gamepad1.left_trigger*50.0)+"\nHello", 1, (10, 10, 10))
        textpos = text.get_rect()
        screen = pygame.display.set_mode((textpos.width, textpos.height))
        textpos.left = -20
        background.fill(pygame.Color(255,255,255))
        background.blit(text, textpos)

        # Blit everything to the screen
        screen.blit(background, (0, 0))

        pygame.display.flip()


if __name__ == '__main__': main()

class Graphics(object):
    def __init__(self):
