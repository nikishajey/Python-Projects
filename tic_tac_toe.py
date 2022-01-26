#! /usr/bin/env python

import pygame
from pygame.locals import *
import sys
import time

# variables 
X_or_O = 'x'
winner = None
draw = False
turns_left = 9
fps = 20

# board variables 
width = 400
height = 400
black = (10,10,10)
#w = (255, 255, 255)

# create board
board = [[None]*3, [None]*3, [None]*3]

# initialize game
pygame.init()
# keep time
clock = pygame.time.Clock()
# display the board
canvas = pygame.display.set_mode((width, height+100),0,32)
pygame.display.set_caption("Tic Tac Toe")

# x and o images 
x = pygame.image.load('x.png')
x = pygame.transform.scale(x, (90,90))
o = pygame.image.load('o.png')
o = pygame.transform.scale(o, (90,90))
# main tic tac image
tictac = pygame.image.load('tic.png')
tictac = pygame.transform.scale(tictac, (width, height+100))

def startGame():
    # put images on top of another
    canvas.blit(tictac,(0,0))
    # update the display
    pygame.display.update()
    # wait 1 second
    time.sleep(2)
    # fill entire canvas as white after main image is displayed 
    canvas.fill((255,255,255))
    # draw vertical grid lines
    pygame.draw.line(canvas, black,(width/3,0), (width/3,height), width=7)
    pygame.draw.line(canvas, black,((width/3)*2,0), ((width/3)*2,height), width=7)
    # draw horizontal grid lines
    pygame.draw.line(canvas, black,(0,height/3), (width,height/3), width=7)
    pygame.draw.line(canvas, black,(0,(height/3)*2), (width,(height/3)*2), width=7)
    # check the drawing
    drawProgress()
    
def drawProgress():
    # function that either initially starts the game or checks if there's a win/draw and then replays
    # check if someone won
    global draw
    if winner is None:
        message = X_or_O.upper() + "'s Turn"
    # display winner
    else:
        message = winner.upper() + " won!"
    # if game finishes as a draw
    if draw:
        message = 'Game Draw!'
    # create the font
    font = pygame.font.Font(None, 30)
    # render font to the messages when displayed 
    text = font.render(message, 1, (255, 255, 255))  
    # create a small box at the bottom of canvas to display wins etc.
    canvas.fill ((0, 0, 0), (0, width, height+100, 100))
    # put message on canvas with a box around it 
    text_result = text.get_rect(center =(width/2, height+100-50))
    # display text and text's rectangle on display
    canvas.blit(text, text_result)
    # update the display
    pygame.display.update() 

def checkWin():
    # check if there is a win everytime we input an X or O
    # first check any column wins
    global board, winner, draw
    for col in range(0,3):
        if (board[0][col] is not None) and (board[0][col] == board[1][col] == board[2][col]):
            # won
            winner = board[0][col]
            # draw the winning red line
            pygame.draw.line(canvas, (250,0,0), ((col + 1)*width/3 - width/6, 0), ((col + 1)* width/3 - width/6, height), 4)
            
            break
    # check for any row winners
    for row in range(0,3):
        if (board[row][0] is not None) and (board[row][0] == board[row][1] == board[row][2]):
            # won
            winner = board[row][0]
            # draw winning red line
            pygame.draw.line(canvas, (255,0,0), (0, ((row+1)*height/3 - height/6)), (width, ((row+1)*height/3 - height/6)), 4)
            break
    # check for diagonal winner
    rc=0
    if (board[rc][rc] is not None) and (board[rc][rc] == board[rc+1][rc+1] == board[rc+2][rc+2]):
        # win
        winner = board[rc][rc]
        pygame.draw.line(canvas, (255,0,0), (0,0), (width,height), 4)
    elif (board[0][2] is not None) and (board[0][2] == board[1][1] == board[2][0]):
        # win
        winner = board[0][2]
        pygame.draw.line(canvas, (255,0,0), (width,0), (0,height), 4)
    # check for draw
    if turns_left == 0:
        draw = True
    drawProgress()

def drawXO(row, column):
    # generates an X or O on square that is clicked 
    global board, X_or_O, turns_left
    if row == 1:
        pos_x = 30 
    if row == 2:
        pos_x = width/3 + 30
    if row == 3:
        pos_x = width/3*2 + 30
    # chcekc column 
    if column == 1:
        pos_y = 30
    if column == 2:
        pos_y = height/3 + 30
    if column == 3:
        pos_y = height/3*2 + 30
    # put x or o onto the correct position
    board[row-1][column-1] = X_or_O
    # check if player is x or o
    if X_or_O == 'x':
        # insert x image here
        canvas.blit(x, (pos_y,pos_x))
        turns_left -= 1
        X_or_O = 'o'
    elif X_or_O == 'o':
        # insert y image here
        canvas.blit(o, (pos_y,pos_x))
        turns_left -= 1
        X_or_O = 'x'
    # update display
    pygame.display.update()

def userClick():
    # FCN LOADED EVERTIME THERE IS A MOUSE CLICK
    # get the coordinates of click
    (x_cor,y_cor) = pygame.mouse.get_pos()
    # get column of mouse click
    if(x_cor < width/3):
        column = 1
    elif ((x_cor < (width/3)*2) and (x_cor > width/3)):
        column = 2
    elif((x_cor < width) and (x_cor > (width/3)*2)):
        column = 3
    else:
        column = None
    # get row of click
    if(y_cor < height/3):
        row = 1
    elif ((y_cor < (height/3*2)) and (y_cor > height/3)):
        row = 2
    elif((y_cor < height) and (y_cor > (height/3*2))):
        row = 3
    else:
        row = None
    # check if valid place on board
    if(row and column and board[row-1][column-1] is None):
        # draw the x or o on screen
        drawXO(row,column)
        # check if there is a win or draw 
        checkWin()

def reset():
    global board, winner,XO, draw
    time.sleep(3)
    x_or_o = 'x'
    draw = False
    winner = None
    turns_left = 9
    board = [[None]*3,[None]*3,[None]*3]
    startGame()


if __name__ == "__main__":
    startGame()
    # run the game loop forever
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # the user clicked; place an X or O
                userClick()
                if(winner or draw):
                    reset()
        pygame.display.update()
        clock.tick(fps)
