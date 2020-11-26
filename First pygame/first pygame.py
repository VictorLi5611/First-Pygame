import pygame
import time
import random
# pylint: disable=no-member
# PLEASE CHANGE THE DIRECTORY FOR THE IMAGE!!!!
pygame.init()

#loads the image
carImg = pygame.image.load("racecar.png")
#########################################################################################

#the width and height of the display
displayWidth = 800
displayHeight = 600

#setting the colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blockColour = (53,115,255)

carWidth = 73

#setting up the display,name and FPS
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Dodge the Blocks")
clock = pygame.time.Clock()



def thingsDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingX, thingY, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])


def car(x,y):
    gameDisplay.blit(carImg, (x,y)) 

#Funtion that displays text
def textObjects(text,font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = (displayWidth/2), (displayHeight/2)
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    gameLoop()
###############################################################################################

def crash():
    messageDisplay("You Crashed")

def gameLoop():

    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)
    xInc = 0

    
    thingSpeed = 4
    thingWidth = 100
    thingHeight = 100
    numThings = 4
    xLoc = 0
    yLoc = 1
    thingStartX = random.randrange(0, displayWidth - thingWidth)
    thingStartY = -600
    thingLoc = []
    for _ in range (numThings):
        thingLoc.append([thingStartX,thingStartY])
        thingStartX = random.randrange(0, displayWidth)
        thingStartY -= -300

    dodged = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #keyboard inputs 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xInc = -5
                elif event.key == pygame.K_RIGHT:
                    xInc = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xInc = 0
            ######
        

        x += xInc

        gameDisplay.fill(white)   
        for thing in thingLoc:
        # things(thingX, thingY, thingW, thingH, color):
            things(thing[xLoc], thing[yLoc], thingWidth, thingHeight, blockColour) 
            thing[yLoc] += thingSpeed
            car(x,y)
            thingsDodged(dodged)

            if x > displayWidth - carWidth or x < 0:
                crash()

            if thing[yLoc] > displayHeight:
                thing[yLoc] = 0 - thingHeight
                thing[xLoc] = random.randrange(0, displayWidth - thingWidth)
                dodged += 1 
                thingSpeed += 0.1

            #collition
            if y < thing[yLoc] + thingHeight:
                if x > thing[xLoc] and x < thing[xLoc] + thingWidth or x + carWidth > thing[xLoc] and x + carWidth < thing[xLoc] + thingWidth:
                    crash()

        #this updates the screen
        pygame.display.update()

        #num is the FPS of the Game
        clock.tick(30)


gameLoop()
pygame.quit()
quit()