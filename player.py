import pygame
from pygame.locals import *
from util import *

SAMPLING_RATE = 0.01
DEFAULT_POS_X = 100
DEFAULT_POS_Y = 100
UP_STRENGTH = 20
GRAVITY = 10

class Player:
	def __init__(self,pygame,screen,image_name,TOP_BORDER,BOTTOM_BORDER):
		self.pygame = pygame
		self.image =  pygame.image.load(image_name)
		self.screen = screen
		self.x = DEFAULT_POS_X
		self.y = DEFAULT_POS_Y
		self.TOP_BORDER = TOP_BORDER
		self.BOTTOM_BORDER = BOTTOM_BORDER
		CyclicThread(self.act,SAMPLING_RATE)

	def act(self):		
		self.handleGravity()
		self.handleControls()

	def draw(self):
		self.screen.blit(self.image,(self.x,self.y))

	def handleGravity(self):
		self.move(-GRAVITY)

	def handleControls(self):
		keys = self.pygame.key.get_pressed()
		if keys[K_UP]:
			self.move(UP_STRENGTH)		

	def move(self,quantity):
		if (quantity > 0 and self.y > self.TOP_BORDER) or (quantity < 0 and self.y < self.BOTTOM_BORDER):
			self.y = self.y - quantity