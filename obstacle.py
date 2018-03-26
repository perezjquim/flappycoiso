import pygame
from pygame.locals import *
from util import *
from actor import *
from random import randint

SAMPLING_RATE = 0.01
GRAVITY = 3

class Obstacle(Actor):
	def __init__(self,pygame,screen,image_name,RES_X,RES_Y):
		Actor.__init__(self,pygame,screen,image_name)
		self.x = RES_X - 50
		self.y = randint(0,RES_Y)
		self.thread = CyclicThread(self.act,SAMPLING_RATE)

	def act(self):		
		self.handleGravity()

	def handleGravity(self):
		self.move(GRAVITY)

	def move(self,quantity):
		if (self.x > 0):
			self.x = self.x - quantity