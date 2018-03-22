import pygame
import thread
import time
from pygame.locals import *

class Player:
	def __init__(self):
		self.x = 100
		self.y = 100
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
			time.sleep(0.001)
			self.handleGravity()
			self.handleControls()

	def handleGravity(self):
		self.move(-1)

	def handleControls(self):
		keys = pygame.key.get_pressed()
		if keys[K_UP]:
			self.move(2)

	def move(self,quantity):
		if (quantity > 0 and self.y > 0) or (quantity < 0 and self.y < 400):
			self.y = self.y - quantity





pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
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


