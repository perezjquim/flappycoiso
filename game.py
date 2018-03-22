from player import *
from util import *
from pygame.locals import *
import pygame
import time
import threading

RES_X = 500
RES_Y = 500
BORDER_Y_TOP = 5
BORDER_Y_BOTTOM = RES_Y - 70
SAMPLING_RATE = 0.02

def handleQuit():
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
	time.sleep(SAMPLING_RATE)

def draw():
	screen.fill(0)
	screen.blit(player, (p.x,p.y))	
	pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((RES_X, RES_Y))
player = pygame.image.load("gold-ball.png")
p = Player(pygame,5,RES_Y - 70)

CyclicThread(handleQuit,SAMPLING_RATE)	

while 1:
	draw()
	time.sleep(SAMPLING_RATE)




	






