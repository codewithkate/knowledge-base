# Title: HigherOrLower 

import random

# Card constants
SUIT_TUPLE = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
RANK_TUPLE = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def get_card(deck_list_in):
    this_card = deck_list_in.pop() # pop a card off the top of the deck (the end of the list)
    return this_card

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deck_list_in):
    deck_list_out = deck_list_in.copy() # make a copy of the deck
    random.shuffle(deck_list_out) # reorder the list
    return deck_list_out

# Main code
print("""
Welcome to Higher or Lower!
Pick a card and place your bet on if the next draw will be higher or lower in value.
\nGet it right: +20pts
Get it wrong: -15pts
\nYou have 50 points to start.
""")
print('-'*15)

# Step 1
starting_deck_list = []
for suit in SUIT_TUPLE:
    for value, rank in enumerate(RANK_TUPLE):
        card_dict = {'rank':rank, 'suit':suit, 'value':value}
        starting_deck_list.append(card_dict)

score = 50

while True: # play multiple games
    print()
    game_deck_list = shuffle(starting_deck_list)
    # Step 2
    current_card_dict = get_card(game_deck_list)
    current_card_suit = current_card_dict['suit']
    current_card_rank = current_card_dict['rank']
    current_card_value = current_card_dict['value']
    print(f'Starting card is: {current_card_rank} of {current_card_suit}')
    print()

    # Step 3
    for n in range(1, NCARDS): # play one game of this many cards
        print('Round', n)
        guess = input('Will the next card be higher or lower? (enter h or l): ')
        guess = guess.casefold() # force lowercase
    
        # Step 4
        next_card_dict = get_card(game_deck_list)
        next_card_suit = next_card_dict['suit']
        next_card_rank = next_card_dict['rank']
        next_card_value = next_card_dict['value']
        print(f'Next card is: {next_card_rank} of {next_card_suit}')

        # Step 5
        if next_card_value > current_card_value:
            answer = 'h'
        elif next_card_value < current_card_value:
            answer = 'l'
        
        if guess == answer:
            score+=20
            print('Correct!')
        else:
            score=-15
            print("Sorry, you're wrong")

        if n != NCARDS-1:
            print('\nYour Score:', score)
        else:
            print('\nFinal Score:', score)
        print()

    
    # Prompt user to play again
    go_again = input('To play again, press ENTER, or "q" to quit: ')
    if 'q' in go_again:
        break # exit loop

print('\nThanks for playing!\n')
