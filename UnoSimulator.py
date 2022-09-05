# Imports
import random
import time


# Variables
bots = ["Kinglord", "Gerard", "Friday", "Sebastian", "Dhanush", "Aishwarya", "Devjith", "Jishnu", "Saaish", "Siddharth"]
fullDeck = {
	"red": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "reverse", "skip", "+2"],
	"blue": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "reverse", "skip", "+2"],
	"yellow": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "reverse", "skip", "+2"],
	"green": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "reverse", "skip", "+2"],
	"special": ["+4", "+4", "wild", "wild"]
}


# Classes
class Player:
	def __init__(self, category, name, deck):
		self.category = category
		self.name = name
		self.deck = deck

class Card:
	def __init__(self, color, number):
		self.color = color
		self.number = number


# Functions
def pretty_print(currentPlayer):
	print(currentPlayer.name, "'s Deck:")
	for x in currentPlayer.deck:
		print(x.color, x.number)
	print("\n")

def deck_maker(CardCount):
	deck = []
	for x in range(CardCount):
		selection = [random.choice(list(fullDeck.keys()))]
		selection.append(random.choice(fullDeck[selection[0]]))
		deck.append(Card(selection[0], selection[1]))
	return deck

def ability_card(direction, currentCard, selectedCard, currentPlayer, nextPlayer, activeBots):
	changeColor = False
	hasAbility = False
	jump = True
	if selectedCard.color == "special":
		hasAbility = True
		selectedCard.color = random.choice(["red", "blue", "yellow", "green"])
		print(currentPlayer.name, "changed the color to", selectedCard.color)
		if selectedCard.number == "wild":
			jump = False
		elif selectedCard.number == "+4":
			nextPlayer.deck += deck_maker(4)
			print(nextPlayer.name, "picked up 4 cards and their turn got skipped!")
	if selectedCard.number == "+2":
		hasAbility = True
		nextPlayer.deck += deck_maker(2)
		print(nextPlayer.name, "picked up 2 cards and their turn got skipped!")
	elif selectedCard.number == "reverse":
		hasAbility = True
		if len(activeBots) != 2:
			jump = False
			direction *= -1
	elif selectedCard.number == "skip":
		hasAbility = True
		print(nextPlayer.name, "got skipped!")
	if hasAbility == True:
		if jump == True:
			nextPlayer = (activeBots[(activeBots.index(nextPlayer) + (1 * direction)) % len(activeBots)])
	return selectedCard, nextPlayer, direction

def finishTurn(direction, playableCards, currentPlayer, nextPlayer, currentCard, activeBots, ):
	selectedCard = random.choice(playableCards)
	print(currentPlayer.name, "played", selectedCard.color, selectedCard.number, "\n")
	selectedCard, nextPlayer, direction= ability_card(direction, currentCard, selectedCard, currentPlayer, nextPlayer, activeBots)
	currentCard = selectedCard
	currentPlayer.deck.remove(selectedCard)
	return nextPlayer, currentCard

def bot_play(direction, currentPlayer, currentCard, activeBots, delay, pickLimitReached):
	nextPlayer = (activeBots[(activeBots.index(currentPlayer) + (1 * direction)) % len(activeBots)])
	playableCards = []
	pretty_print(currentPlayer)
	for card in currentPlayer.deck:
		if card.color == currentCard.color or card.number == currentCard.number or card.color == "special":
			playableCards.append(card)
	if len(playableCards) == 0 and pickLimitReached == False:
		newCard = deck_maker(1)[0]
		currentPlayer.deck.append(newCard)
		print(currentPlayer.name, "picked up", newCard.color, newCard.number, "\n")
		if pickLimitReached == False:
			currentPlayer, currentCard = bot_play(direction, currentPlayer, currentCard, activeBots, delay, True)
	elif len(playableCards) != 0:
		nextPlayer, currentCard = finishTurn(direction, playableCards, currentPlayer, nextPlayer, currentCard, activeBots)
	time.sleep(delay)
	return nextPlayer, currentCard

def start(activeBots, delay, startTime):
	winners = []
	currentCard = deck_maker(1)[0]
	currentPlayer = activeBots[0]
	direction = 1
	while True:
		print("The face card is:", currentCard.color, currentCard.number, "\n")
		nextPlayer, currentCard = bot_play(direction, currentPlayer, currentCard, activeBots, delay, False)
		if len(currentPlayer.deck) == 1:
			uno = random.randint(1, 10)
			if uno == 1 or uno == 2:
				print(currentPlayer.name, "forgot to say Uno!\n")
				currentPlayer.deck += deck_maker(4)
				print(currentPlayer.name, "picked up 4 cards!")
			else:
				print(currentPlayer.name, "said Uno!\n")
		print("-------------------------------------------------------------------")
		if len(currentPlayer.deck) == 0:
			print(currentPlayer.name, "has finished their deck!")
			winners.append(currentPlayer)
			activeBots.remove(currentPlayer)
			if len(activeBots) == 1:
				print("Game Over!\n")
				print("Winner's List:")
				for x in winners:
					print(winners.index(x) + 1, "-", x.name)
				print(activeBots[0].name, "lost the game!")
				print(time.time() - startTime, "seconds!")
				break
		currentPlayer = nextPlayer

def startup():
	cardCount = int(input("Enter the number of cards to be dealt to all bots: "))
	numberOfBots = int(input("Enter number of bots you want to see play against each other (Maximum 10): "))
	delay = int(input("Enter the number of seconds you want the game to stop before letting the next bot play: "))
	print("\n")
	startTime = time.time()
	activeBots = []
	for x in range(numberOfBots):
		activeBots.append(Player("bot", bots[x], deck_maker(cardCount)))
	start(activeBots, delay, startTime)

def welcome():
	print("Welcome to Kinglord's Uno Simulator!!!\n                  -version alpha^2")
	while True:
		if input("Type 'start' to begin!\n").lower()  == "start":
			startup()
			break
		else:
			print("Type something valid!")


if __name__ == "__main__":
	welcome()
