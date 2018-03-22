import pygame
from pygame.locals import *
from util import *
import thread

SAMPLING_RATE = 0.02
DEFAULT_POS_X = 100
DEFAULT_POS_Y = 100

class Player:
	def __init__(self,pygame,TOP_BORDER,BOTTOM_BORDER):
		self.pygame = pygame
		self.x = DEFAULT_POS_X
		self.y = DEFAULT_POS_Y
		self.TOP_BORDER = TOP_BORDER
		self.BOTTOM_BORDER = BOTTOM_BORDER
		CyclicThread(self.act,SAMPLING_RATE)

	def act(self):
		self.handleGravity()
		self.handleControls()		

	def handleGravity(self):
		self.move(-30)

	def handleControls(self):
		keys = self.pygame.key.get_pressed()
		if keys[K_UP]:
			self.move(50)		

	def move(self,quantity):
		if (quantity > 0 and self.y > self.TOP_BORDER) or (quantity < 0 and self.y < self.BOTTOM_BORDER):
			self.y = self.y - quantity