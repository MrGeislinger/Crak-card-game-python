#Player for the game of Crak
class Player:
	#Initiate the player with a name
	def __init__(self,name):
		self.name = name
		#Define the different hands
		self.handMine = [] #only Player sees
		self.handShow = [] #all players see
		self.handHide = [] #no players see