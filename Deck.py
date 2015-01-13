from Card import Card

#Deck
class Deck(Card):
	'''Definition of a card deck.'''
	from random import shuffle as rShuffle

	def __init__(self,hasJoker=False):
		#Assemble deck
		self.cards = [Card(v,s) for v in self.values for s in self.suits]
		#Add Joker cards (2) as 'WW' if needed
		#if(hasJoker):
		#	self.cards.extend([('W','W'),('W','W')])

	#Draw a card from the deck and return a card
	def draw(self,fromTop=True):
		#Remove from the front/top of deck
		if fromTop:
			return self.cards.pop(0)
		#Remove from the back/bottom of deck
		else:
			return self.cards.pop()

	#Return how many cards are in deck
	def sizeOf(self):
		return len(self.cards)

	#Shuffle deck and return the newly shuffled deck
	def shuffle(self):
		#Use random.shuffle() method
		rShuffle(self.cards)
		return self.cards
