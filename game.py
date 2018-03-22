import pygame
import thread
import time
from player import *
from pygame.locals import *

RES_X = 500
RES_Y = 500
BORDER_THRESHOLD = 70
SAMPLING_RATE = 0.02
DEFAULT_POS_X = 100
DEFAULT_POS_Y = 100

pygame.init()
screen = pygame.display.set_mode((RES_X, RES_Y))
player = pygame.image.load("gold-ball.png")

def redraw():

	p = Player(pygame)	
	while 1:
		screen.fill(0)
		screen.blit(player, (p.x,p.y))	
		pygame.display.flip()
		time.sleep(SAMPLING_RATE)

try:
	thread.start_new_thread(redraw,())
except Exception as e:
	raise
else:
	pass
finally:
	pass

while 1:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
	time.sleep(SAMPLING_RATE)



