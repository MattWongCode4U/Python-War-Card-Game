from deck_pkg.CardModule import CardDeck

def main():
    print("Setting up War Card Game")
    gameDeck = CardDeck()
    gameDeck.fillDeck()
    gameDeck.shuffleDeck()
    print("Cards in deck: ", gameDeck.getCardCount())

    pDeck = CardDeck()
    cpuDeck = CardDeck()

    while gameDeck.getCardCount() > 0:
        pDeck.addCardToBottom(gameDeck.drawCard())
        cpuDeck.addCardToBottom(gameDeck.drawCard())

    print("Cards in PLAYER deck: ", pDeck.getCardCount())
    print("Cards in CPU deck: ", cpuDeck.getCardCount())
    
    print("\nBeginning War Card Game\n")

    gameRunning = True

    while gameRunning:
        print("\nDrawing cards...")
        pCard = pDeck.drawCard()
        print("Your card: ", pCard.getValue(), pCard.getSuit())
        cpuCard = cpuDeck.drawCard()
        print("CPU's card: ", cpuCard.getValue(), cpuCard.getSuit())

        #Compare card values
        if pCard.getRawValue() > cpuCard.getRawValue():
            #player won
            pDeck.addCardToBottom(pCard)
            pDeck.addCardToBottom(cpuCard)
            print("You win the round.")
        elif pCard.getRawValue() < cpuCard.getRawValue():
            #cpu won
            cpuDeck.addCardToBottom(pCard)
            cpuDeck.addCardToBottom(cpuCard)
            print("You lose the round.")
        else:
            #War
            print("WAR!!!!!!!!!!!!!!!!!!")
            war = True
            ptemplist = []
            cputemplist = []
            ptemplist.append(pCard)
            cputemplist.append(cpuCard)
            while war:
                if pDeck.getCardCount() <= 1:
                    print("Player doesn't have enough cards for War, you Lose!")
                    war = False  
                elif cpuDeck.getCardCount() <= 1:
                    print("CPU doesn't have enough cards for War, you Win!")
                else:
                    ptemplist.append(pDeck.drawCard())
                    cputemplist.append(cpuDeck.drawCard())

                    pwar = pDeck.drawCard()
                    cpuwar = cpuDeck.drawCard()
                    ptemplist.append(pwar)
                    cputemplist.append(cpuwar)
                    
                    if pwar.getRawValue() > cpuwar.getRawValue():
                        #player wins war
                        print("You win the War!")
                        pDeck.deck.extend(ptemplist)
                        pDeck.deck.extend(cputemplist)
                        war = False
                    elif pwar.getRawValue() < cpuwar.getRawValue():
                        #cpu wins war
                        print("You lose the War!")
                        cpuDeck.deck.extend(ptemplist)
                        cpuDeck.deck.extend(cputemplist)
                        war = False
                    else:
                        #war is tied, repeat
                        print("War continuing!")
                        war = True
            
        print("Player Deck: ", pDeck.getCardCount(), " - CPU Deck: ", cpuDeck.getCardCount(), "\n")

        #Check game win / lose condition
        if(pDeck.getCardCount() == 0):
            print("You lose the game")
            gameRunning = False
        elif(cpuDeck.getCardCount() == 0):
            print("You win the game")
            gameRunning = False
        else:
            gameRunning = True
                
        #Wait for user input for next action
        if(gameRunning):
            gameRunning = handleInput(pDeck, cpuDeck)

def handleInput(playerDeck, computerDeck):
    playing = True
    while True:
        playerInput = input("\nPlay Round (P), Print Score (S), Exit Game (X)\n")
        if playerInput.lower() == "p":
            playing = True
            break
        elif playerInput.lower() == "s":
            print("Player Deck: ", playerDeck.getCardCount(), " - CPU Deck: ", computerDeck.getCardCount())
            continue
        elif playerInput.lower() == "x":
            playing = False
            print("Thanks for playing!")
            break
        else:
            print("Unexpected input, try again!")
            continue
    return playing

main()
