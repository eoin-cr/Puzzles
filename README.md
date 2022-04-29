A selection of Free and Open Source Software puzzles.  At the moment they're
all command line based.  The puzzles will initially be written in Python
but I'll be rewriting them in C and maybe Rust as well for efficiency.

# Puzzles

## Doesn't have a proper name yet

I haven't come up with a name for `main.py` yet.  You are given a list
of letters and you must come up with all the words containing those
letters alone.  You are allowed to use the same letter multiple times,
or not at all.  However, you *must* use the main letter in every guess.
You can enter `!stop` when you give up.  This will display all the
possible words you could have guessed.

## Hangman

Just a terminal variation of the classic hangman game.  The computer
thinks of a word and you have to guess what it is by entering a letter
at a time. If your letter is in the word you will be able to see 
where it was in word the computer thought of.


# Installing

After installing python3 (if on windows you may have to add it to your
PATH), simply use `git clone https://github.com/eoin-cr/Puzzles/` to
download the puzzles.  Then do `cd Python` to go to the python puzzles.
Then simply do `python3 [puzzlename].py` to play :)


The English dictionary is available 
[here](https://github.com/sujithps/Dictionary)

And wiki100k is available [here](https://gist.github.com/h3xx/1976236)
