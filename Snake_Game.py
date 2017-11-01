import pygame, sys, random, time

check_Errors = pygame.init()
if check_Errors[1]>0:
    print("Had {} initializing errors".format(check_Errors[1]))
    sys.exit(-1)
else:
    print("PyGame initlialized successfully")

# PlaySurface

PlaySurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Sname game!')


# Colors

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
food = pygame.Color(128, 0, 0)


# FPS Controller

fpsController = pygame.time.Clock()

# Important Variables
smakePos = [100,60]
smakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction


#Game over Function

def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect = midtop = (360, 15)
    PlaySurface.blit(GOsurf, GOrect)

gameOver()
time.sleep(10)






























print("PyGame reached the end")
