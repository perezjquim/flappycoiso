import pygame
import thread
import time
from pygame.locals import *

RES_X = 500
RES_Y = 500
BORDER_THRESHOLD = 70
SAMPLING_RATE = 0.02
DEFAULT_POS_X = 100
DEFAULT_POS_Y = 100

class Player:
	def __init__(self,pygame):
		self.pygame = pygame
		self.x = DEFAULT_POS_X
		self.y = DEFAULT_POS_Y
		try:
			thread.start_new_thread(self.act,())
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass

	def act(self):
		while 1:
			self.handleGravity()
			self.handleControls()
			time.sleep(SAMPLING_RATE)

	def handleGravity(self):
		self.move(-10)

	def handleControls(self):
		keys = self.pygame.key.get_pressed()
		if keys[K_UP]:
			self.move(20)

	def move(self,quantity):
		if (quantity > 0 and self.y > 0 - BORDER_THRESHOLD/8) or (quantity < 0 and self.y < RES_Y - BORDER_THRESHOLD):
			self.y = self.y - quantity