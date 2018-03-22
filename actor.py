import pygame
from pygame.locals import *
from util import *

class Actor:
	def __init__(self,pygame,screen,image_name):
		self.pygame = pygame
		self.image =  pygame.image.load(image_name)
		self.screen = screen

	def draw(self):
		self.screen.blit(self.image,(self.x,self.y))	