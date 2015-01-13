#Card
class Card:
	#Define the possible suits and values
	suits  = ['H','D','S','C']
	values = [str(x) for x in range(2,10)] #2-9 cards
	values.extend(['T','J','Q','K','A']) #Face cards (including the 10s)

	#Initiate card
	def __init__(self,value,suit):
		#Check to see if valid inputs, else make it None value
		self.suit = suit if suit in self.suits else None 
		self.value = value if value in self.values else None
		#Create card representation
		self.card = (self.value, self.suit)