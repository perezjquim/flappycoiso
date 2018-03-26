from actors.player import *
from actors.obstacle import *
from etc.util import *
from pygame.locals import *
from ui.application import *
from ui.mainmenu import *
from ui.endmenu import *
import pygame
import os

RES_X = 500
RES_Y = 500
SAMPLING_RATE = 0.01
OBSTACLE_SPAWN_RATE = 20
PLAYER_SKIN = os.path.dirname(__file__) + "/images/gold-ball.png"
OBSTACLE_SKIN = os.path.dirname(__file__) + "/images/beeper.png"

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((RES_X, RES_Y))
		self.player = Player(pygame,self.screen,PLAYER_SKIN,RES_X,RES_Y)
		self.obstacles = []
		self.running = True
		self.score = 0
		self.quitHandler = CyclicThread(self.handleQuit,SAMPLING_RATE)	

		while self.running == True:
			self.draw()		
			self.act()
			time.sleep(SAMPLING_RATE)
			self.score = self.score + 0.1

		self.quitHandler.stop()
		pygame.quit()
		EndMenu(int(self.score))

	def handleQuit(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				exit(0)
		time.sleep(SAMPLING_RATE)

	def drawActors(self):
		for o in self.obstacles:
			if(o.x > 0):
				o.draw()
		self.player.draw()

	def draw(self):
		self.screen.fill(0)
		self.drawActors()
		pygame.display.flip()
		for o in self.obstacles:
			if abs(o.x-self.player.x) < self.player.image.get_width()*0.5 - 10 and abs(o.y-self.player.y) < self.player.image.get_height()*0.5 - 10:	
				self.stopGame()
				self.stopActors()
				return	

	def act(self):
		if randint(0,OBSTACLE_SPAWN_RATE) == 0:
			o = Obstacle(pygame,self.screen,OBSTACLE_SKIN,RES_X,RES_Y)	
			self.obstacles.append(o)

	def stopActors(self):
		for o in self.obstacles:
			o.thread.stop()
		self.player.thread.stop()

	def stopGame(self):
		self.running = False