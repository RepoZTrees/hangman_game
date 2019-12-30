import random

def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)

    word = random.choice(good_words)
    return word.lower()

def hide_word(sw, guesses):
    
    guessed = []

    for secret_letter in sw:
        if secret_letter in guesses:
            guessed.append(secret_letter)
        else:
            guessed.append('_')
    guessed_str = ''.join(guessed) 
    return guessed_str
