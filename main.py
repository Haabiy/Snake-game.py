import pygame
import time
import random
pygame.init()

# Initialize some colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255,255,255)
yellow = (255, 255 , 102)

#set a timer and the speed of the snake
timer = pygame.time.Clock()
speed = 7

# Initialize Snake class
class Snake:

    # Parameters required for us to make the board and set positions
    def __init__(self, x=int(), y=int(), length=int(), width=int()):

        self.game_on = bool(True)

        # Initialize the positions
        self.x = x
        self.y = y

        # Initialize new positions
        new_x = int(0)
        new_y = int(0)

        # Accessible in the class
        self.new_x = new_x
        self.new_y = new_y

        # Initialize length and width of the board
        self.length = length
        self.width = width

        # initialize length and width of the snake

        self.s_length= int(20)
        self.s_width = int(20)

        # Board length and width
        self.disp = pygame.display.set_mode((self.length, self.width))

    def play(self):

        # Food position along x and y axis
         food_x = int(random.randrange(0, self.length) / 2)
         food_y = int(random.randrange(0, self.width) / 2)

        # Initializing a counter
         count = int(0)

         # creating a loop
         while(self.game_on==True):

             # Board name
             pygame.display.set_caption("Snake game")

             #Background color
             self.disp.fill((13, 14, 39))

             # Snake's positions and dimentions
             pygame.draw.rect(self.disp, green, [self.x, self.y, self.s_length, self.s_width])
             pygame.display.update()

             # Controls keystrokes and others
             for event in pygame.event.get():

                 # Handle other events
                 if (event.type == pygame.QUIT):
                     self.game_on = False
                     pygame.display.quit()
                     exit()

                 # Waiting for the keystroke to execute the conditions
                 if(event.type == pygame.KEYDOWN):

                     # Condtions for Right, Left, Up and Down
                     if event.key == pygame.K_RIGHT:
                         self.new_x = 20
                         self.new_y = 0
                     elif event.key == pygame.K_LEFT:
                         self.new_x = -20
                         self.new_y = 0
                     elif event.key == pygame.K_UP:
                         self.new_x = 0
                         self.new_y = -20
                     elif event.key == pygame.K_DOWN:
                         self.new_x = 0
                         self.new_y = 20

             # Update postions
             self.x = self. x + self.new_x
             self.y = self.y + self.new_y

             # Locate where the food is
             pygame.draw.rect(self.disp, yellow, [food_x, food_y, 20, 20])
             # Updated positions
             pygame.draw.rect(self.disp, green, [self.x, self.y, self.s_length, self.s_width])

             # Getting the food
             if self.x >= food_x and self.x <= food_x+ 25 and self.y >= food_y and self.y <= food_y + 25:

                     # 50 points/food
                     count += 50
                     pygame.draw.rect(self.disp, green, [self.x, self.y, self.s_length + 20, self.s_width])
                     #print("count = ", count)

                     # Eaten? then update to other postions
                     food_x = int(random.randrange(0, self.length) / 2)
                     food_y = int(random.randrange(0, self.width) / 2)

             pygame.display.update()
             #print("Snake_X, Food_x :", self.x, food_x)
             #print("Snake_Y, Food_y :", self.y, food_y)

             #Control the speed
             timer.tick(speed)

             # Make boundaries
             if( self.x >self.length or self.x <0 or self.y >self. width or self.y <0):
                 self.game_on = False

         pygame.display.update()
         # Dispaying the score
         font_style = pygame.font.SysFont(None, 50)
         score = font_style.render("Score = "+ str(count), True, white)
         self.disp.blit(score, [self.length/2 -95 , 0])
         pygame.display.update()

         # sets an icon
         pygame.display.set_icon(self.disp)
         print("\n//////// GAME OVER //////// ")
         print("\n//////// Total score = ", count, "////////")

         # sleeps for 3 secs
         time.sleep(3)
         pygame.quit()
         quit()

if __name__ == "__main__":

 # position x, position y, board length, board width
 Game = Snake(50, 50, 600, 600)
 Game.play()


