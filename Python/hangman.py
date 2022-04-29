import random
import string
# from sets import set
import os
import mmap

title = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
"""

stages = ["",
"""


_______
""",
"""

|  
|   
|   
|   
|   
|
|_______
""",
"""
_____
|  
|   
|   
|   
|   
|
|_______
""",
"""
_____
|/  
|   
|   
|   
|   
|
|_______
""",
"""
_____
|/  |
|   
|   
|   
|   
|
|_______
""",
"""
_____
|/  |
|   O
|   
|   
|   
|
|_______
""",
"""
_____
|/  |
|   O
|   |
|   |
|   
|
|_______
""",
"""
_____
|/  |
|   O
|   |
|   |
|  / 
|
|_______
""",
"""
_____
|/  |
|   O
|   |
|   |
|  / \\
|
|_______
""",
"""
_____
|/  |
|   O
|  \|
|   |
|  / \\
|
|_______
""",
"""
_____
|/  |
|   O
|  \|/
|   |
|  / \\
|
|_______
"""
]

print(title)
# print(stages[6])
# for stage in stages:
#     print(stage)

# def read_file():
with open("../Dictionary.txt") as f:
    file = f.read()

# with open("Dictionary.txt", mode="r", encoding="utf8") as file_obj:
#     with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
#         text = mmap_obj.read()
#         print(text)

# file = text.split('\n')
file = file.split('\n')
# return file

# generates list of letters
def gen_word():
    word = file[random.randint(0, len(file))]
    return word

def start():
    word = gen_word().upper()
    # print(word)
    user_guesses = []
    user_word = []
    wrong_guesses = 0
    # not_guessed = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
    #                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
    #                "Y", "Z"]

    for i in range(len(word)):
        user_word.append("_")

    while wrong_guesses < 11 and ''.join(user_word) != word:
        print(stages[wrong_guesses])
        # print(f"Letters not guessed: {not_guessed}")
        print(f"Letters guessed: {user_guesses}")
        print(user_word)
        guess = input("Enter letter: ").upper()
        os.system('cls' if os.name == 'nt' else 'clear')
        if guess in user_guesses:
            print(f"You've already guessed {guess}!")
        else:
            user_guesses.append(guess)
            # print(word)
            # print(guess)
            if guess not in word:
                print(f"{guess} is not in the word!")
                wrong_guesses += 1
            else:
                for i in range(len(word)):
                    # print(word[i])
                    # print(guess)
                    if word[i] == guess:
                        # print("yes")
                        user_word[i] = guess
            # else:
            #     print(f"{guess} is not in the word!")
        #     wrong_guesses += 1


    print(stages[wrong_guesses])
    print(user_word)
    if wrong_guesses == 11:
        print(f"Unlucky, you lost!  The word was {word}")
    else:
        print("Congrats, you won!")

start()


