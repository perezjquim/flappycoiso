from etc.util import *
from actors.actor import *

SAMPLING_RATE = 0.01
UP_STRENGTH = 20
GRAVITY = 10

class Player(Actor):
	def __init__(self,pygame,screen,image_name,RES_X,RES_Y):
		Actor.__init__(self,pygame,screen,image_name)
		self.x = RES_X/2
		self.y = RES_Y/2
		self.TOP_BORDER = 5
		self.BOTTOM_BORDER = RES_Y - 70
		self.thread = CyclicThread(self.act,SAMPLING_RATE)

	def act(self):		
		self.handleGravity()
		self.handleControls()

	def handleGravity(self):
		self.move(-GRAVITY)

	def handleControls(self):
		keys = self.pygame.key.get_pressed()
		if keys[K_UP]:
			self.move(UP_STRENGTH)		

	def move(self,quantity):
		if (quantity > 0 and self.y > self.TOP_BORDER) or (quantity < 0 and self.y < self.BOTTOM_BORDER):
			self.y = self.y - quantity