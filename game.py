from actors.player import *
from actors.obstacle import *
from etc.util import *
from pygame.locals import *
import pygame

RES_X = 500
RES_Y = 500
SAMPLING_RATE = 0.01
OBSTACLE_SPAWN_RATE = 20
PLAYER_SKIN = "images/gold-ball.png"
OBSTACLE_SKIN = "images/beeper.png"
running = True

def handleQuit():
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
	time.sleep(SAMPLING_RATE)

def drawActors():
	for o in obstacles:
		o.draw()
	player.draw()

def draw():
	screen.fill(0)
	drawActors()
	pygame.display.flip()
	for o in obstacles:
		if abs(o.x-player.x) < player.image.get_width()*0.5 - 20 and abs(o.y-player.y) < player.image.get_height()*0.5 - 20:	
			stopGame()
			stopActors()
			return	

def act():
	if randint(0,OBSTACLE_SPAWN_RATE) == 0:
		o = Obstacle(pygame,screen,OBSTACLE_SKIN,RES_X,RES_Y)	
		obstacles.append(o)

def stopActors():
	for o in obstacles:
		o.thread.stop()
	player.thread.stop()

def stopGame():
	global running
	running = False

pygame.init()
screen = pygame.display.set_mode((RES_X, RES_Y))

player = Player(pygame,screen,PLAYER_SKIN,RES_X,RES_Y)
obstacles = []

CyclicThread(handleQuit,SAMPLING_RATE)	

while running == True:
	draw()		
	act()
	time.sleep(SAMPLING_RATE)

while 1:
	time.sleep(9999999)

