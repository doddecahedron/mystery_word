secret_word = "bathroom" ## change this string to a list so that it's mutable
counter = 0

empty_word = (list("_" * len(secret_word)))

while True:
    print(empty_word)
    guess= input("What letter would you like to guess? ").lower()
    for character in 'bathroom':
        if character == guess:
            empty_word[counter] = guess
        counter += 1
    counter = 0

print(empty_word)

