import random
import pygame
import math as m 
from sys import exit


class snake:
    def __init__(self, p_screen):
        self.p_screen = p_screen
        self.screenrect = self.p_screen.get_rect()
        self.screencenter = self.screenrect.center
        self.bgclr = (0,255,64)
        self.location = self.screencenter
       
        
    def draw(self):
        self.name = pygame.draw.circle(self.p_screen, (0,0,255), (self.location), 20)

    def move(self,x2,y2):
        self.p_screen.fill(self.bgclr)
        game.apple.draw()
        self.location = (self.screencenter[0] + x2, self.screencenter[1] + y2)
        self.draw()

    def eat(self):
        game.apple.location = game.apple.randomcoord()
        game.apple.draw()
        game.score += 1
        self.snakelength += 1

class apple:

    def __init__(self, p_screen):
        self.p_screen = p_screen
        self.screenrect = self.p_screen.get_rect()
        self.location = self.randomcoord()

    def draw(self):
        self.name = pygame.draw.circle(self.p_screen, (255,0,0), (self.location[0],self.location[1]), 15)
    
    def randomcoord(self):
        return (random.randrange(50,550), random.randrange(50,450))


class game:

    def __init__(self):
        self.initialise()

    def initialise(self):
        pygame.init()
        pygame.font.init()
        WIDTH, HEIGHT= 600,500
        self.SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
        self.bgclr = (0,255,64)
        self.SCREEN.fill(self.bgclr)
        pygame.display.set_caption('SNAKE PROJECT')
        self.snake = snake(self.SCREEN)
        self.snake.draw()
        self.apple = apple(self.SCREEN)
        self.apple.draw()
        self.speed = 5
        self.FPS = 60
        self.x1 = 0
        self.y1 = 0
        self.xchange = 0
        self.ychange = 0
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = 0 
        self.snakelength = 1


    def main(self,run):

        self.run = run
        clock = pygame.time.Clock()
        print("running")
        self.SCREEN.fill(self.bgclr)
        while run:    

            for event in pygame.event.get():   
                   
                if event.type == pygame.QUIT:
                    run = False  

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.xchange = self.speed
                        self.ychange = 0
                    elif event.key == pygame.K_LEFT:
                        self.xchange = -self.speed
                        self.ychange = 0
                    elif event.key == pygame.K_DOWN:
                        self.xchange = 0 
                        self.ychange = self.speed
                    elif event.key == pygame.K_UP:
                        self.xchange = 0 
                        self.ychange = -self.speed

            if m.sqrt((game.snake.location[0] - game.apple.location[0])**2 + (game.snake.location[1] - game.apple.location[1])**2) <= 35:
                game.snake.eat()
                print(game.score)
            
            if game.snake.screenrect.contains(game.snake.name) != True:
                self.run = False
                game.gameover(endrun = True)
                
            
            self.snakeblocks = []
            self.snakehead = []
            self.snakehead.append(game.snake.name.x)
            self.snakehead.append(game.snake.name.y)
            self.snakeblocks.append(self.snake_head)

            self.x1 += self.xchange
            self.y1 += self.ychange 
            self.snake.move(self.x1,self.y1)  
            self.updatescore() 
            pygame.display.update()
            clock.tick(self.FPS)    
            
        self.run = False

    def updatescore (self):
        txt = (f'Score: {self.score}')
        scoretext =  self.my_font.render(txt, False, (255, 255, 255))      
        self.SCREEN.blit(scoretext, (50,50))

    def gameover(self,endrun):
        while endrun:
            
            text_surface = self.my_font.render('GAME OVER: RESTART = ANY BUTTON', False, (255, 255, 255))
            self.SCREEN.blit(text_surface, (0,0))
            pygame.display.update()
            
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    endrun = False
                    self.initialise()
                    game.main(True)

                elif event.type == pygame.QUIT:
                    endrun= False
                    pygame.quit()
                    quit()
                    
            

if __name__ == '__main__':
    
    game = game()
    game.main(True)
        
