import random
#import string

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

#***
def get_status_message(sw, correct_guesses, wrong_guesses, turns_left):
    masked_word = hide_word(sw, correct_guesses+wrong_guesses)
    guesses = "".join(correct_guesses + wrong_guesses)
    status_message = """{}
Guesses:{}
Turns left:{}
""".format(masked_word, guesses, turns_left)
    return status_message

#***
cg = []
wg = []
def play(sw, cg, wg, new_guess, turns_left):
    if new_guess in cg+wg:
        return (cg, wg, turns_left, False, "")
    if new_guess in sw:
        cg.append(new_guess)
    else:
        turns_left -= 1
        wg.append(new_guess)

    if turns_left == 0:
        return (cg, wg, 0, True, "You lost! The word was '{}'.".format(sw))

    guessed = "_" not in hide_word(sw, cg+wg)
    if guessed:
        return (cg, wg, turns_left, True, "You win!")
    return (cg, wg, turns_left, False, "")

#***
def main():
    secret_word = get_secret_word()
    print(secret_word)
    game_over = False
    correct = []
    wrong = []
    turns_left = 7
    while not game_over:
        status = get_status_message(secret_word, correct, wrong, turns_left)

        print(status)
        ip = input ("Enter a letter> ")
        
        correct, wrong, turns_left, game_over, message = play(secret_word, correct, wrong, ip, turns_left)
    print(message)

if __name__ == "__main__":
    main()
