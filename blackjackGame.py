import random
from art import logo

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculateScore(cards):
    if sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, aiScore):
    if userScore == aiScore:
        return "Draw."
    elif aiScore == 0:
        return "You lose. Opponent has Blackjack."
    elif userScore == 0:
        return "Win with a Blackjack."
    elif userScore > 21:
        return "You went over. You lose."
    elif aiScore > 21:
        return "Opponent went over. You win."
    elif userScore > aiScore:
        return "You win"
    else:
        return "You lose"
    

def playGame():

    print(logo)

    myHand = []
    aiHand = []
    isGameOver = False

    for i in range(2):
        myHand.append(dealCard())
        aiHand.append(dealCard())

    while not isGameOver:
        userScore = calculateScore(myHand)
        aiScore = calculateScore(aiHand)

        print(f" Your cards: {myHand}, current score: {userScore}")
        print(f" Computer's first card: {aiHand[0]}")

        if userScore == 0 or aiScore == 0 or userScore > 21:
            isGameOver = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == "y":
                dealCard()
                myHand.append(dealCard())
            else:
                isGameOver = True

    while aiScore != 0 and aiScore < 17:
        aiHand.append(dealCard())
        aiScore = calculateScore(aiHand)

    print(f"   Your final hand: {myHand}, final score: {userScore}")
    print(f"   Computer's final hand: {aiHand}, final score: {aiScore}")
    print(compare(userScore, aiScore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  playGame()


    




    

    
