# First import the logo from art.py using the from/import syntax
from art import logo
# Next, we will import the rest of the modules that will be used in this project
import os
import random

# There is not a command in VSCode to clear the console when we want, so this is a work-around
# Using the os module we imported above, we will create the following function
def clear():
    '''Clears the console across operating systems'''
    command = 'clear'
    # If statement to check and see what OS the computer is running. The 'clear' command in windows is 'cls' so if the computer is running windows, it changes the command so it works
    if os.name == ('nt', 'dos'):
        command = 'cls'
        # Inputs the command variable into the system function from the os module. This executes the command in the console/terminal
    os.system(command)



# Function to pull a card or deal from the deck at random
def deal_card():
    '''Returns a random card from the deck'''
    # Create a card list for each card, Ace through King.
    # All Royalty cards are 10
    # Ace will be 11. Rules state it can also be 1
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Use the random module with the choice method passing in the card list and set it to a variable
    card = random.choice(cards)
    return card


# Function to score our cards that are pulled from the deck
def calculate_score(cards):
    '''Take a list of cards and returns the score calculated from the cards'''
    # Create an if statement to check and see if the player has a blackjack hand (2 cards, an ace and a 10)
    if sum(cards) == 21 and len(cards) == 2:
        # Return 0 to represent our blackjack hand. We will use this instead of 21 to differentiate it from the normal score of 21
        return 0
    # Create an if statement that says if 11 is in the cards and the sum is more than 21, change 11 to one so as not to bust
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create a function that compares the score and returns an outcome
def compare(user_score, com_score):
    '''Pass in both the users score and the computers score as arguments'''
    # if/elif/else statements for each outcome
    if user_score == com_score:
        print(f'Your Score: {user_score}')
        return 'Draw'
    elif com_score == 0:
        return 'You Lose! COM has BlackJack!'
    elif user_score == 0:
        return 'Congratulations! You have BlackJack!'
    elif user_score > 21:
        return 'You Busted! COM Wins!'
    elif com_score > 21:
        return 'COM Busted! You Win!'
    elif user_score > com_score:
        return 'Congratulations! You win!'
    else:
        return 'Sorry, You Lose!'
    


# Create game function
def play_game():
    '''This function will be run so the game begins'''
    print(logo)
    
    # Create empty lists for computers and users cards. This is where the cards drawn by each player will be stored and how each of the above functions will make their calculations
    user_cards = []
    com_cards = []
    # Create a variable to notate whether game should continue and use a boolean value of false
    is_game_over = False
    # BlackJack starts with 2 cards being dealt, so we need to start the game with 2 cards being added to the user_cards and the com_cards list
    # Use a for loop using the built in range() function to loop only twice
    for _ in range(2):
        # Use the append method with each empty list and pass in our deal_card function
        user_cards.append(deal_card())
        com_cards.append(deal_card())
    while not is_game_over:
        # Using the calulate_score function, create two new variables to store the scores by passing in our lists as arguments
        user_score = calculate_score(user_cards)
        com_score = calculate_score(com_cards)

        # Using print statements and f strings, have the current score of the user and the first card of the computers hand display
        print(f'Your cards: {user_cards}, Current Score: {user_score}\n')
        print(f'Computers first card: {com_cards[0]}\n')

        # Create an if/else statement that states if either player has a blackjack hand or the user goes over 21 the game ends
        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True # Ends the game loop
        else:
            # Create an input stored to a variable tht asks the user to 'hit' or 'stand'
            user_should_deal = input('Type `Y` to get another card (hit). Type `N` to stand: ').lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    # Create a while loop outside of our main game loop that keeps the computer playing as long as its score is not equal to 0 and under 17
    while com_score != 0 and com_score < 17:
        # Within this while loop, we will have a card dealt to the computer and score updated and stored to the com_score variable
        com_cards.append(deal_card())
        com_score = calculate_score(com_cards)
    # Have print statementsand f-strings that print out the final user_score and com_score
    print(f'\nYour final hand: {user_cards}, your final score: {user_score}')
    print(f'Computer final hand: {com_cards}, computer final score: {com_score}\n')
    print(compare(user_score, com_score))


# One final while loop that takes the users input to start or leave the program, this also will be the first thing that will show when the program is run
while input('Want to play BlackJack? Type `Y` to start, or `Enter` to quit.'):
    clear()
    play_game()