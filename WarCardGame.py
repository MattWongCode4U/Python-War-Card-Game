from deck_pkg.CardModule import CardDeck

def main():
    print("Setting up War Card Game")
    gameDeck = CardDeck()
    print("Deck obj created")
    print("Cards in deck: ", gameDeck.getCardCount())

    print("Beginning War Card Game")

    gameRunning = True
    playerScore = 0
    cpuScore = 0

    while gameRunning:
        print("\nDrawing cards...")
        pCard = gameDeck.drawCard()
        print("Your card: ", pCard.getValue(), pCard.getSuit())
        cpuCard = gameDeck.drawCard()
        print("CPU's card: ", cpuCard.getValue(), cpuCard.getSuit())

        if pCard.getValue() > cpuCard.getValue():
            playerScore += 1
            print("You win the round.")
        elif pCard.getValue() < cpuCard.getValue():
            cpuScore += 1
            print("You lose the round.")
        else:
            #War
            print("WAR!!!!!!!!!!!!!!!!!!")
        print("Player Score: ", playerScore, " - CPU Score: ", cpuScore, "\n")

        print("Cards left in deck: ", gameDeck.getCardCount())
        if(gameDeck.getCardCount() == 0):
            print("Shuffling cards back into the deck.")
            gameDeck.fillDeck()
            gameDeck.shuffleDeck()
            print("Finished shuffling cards.")
        
        #Wait for user input for next action
        while True:
            playerInput = input("\nPlay Round (P), Print Score (S), Exit Game (X)\n")
            if playerInput.lower() == "p":
                break
            elif playerInput.lower() == "s":
                print("Player Score: ", playerScore, " - CPU Score: ", cpuScore)
                continue
            elif playerInput.lower() == "x":
                gameRunning = False
                print("Thanks for playing!")
                break
            else:
                print("Unexpected input, try again!")
                continue


main()
