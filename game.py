import pygame
import thread
import time
from pygame.locals import *

RES_X = 800
RES_Y = 600
BORDER_THRESHOLD = 70
SAMPLING_RATE = 0.001
DEFAULT_POS_X = 100
DEFAULT_POS_Y = 100

class Player:
	def __init__(self):
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
			time.sleep(SAMPLING_RATE)
			self.handleGravity()
			self.handleControls()

	def handleGravity(self):
		self.move(-1)

	def handleControls(self):
		keys = pygame.key.get_pressed()
		if keys[K_UP]:
			self.move(2)

	def move(self,quantity):
		if (quantity > 0 and self.y > 0) or (quantity < 0 and self.y < RES_Y - BORDER_THRESHOLD):
			self.y = self.y - quantity

pygame.init()
screen = pygame.display.set_mode((RES_X, RES_Y))
player = pygame.image.load("gold-ball.png")
p = Player()

while 1:
	screen.fill(0)
	screen.blit(player, (p.x,p.y))	
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
	pass


