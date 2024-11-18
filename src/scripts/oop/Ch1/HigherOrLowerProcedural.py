# Setup 

import random

deck = {
    'rank': ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'], 
    'suit': ['Diamonds', 'Hearts', 'Clubs', 'Spades'], 
}

message = """
Welcome to Higher or Lower!
The card game where you guess what's next.
\nPick a card and place your bet if the next draw will be higher or lower in value.
\nGet it right: +20pts
Get it wrong: -15pts
"""
print(message)
print('-'*15,'\n')

# Instructions

def random_rank(deck:list):
    return deck['rank'][random.randint(0,12)]

def random_suit(deck:list):
    return deck['suit'][random.randint(0,3)]

def get_value(rank) -> int:
    if rank == 'Ace': return 1
    elif rank == 'Jack': return 11
    elif rank == 'Queen': return 12
    elif rank == 'King': return 13    
    else: return rank

def draw(deck):
    rank = random_rank(deck)
    suit = random_suit(deck)
    value = get_value(rank)
    return [rank, suit, value]

def predict_card() -> int:
    while True:  # Loop until valid input is given
            guess = input("Will the next card be higher(1) or lower(0)? ")  # Ensure input is converted to an integer
            
            if guess in ['1','0']:
                break # Exit loop
            else: # Loop again
                print("Enter 1 or 0.")
    return int(guess)

def compare_cards(v1, v2):
    if v1 < v2: return 1 # higher
    elif v1 >= v2: return 0 # lower


# Gameplay

score = 50

while True: # Allow user to play again
    for i in range(1,8): # Play 7 rounds per game
        print('\nRound', i)

        # Draw rank, suit, and value
        r, s, v = draw(deck)
        print(f'Current Card: {r} of {s}')

        # Guess the next card
        guess = predict_card()
        r2, s2, v2 = draw(deck)
        
        # Check your answer
        answer = compare_cards(v, v2)
        if answer == guess:
            print("Correct!")
            score+=20
        else:
            print("Wrong!")
            score-=15

        # Next round out of 7
        r, s, v = r2, s2, v2
        if i != 7:    
            print('\nYour Score:', score)
        else: 
            print('\nFinal Score:', score)
    
    # Prompt user to play again
    reset = input("Play again (y/n)? ").strip().lower()

    if 'n' in reset:
        break # exit loop
    else:
        score = 0

print('\nThanks for playing!\n')
