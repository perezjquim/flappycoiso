from ui.application import *
from game import *

class EndMenu(Application):

	def createWidgets(self):
		self.lblUser = Label(self)
		self.lblUser["text"] = "GAMEOVER!"
		self.lblUser.pack(padx=self.get_padding(),pady=self.get_padding())

		self.btnPlay = Button(self)
		self.btnPlay["text"] = "REPLAY"
		self.btnPlay["command"] = self.playGame
		self.btnPlay.pack(padx=self.get_padding(),pady=self.get_padding())		

	def playGame(self):
		self.close()
		Game()