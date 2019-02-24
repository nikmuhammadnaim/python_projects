# Import relevant libraries
from random import shuffle

# Create deck
shapes = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
values = [i for i in range(2, 11)]
special = ['Ace', "King", "Queen", "Jack"]

deck = [str(i) + " of " + shape for i in values + special for shape in shapes]
six_deck = deck * 6

# TODO: Allow for more than one player
# Create dealer and player(s)
p1_wallet = 100

# Ask player to place bet
place_bet = True

while place_bet:
    try:
        p1_bet = int(input(f'=== Your current wallet balance is ${p1_wallet}' +
            ' ===\nHow much money would you like to place your bet? '))

        if p1_bet > p1_wallet:
            print(f"You do not have enough money in your wallet." +
                ' Please try again.')
            print()
        else:
            place_bet = False
    except Exception as e:
        print("--> Please enter a valid input.")
        print()

# TODO: Randomly select a player to cut the deck
# Shuffle and ask player
shuffle(six_deck)
deck_cut = int(input('Player 1 will cut the deck.' +
                'Player 1 please enter a random number between 50 - 75'))
playing_deck = six_deck[:-deck_cut]

# Hands
dealer = []
p1 = []

for i in range(2):
    p1.append(playing_deck.pop())
    dealer.append(playing_deck.pop())
    
