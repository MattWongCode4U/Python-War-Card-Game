from random import shuffle
"""
CardModule.py

Contains classes of a Card and CardDeck and their respective
functionalities.
"""

class Card:
    "Class for a playing card"

    #Initializes a card
    def __init__(self, value, suit):
        """
        Card initializer.

        Args:
            value:  Numeric value of the card.
            suit:   Suit of the card.
        """
        self.value = value
        self.suit = suit

    #Get number value of the card
    def getValue(self):
        """
        Get number value of the card.

        Returns:
            Value of the card.
        """
        return self.value

    #Get suit of the card
    def getSuit(self):
        """
        Get suit of the card.

        Returns:
            Suit of the card.
        """
        return self.suit

    #Print value and suit of the card
    def printCardInfo(self):
        """
        Print value and suit of the card
        """
        print("Card: ", self.value, "-", self.suit)


class CardDeck:
    "Class for a deck of playing cards"

    SuitValues = ["Spades", "Hearts", "Diamonds", "Clubs"]

    #Initializes card deck
    def __init__(self):
        """
        CardDeck initializer.
        """
        self.deck = []
        self.fillDeck()
        self.shuffleDeck()
        
    #Fill deck with cards
    def fillDeck(self):
        """
        Fill the deck with cards.
        """
        #Ace - King (1- 13)
        for i in range(1, 14):
            #Suits (Spades, Hearts, Diamonds, Clubs)
            for j in range(0, 4):
                tmpCard = Card(i, CardDeck.SuitValues[j])
                self.deck.append(tmpCard)

    #Shuffle the deck of cards randomly
    def shuffleDeck(self):
        """
        Shuffle the deck randomly.
        """
        shuffle(self.deck)

    #Get the amount of cards still in the deck
    def getCardCount(self):
        """
        Get the amount of cards still in the deck.

        Returns:
            Amount of cards in the deck.
        """
        return len(self.deck)

    #Draw a card from the deck
    def drawCard(self):
        """
        Draw a card from the deck.
        
        Returns:
            Card drawn from the deck.
        """
        return self.deck.pop()

    #Print the contents of the cards still in the deck
    def printDeck(self):
        """
        Print the contents of the cards still in the deck.
        """
        for i in range(0, self.getCardCount()):
            self.deck[i].printCardInfo()
