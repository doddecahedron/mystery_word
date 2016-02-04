import random

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
secret_word = random.choice(WORDS)

while True:
    start = input("Press enter to start, or Q to quit")
    if start.lower() == 'q':
        break

    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 8 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end="") # lets print print multiple times on the same line
            else:
                print('_', end="")
        print('Strikes: {}/8'.format(len(bad_guesses)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter.")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter.")
            continue
        elif not guess.isalpha():
            print("You can only guess letters.")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("WRONG! My secret word was {}".format(secret_word))

