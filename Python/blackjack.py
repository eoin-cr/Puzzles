import random
import os

# notes about this version:
# most of the basic logic is working, however, functions such as an ace being
# either 1 or 11 is missing.  There is also no split or double down function.
# Also there is no option to play where you don't see the dealer's cards
# until you stand.  I would also like to add some sort of money counter
# and betting system, and maybe even the option to set how many decks are used
# so it becomes possible to try counting cards.


suits = ["♧", "♤", "♢", "♡"]
suit_names = ["clubs", "spades", "diamonds", "hearts"]


def pick_cards():
    output = [random.randint(1, 13), random.randint(0, 3)]

    return output


# def string_merger(a, b, whitespace):
def string_merger(array, whitespace):
    output = ""
    # a = a.split("\n")
    # b = b.split("\n")
    for i in range(len(array)):
        array[i] = array[i].split("\n")

    for i in range(len(array[0])):
        for j in range(len(array) - 1): output += array[j][i] + f"{'' * whitespace}"
        output += array[-1][i] + "\n"
        # output += array[0][i] + f"{''*whitespace}" + array[1][i] + "\n"

    return output


def print_cards(cards):
    # print("HI")
    card_list = []
    # arr = []
    # print(cards)
    # print(len(cards))
    # print(int(len(cards)/2))
    for i in range(int(len(cards) / 2)):
        # print("hi")
        card = to_char(cards[i * 2])
        # print(f"""
        card_list.append(f"""
        _________
        |{card:<6} |
        |       |
        |   {suits[cards[i * 2 + 1]]}   |
        |       |
        | {card:>6}|
        _________
      {card} of {suit_names[cards[i * 2 + 1]]:<8}""")
        # string += string

    # card_list = [x for x in card_list]
    print(string_merger(card_list, 3))
    total_score = 0
    for i in range(int(len(cards) / 2)): total_score += to_val(cards[i * 2])
    print(f"Total score: {total_score}")
    print("")


def to_char(card):
    match card:
        case 11:
            return "J"
        case 12:
            return "Q"
        case 13:
            return "K"
        case 1:
            return "A"
        case _:
            return card


def to_val(card):
    return 10 if card > 10 else card


def game(selection):
    comp_cards = pick_cards() + pick_cards()
    # user_cards = pick_cards() + pick_cards()
    user_cards = pick_cards()
    # user_score = to_val(user_cards[0]) + to_val(user_cards[2])
    user_score = to_val(user_cards[0])
    comp_score = to_val(comp_cards[0]) + to_val(comp_cards[2])

    if selection == 1:
        # user
        choice = "H"
        while choice != "S":
            user_cards += pick_cards()
            user_score += to_val(user_cards[-2])
            os.system('cls' if os.name == 'nt' else 'clear')  # clears terminal
            print("Dealer's cards:", end="")
            print_cards(comp_cards)
            print("Your cards:", end="")
            print_cards(user_cards)
            if (user_cards[0] == 1 and to_val(user_cards[2]) == 10 or
                    to_val(user_cards[0]) == 10 and user_cards[0] == 1):
                print("Blackjack!  You win!")
                exit(0)
            elif user_score > 21:
                print("You're bust!  You lose.")
                exit(0)

            choice = input("Enter H to hit (get another card) or S to stand ("
                           "stick with the cards you have)").upper()
            while choice != "H" and choice != "S":
                choice = input("Invalid input.  Enter H to hit or S to stand")

        if user_score > 21:
            print("You're bust!  You lose.")
            exit(0)

        while comp_score < 17:
            comp_cards += pick_cards()
            comp_score += to_val(comp_cards[-2])
            os.system('cls' if os.name == 'nt' else 'clear')  # clears terminal
            print("Dealer's cards:", end="")
            print_cards(comp_cards)
            print("Your cards:", end="")
            print_cards(user_cards)

        # print(user_score)
        # print()
        if user_score > comp_score or comp_score > 21:
            print("You win!")
        elif user_score == comp_score:
            print("It's a draw!")
        else:
            print("The computer wins!")


game(1)
