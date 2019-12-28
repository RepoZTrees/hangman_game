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

#either use string or .join
def hide_word(sw,guesses):
    guessed = []
    for secret_letter in sw:
        if secret_letter in guesses:
            guessed.append(guesses)
            return guessed

def hide_word(sw, guesses):
    guessed = []

    for secret_letter in sw:
        if secret_letter in guesses:
            guessed.append(secret_letter)
        else:
            guessed.append('_')
    guessed_str = ''.join(guessed) 
    return guessed_str

"""
def first_correct_(secret_word, guesses):
    guess = []
    for sw in secret_word:
        if sw in guesses:
            guess.append(sw)
        return "_l______"

def second_correct_guess(secret_word, guesses):
    guess = []
    for sw in secret_word:
        if sw in guesses:
            guess.append(sw)
        return "ele_____"

def third_correct_guess(secret_word, guesses):
    guess = []
    for sw in secret_word:
        if sw in guesses:
            guess.append(sw)
        return "elep____"
    
 """ 
    
#     word = "elephant"
#     hw = []
#     gl = []
#     for sl in word:
#         if gl in sl:
#             hw.append()
#         else:
            
            
#     return hw
#secret_word = "elephant"
#def hide_word(secret):
    

    
    
