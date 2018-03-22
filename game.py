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
SAMPLING_RATE = 0.01

def handleQuit():
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
	time.sleep(SAMPLING_RATE)

def draw():
	screen.fill(0)
	for player in players:
		player.draw()
	pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((RES_X, RES_Y))
players = []
players.append(Player(pygame,screen,"gold-ball.png",5,RES_Y - 70))

CyclicThread(handleQuit,SAMPLING_RATE)	

while 1:
	draw()
	time.sleep(SAMPLING_RATE)