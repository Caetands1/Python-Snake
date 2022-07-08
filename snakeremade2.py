import random
import pygame

pygame.init()
WIDTH, HEIGHT= 600,500
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
#VARIABLES
FPS = 144
initiated = False
screenrect = SCREEN.get_rect()
screencenter = screenrect.center
bgclr = (81, 112, 54)
speed = 1
x = 0
y=0

def randomcoord():
    coord = (random.randrange(40,560), random.randrange(40,460))
    print(coord)
    return coord
class objects:
    def __init__(self,colour ,location ,size,surface=SCREEN):
        self.surface = surface
        self.colour = colour
        self.location = location
        self.size = size
        
    def drawobject(self):
        
        self = pygame.draw.circle(self.surface,self.colour,self.location,self.size, width=0)
        pygame.display.update()
        
class snakeobj(objects):
    def __init__(self,colour,location, size):
        super().__init__(colour, location, size)
    
    def move(self,event,apple,xchange=0, ychange=0):
        self.event = event
        self.xchange = xchange
        self.ychange = ychange

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xchange = speed
                ychange = 0
            elif event.key == pygame.K_LEFT:
                xchange = -speed
                ychange = 0
            elif event.key == pygame.K_DOWN:
                xchange = 0 
                ychange = -speed
            elif event.key == pygame.K_UP:
                xchange = 0 
                ychange = speed


        SCREEN.fill(bgclr)
        apple.drawobject()
        
        self.location = (screencenter[0]+self.xchange, screencenter[1]+self.ychange)
        self.drawobject()
        pygame.display.update()

class appleobj(objects):
    def __init__(self,colour, location,size):
        super().__init__(colour,location, size)
        self.location = randomcoord()

def initialise():
    SCREEN.fill(bgclr)
    snake = snakeobj((0,0,255),screencenter, 20)
    snake.drawobject()

    apple = appleobj((255,0,0),None,15)
    apple.drawobject()

    return snake, apple

def main(initiated):
    clock = pygame.time.Clock()
    run = True      
    while run:
        if initiated == False:
            ran = initialise()
            snake = ran[0]
            apple = ran[1]            
            initiated = True 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                run = False  
            
        snake.move(event,apple)
        clock.tick(FPS)


if __name__ == "__main__":
    main(initiated)

pygame.quit()

# LINE 36 X AND Y ARE RESETTING TO 0 AS EVERY TIME MOVE IS CALLED IT IS SET TO 0 -> FIND A WAY TO USE X AND Y WITHOUT SETTING TO 0 EVERY TIME