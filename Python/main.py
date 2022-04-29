import random
import string
# from sets import set
import os
import mmap


# def read_file():
with open("../Dictionary.txt") as f:
    file = f.read()

file = file.split('\n')

# with open("Dictionary.txt", mode="r", encoding="utf8") as file_obj:
#     with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
#         text = mmap_obj.read()
#         print(text)
#
# file = text.split(b'\n')
# return file


# generates list of letters
def gen_letters():
    # print("Generating letters")
    letter_list = []
    while len(letter_list) < 7:
        letter = random.choice(string.ascii_letters).upper()
        if letter not in letter_list:
            letter_list.append(letter)

    # print(f"Letters: {letter_list}")
    return letter_list
    # for element in letter_list:
    #     print(element)


# tests if there are enough possible solutions for the letters to be good
# (atm letters will only be used if there's more than 15 possible solutions
def test_letters():
    # print("Testing letters!")
    good_letters = False
    output_list = []

    while not good_letters:
        valid_words = []
        letters = gen_letters()
        # letters = ["A","B", "C","D","E","F","G","H","I","J","K","L","M",
        #            "N", "O", "P", "Q", "R", "S", "T"]
        allowed_chars = set(''.join(letters))
        for word in file:
            word = word.upper()
            # print(f"word: {word}")
            # print(f"letters 0: {letters[0]}")
            # print(f"allowed chars: {allowed_chars}")
            # print(f"subset?: {set(word).issubset(allowed_chars)}")
            if letters[0] in word and set(word).issubset(allowed_chars):
                valid_words.append(word)

        # print(f"valid_words: {valid_words}")
        if len(valid_words) > 15:
            good_letters = True
            output_list.append(valid_words)
            output_list.append(letters)

    return output_list


def start():
    out = test_letters()
    valid_words = out[0]
    valid_letters = out[1]
    prev_words = []
    word = None

    while len(prev_words) < len(valid_words) and word != "!STOP":
        # print(word)
        print("Previous words:")
        for element in prev_words:
            print(element)
        print(f"The main letter is: {valid_letters[0]} \nThe other letters are:"
              f" {valid_letters[1:]}")
        word = input("Enter word (or enter !stop to stop): ")
        word = word.upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        if word in valid_words and word not in prev_words:
            prev_words.append(word)
            print("Correct!")

        elif word == "!STOP":
            print("Game stopped.  All the possible solutions were:")
            for word in valid_words:
                print(word)

            print(f"You got {len(prev_words)}/{len(valid_words)} words")
            exit()

        elif word in prev_words:
            print("You've already guessed that!")

        elif valid_letters[0] not in word:
            print(f"The letter {valid_letters[0]} must be in your answer!")

        else:
            string = ""
            for letter in word:
                if letter not in valid_letters:
                    string += letter

            if string == "":
                print("Invalid word!  That word is not in our dictionary")
            else:
                print(f"Invalid word!  The letters {string} are not allowed letters!")
            # print("")

start()
