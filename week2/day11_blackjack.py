import random
"""
Blackjack values
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card():
    return random.choice(cards)


def player_total_cards(player_cards):
    total = 0
    for t in player_cards:
        total += t
    return total


def dealer_total_cards(dealer_cards):
    total = 0
    for t in dealer_cards:
        total += t
    return total


def game():

    players_turn = True
    dealer_turn = True
    player_cards = []
    dealer_cards = []

    player_cards.append(get_card())
    player_cards.append(get_card())
    dealer_cards.append(get_card())

    print(
        f"Dealers cards: {dealer_cards} = {(dealer_total_cards(dealer_cards))}")
    print(
        f"Your cards are: {player_cards} = {(player_total_cards(player_cards))}")

    while players_turn and dealer_turn:
        while players_turn:
            if (player_total_cards(player_cards) < 22):
                cont = input("Would you like another card?")
                if cont == "Y":
                    player_cards.append(get_card())
                    print(player_total_cards(player_cards))
                    print(f"Your total: {player_total_cards(player_cards)}")
                else:
                    print(player_total_cards(player_cards))
                    print(f"Your total: {player_total_cards(player_cards)}")
                    players_turn = False
            else:
                print(f"YOU ARE OVER! {player_total_cards(player_cards)}")
                player_cards = []
                players_turn = False
                dealer_turn = False

        while dealer_turn:
            if dealer_total_cards(dealer_cards) < 17:
                print(f"Dealer has : {dealer_total_cards(dealer_cards)}")
                dealer_cards.append(get_card())
            elif dealer_total_cards(dealer_cards) < 22:
                print(f"Dealer has : {dealer_total_cards(dealer_cards)}")

                dealer_turn = False
            else:
                print(f"Dealer has : {dealer_total_cards(dealer_cards)}")
                print("Dealer bust! You win!")
                dealer_turn = False
                dealer_cards = []

    else:
        if dealer_total_cards(dealer_cards) > player_total_cards(player_cards):
            print("dealer wins")
        elif player_total_cards(player_cards) > dealer_total_cards(dealer_cards):
            print("Player wins")
        else:
            print("Draw")


game()
