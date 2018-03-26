from actors.player import *
from actors.obstacle import *
from etc.util import *
from pygame.locals import *
from random import randint
import pygame
import time
import threading

RES_X = 500
RES_Y = 500
BORDER_Y_TOP = 5
BORDER_Y_BOTTOM = RES_Y - 70
SAMPLING_RATE = 0.01
running = True

def handleQuit():
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
	time.sleep(SAMPLING_RATE)

def drawActors():
	for actor in actors:
		actor.draw()

def draw():
	screen.fill(0)
	drawActors()
	for actor in actors:
		if isinstance(actor,Obstacle) and abs(actor.x-player.x) < 20 and abs(actor.y-player.y) < 20:
			stopGame()
			stopActors()
			return
	pygame.display.flip()

def act():
	if randint(0,20) == 0:
		o = Obstacle(pygame,screen,"beeper.png",RES_X,RES_Y)	
		actors.append(o)

def stopActors():
	for actor in actors:
		actor.thread.stop()

def stopGame():
	global running
	running = False

pygame.init()
screen = pygame.display.set_mode((RES_X, RES_Y))

player = Player(pygame,screen,"gold-ball.png",5,RES_Y- 70)
actors = []
actors.append(player)

CyclicThread(handleQuit,SAMPLING_RATE)	

while running == True:
	draw()		
	act()	
	time.sleep(SAMPLING_RATE)

while 1:
	pass

