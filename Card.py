#Card
class Card:
	#Define the possible suits and values
	suits  = ['H','D','S','C']
	values = [str(x) for x in range(2,10)] #2-9 cards
	values.extend(['T','J','Q','K','A']) #Face cards (including the 10s)

	#Initiate card
	def __init__(self,value,suit):
		#Check to see if valid inputs, else return False
		if suit in self.suits:
			self.suit  = suit
		else:
			return False
		if value in self.values:
			self.value = value
		else:
			return False
		#Return a card representation
		return (self.value, self.suit)