import Hand from Hand

#Player for the game of Crak
class Player:
	#Initiate the player with a name
	def __init__(self,name):
		self.name = name
		#Define the different hands (empty)
		self.handMine = Hand() #only Player sees
		self.handShow = Hand() #all players see
		self.handHide = Hand() #no players see
