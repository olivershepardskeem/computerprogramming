import random

def pick_random_word_from_sowpods(words):

    with open('sowpods.txt', 'r') as f:
        words = f.read(words).splitlines(words)

    random_word = random.choice(words)

    return random_word

