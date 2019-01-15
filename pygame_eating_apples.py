''' Here we want to setup a few things
    FIRST A game loop that will let the user to play the game again without actually exiting everytime he loses
    SECOND still show the message when we leave the game
'''
import pygame
import random

pygame.init()
#colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,180,0)

screenSize = (800,600)

block_width = 10
block_height = 10

fps = 30

# defining the diffrent blocks of the snake
def snakeBlocks(snakeList):
    for block in snakeList:
         pygame.draw.rect(gameDisplay , green , [block[0],block[1],block_width,block_height])  #needs 4 paramerters .screen . color  .[.x cordinate .y cordinate .width .height]

    
# defining a function for displaying stuff for the user
def displayMessage(msg, color, font_size):
    font = pygame.font.SysFont("Times New Roman ",font_size) # font object that will be used to draw the text on the screen 
    screen_text = font.render(msg, True,color) # renders font on to a new surfsce ''' font.render'''
    gameDisplay.blit(screen_text, [screenSize[0]/2 - screen_text.get_rect().width/2, screenSize[1]/2]) # arguments are what to print(screen_text) and wherer to print it( x and y coordinates on the screen
 
''' blit function has only 2 agruments so position should be in the for of a tuple or a list'''
''' basically the text is drawn in the rectangular form rather that letter by letter so we are actually printing that particular block on to the screen by blitting the rectangle on to the screen '''


gameDisplay = pygame.display.set_mode(screenSize)   
pygame.display.set_caption('Key Press Test')
clock = pygame.time.Clock()
# Defining a game loop

def gameLoop():
    block_x_change = 0
    block_y_change = 0
    block_x = screenSize[0]/2 # initial position of the block
    block_y = screenSize[1]/2

    gameOver = False
    gameExit = False

    apple_x = random.randrange(0,screenSize[0]-block_width,10)
    apple_y = random.randrange(0,screenSize[1]-block_height,10) #the last argument makes sure that the coordinates are in multiples of 10
    while not gameExit:

        while gameOver:
            gameDisplay.fill(white) #needs a colour in the argument
            displayMessage(" Oh Snap! You lost Ninja. Press P to play again or Q to quit", red, 20)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False # we need to do this coz if not done then it doesnt matter if we change the value of gameExit it wont QUIT coz the inner while loop will be running continuously
            
                    if event.key == pygame.K_p:
                        gameLoop()
        for event in pygame.event .get():
            if event.type == pygame.QUIT:     #Exit event management
                gameExit = True
            if event.type == pygame.KEYDOWN: # when you keep on pressing the key the keydown keeps on returning True logic ang hence every single time it will enter the corresponding if statement
                if event.key == pygame.K_LEFT and block_x>0 :
                    block_x_change = -1*block_width
                    block_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    block_x_change = block_width
                    block_y_change = 0
                elif event.key == pygame.K_UP:
                    block_y_change = -1*block_height
                    block_x_change = 0
                elif event.key == pygame.K_DOWN:
                    block_y_change = block_height
                    block_x_change = 0

        block_x += block_x_change
        block_y += block_y_change

     

        if block_x > screenSize[0]-block_width or block_x < 0 or block_y > screenSize[1]-block_height or block_y < 0:
            gameOver = True                         # boundary conditions will end that game
           
        gameDisplay.fill(white)                     #needs a colour in the argument

        pygame.draw.rect(gameDisplay , red , [apple_x,apple_y,block_width,block_height])

        snakeList = []
        blockList = []
        blockList.append(block_x)
        blockList.append(block_y)
        snakeList.append(blockList)


        snakeBlocks(snakeList)
        pygame.display.update()
        
        if apple_x == block_x and apple_y == block_y:
            apple_x = random.randrange(0,screenSize[0]-block_width,10)
            apple_y = random.randrange(0,screenSize[1]-block_height,10)
            print("eating")
        
        clock.tick(fps)
   
    pygame.quit()
    quit()
gameLoop()

