from Card import Card

#Hand
class Hand(Card):
	#Initiate the hand
	def __init__(self,cards=[]):
		self.cards = cards

	#Print out your whole hand
	def __str__(self,joinWith=','):
		handStr = ''
		for card in self.cards:
#			print card
			handStr += str(card) 
			handStr += joinWith
		#Returns all of the cards (with no trail joinWith character)
		return handStr[:-1]
