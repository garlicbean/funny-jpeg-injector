hand = "TH TH JH KH KH"


class PokerHand(object):

	RESULT = ["Loss", "Tie", "Win"]

	def __init__(self, hand):
		self.hand = hand
		
		#Enumerates suites in hand
		self.suitEnum = {"H" : 0, "D" : 0, "C" : 0, "S" : 0}
		for i in self.hand.split(' '):
			self.suitEnum[i[1]] += 1


		#Flush Check
		self.isFlush = False
		for i in self.suitEnum:
			if self.suitEnum[i] == 5:
				self.isFlush = True

		#Straight Check
		def convertToNum(i):
			values = {'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
			if i in values:
				return values[i]
			else:
				return int(i)
		self.isStraight = False
		self.straightSource = [convertToNum(i[0]) for i in self.hand.split(' ')]
		self.straightSource.sort()
		self.straightComp = [i for i in range(self.straightSource[0], self.straightSource[0]+5)]
		if self.straightSource == self.straightComp:
			self.isStraight = True

		#Matching Card Value Check
		self.valueEnum = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}
		for i in self.straightSource:
			self.valueEnum[i] += 1
		self.fourMatch = 0
		self.threeMatch = 0
		self.twoMatch = 0
		for i in self.valueEnum:
			if self.valueEnum[i] == 4:
				self.fourMatch += 1
			elif self.valueEnum[i] == 3:
				self.threeMatch += 1
			elif self.valueEnum[i] == 2:
				self.twoMatch += 1



		##Evaluates Card Rank
		#Royale Flush
		if self.isFlush == True and self.isStraight == True and self.straightSource[0] == 10:
			self.cardrank = 10
		#Straight Flush
		elif self.isFlush == True and self.isStraight == True:
				self.cardrank = 9
		#Flush
		elif self.isFlush == True:
			self.cardrank = 6
		#Straight
		elif self.isStraight == True:
			self.cardrank = 5
		else:
			self.cardrank = 0

		pass

	def compare_with(self, other):
		pass


hand1 = PokerHand(hand)
print(hand1.suitEnum)
print(hand1.isFlush)
print(hand1.straightSource)
print(hand1.straightComp)
print(hand1.isStraight)
print(hand1.cardrank)
print(hand1.valueEnum)
print(hand1.fourMatch, hand1.threeMatch, hand1.twoMatch)