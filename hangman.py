import random

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def pick_random_word_from_sowpods():
    with open('sowpods.txt', 'r') as f:
        words = f.read().splitlines()
    random_word = random.choice(words)
    return random_word

def uranium():
    word_to_guess = pick_random_word_from_sowpods()

    guessed_letters = []
    max_attempts = 10
    attempts = 0

    print("you are about to play goofy goober hang man!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts < max_attempts:
        guess = input("Pick a letta: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letta.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letta!")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"wrong! You have {max_attempts - attempts} guesses remaining.")
            if attempts == max_attempts:
                print(f"You have used all your guesses you goofy goober The answer was: {word_to_guess}")
        else:
            print("Correct!")

        word_display = display_word(word_to_guess, guessed_letters)
        print(word_display)

        if "_" not in word_display:
            print("You win, you are not a goofy goober!")
            break

uranium()