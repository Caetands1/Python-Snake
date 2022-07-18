import random
from tkinter import scrolledtext
import pygame
import math as m


pygame.init()
pygame.font.init()
WIDTH, HEIGHT= 600,500
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SNAKE PROJECT')


#VARIABLES
FPS = 144
initiated = False
screenrect = SCREEN.get_rect()
screencenter = screenrect.center
bgclr = (81, 112, 54)
BLACK = 0,0,0
speed = 2
x=0
y=0
xchange = 0 
ychange = 0
my_font = pygame.font.SysFont('Comic Sans MS', 30)
score = 0


class objects:
    def __init__(self,colour ,location ,size, name, surface=SCREEN):
        self.surface = surface
        self.colour = colour
        self.location = location
        self.size = size
        self.name = name
        
    def drawobject(self):
        
        self.name = pygame.draw.circle(self.surface,self.colour,self.location,self.size, width=0)

    def randomcoord(self):
        coord = (random.randrange(40,560), random.randrange(40,460))
        return coord
        

class snakeobj(objects):
    def __init__(self,colour,location, size,name):
        super().__init__(colour, location, size,name)
        
    def move(self,x,y,apple):
        SCREEN.fill(bgclr)
        apple.drawobject()
        self.location = (screencenter[0] + x, screencenter[1] + y)
        self.drawobject()
       

    def eat(self):
        global score
        score += 1 
        apple.location =  apple.randomcoord()
        print(score)

class appleobj(objects):
    def __init__(self,colour, location,size,name):
        super().__init__(colour,location, size,name)
        self.location = self.randomcoord()


def initialise(endrun):
    SCREEN.fill(bgclr)
    global snake
    snake = snakeobj((0,0,255),screencenter, 20 , "snakerect")
    snake.drawobject()

    global apple
    apple = appleobj((255,0,0),None,15, "applerect")
    apple.drawobject()

    if endrun:
        main(initiated,x,y,xchange,ychange)
    return snake, apple


def endscreen(endrun):
    while endrun:
        text_surface = my_font.render('GAME OVER: RESTART = ANY BUTTON', False, (255, 255, 255))
        SCREEN.blit(text_surface, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                initialise(endrun=True)
                endrun = False
                
            elif event.type == pygame.QUIT:
                pygame.quit
                endrun=False
                
     
def main(initiated,x,y,xchange,ychange):
    clock = pygame.time.Clock()
    run = True      
    while run:

        if initiated == False:
            ran = initialise(None)
            score = 0 
            snake = ran[0]
            apple = ran[1]            
            initiated = True 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                run = False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xchange = speed
                    ychange = 0
                elif event.key == pygame.K_LEFT:
                    xchange = -speed
                    ychange = 0
                elif event.key == pygame.K_DOWN:
                    xchange = 0 
                    ychange = speed
                elif event.key == pygame.K_UP:
                    xchange = 0 
                    ychange = -speed
        if m.sqrt((apple.location[0]-snake.location[0])**2 + (apple.location[1]-snake.location[1])**2) < 35:
            snake.eat()
            
        if screenrect.contains(snake.name) != True:
            endscreen(endrun = True)
            run = False
        
        txt = my_font.render(f'Score: {score}', False, (255, 255, 255))
        SCREEN.blit(txt, (25,25))

        x += xchange
        y += ychange 
        snake.move(x,y,apple)
        clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    main(initiated,x,y,xchange,ychange)

pygame.quit()