from ui.application import *
import game

class EndMenu(Application):

	def createWidgets(self):
		self.lblUser = Label(self)
		self.lblUser["text"] = "! GAMEOVER !"
		self.lblUser.pack(padx=self.get_padding(),pady=self.get_padding())

		self.btnReplay = Button(self)
		self.btnReplay["text"] = "REPLAY"
		self.btnReplay["command"] = self.playGame
		self.btnReplay.pack(padx=self.get_padding(),pady=self.get_padding())	

		self.btnQuit = Button(self)
		self.btnQuit["text"] = "QUIT"
		self.btnQuit["command"] = self.close
		self.btnQuit.pack(padx=self.get_padding(),pady=self.get_padding())					

	def playGame(self):
		self.close()
		game.Game()