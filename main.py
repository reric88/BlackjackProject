from art import logo
import os
import random


def clear():
    '''Clears the console across operating systems'''
    command = 'clear'
    if os.name == ('nt'):
        command = 'cls'
    os.system(command)


def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Take a list of cards and returns the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, com_score):
    '''Pass in both the users score and the computers score as arguments'''
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


def play_game():
    '''This function will be run so the game begins'''
    print(logo)
    user_cards = []
    com_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        com_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        com_score = calculate_score(com_cards)
        print(f'Your cards: {user_cards}, Current Score: {user_score}\n')
        print(f'Computers first card: {com_cards[0]}\n')
        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True # Ends the game loop
        else:
            user_should_deal = input('Type `Y` to get another card (hit). Type `N` to stand: ').lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while com_score != 0 and com_score < 17:
        com_cards.append(deal_card())
        com_score = calculate_score(com_cards)
    print(f'\nYour final hand: {user_cards}, your final score: {user_score}')
    print(f'Computer final hand: {com_cards}, computer final score: {com_score}\n')
    print(compare(user_score, com_score))

while input('\nWant to play BlackJack? Type `Y` to start, or `Enter` to quit.'):
    clear()
    play_game()