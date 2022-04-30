import random

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
        for j in range(len(array)-1): output += array[j][i] + f"{''*whitespace}"
        output += array[-1][i] + "\n"
        # output += array[0][i] + f"{''*whitespace}" + array[1][i] + "\n"

    return output


def print_cards(cards):
    # print("HI")
    card_list = []
    arr = []
    for i in range(int(len(cards) / 2)):
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
      {card} of {suit_names[cards[i*2+1]]:<8}""")
        # string += string

    print(string_merger([card_list[0], card_list[1]], 3))


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
    user_cards = pick_cards() + pick_cards()
    user_score = to_val(user_cards[0]) + to_val(user_cards[2])
    comp_score = to_val(comp_cards[0]) + to_val(comp_cards[2])

    if selection == 1:
        print("Dealer's cards:", end="")
        print_cards(comp_cards)
        print("Your cards:", end="")
        print_cards(user_cards)


game(1)
