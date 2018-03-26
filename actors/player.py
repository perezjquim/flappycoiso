from etc.util import *
from actors.actor import *

SAMPLING_RATE = 0.01
DEFAULT_POS_X = 100
DEFAULT_POS_Y = 100
UP_STRENGTH = 20
GRAVITY = 10

class Player(Actor):
	def __init__(self,pygame,screen,image_name,TOP_BORDER,BOTTOM_BORDER):
		Actor.__init__(self,pygame,screen,image_name)
		self.x = DEFAULT_POS_X
		self.y = DEFAULT_POS_Y
		self.TOP_BORDER = TOP_BORDER
		self.BOTTOM_BORDER = BOTTOM_BORDER
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