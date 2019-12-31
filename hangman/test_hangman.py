import hangman
#from hangman import get_secret_word
#from hangman import hide_word
#from hangman import get_status_message
#from hangman import test_secret_word_atleast_five

from hangman import get_secret_word, hide_word, get_status_message

#You can either say 'from file_name import function_name' or call as 'filename.function_name inside the function' 
#to check the coverage: (venv) vik@vik-VirtualBox:~/lycaeum/tdd/hangman$ pytest -v --cov=hangman test_hangman.py



def test_secret_word_no_punctuation():
    with open ("/tmp/words.txt","w") as f:
        for i in ["word'one", "word_two", "wordthree"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wordthree"

def test_hide_word_empty():
    sw = "elephant"
    assert hide_word(sw,[]) == "________"

def test_hide_word_first_guess():
    sw = "elephant"
    assert hide_word(sw, ['l']) == "_l______"

def test_hide_word_second_guess():
    sw = "elephant"
    assert hide_word(sw,['e','l']) == "ele_____"

def test_hide_word_third_guess():
    sw = "elephant"
    assert hide_word(sw,['e','l','p']) == "elep____"

def test_hide_fourth_guess():
    sw = "elephant"
    assert hide_word(sw,['e','l','p','h']) == "eleph___"

def test_hide_fifth_guess():
    sw = "elephant"
    assert hide_word(sw,['e','l','p','h','a']) == "elepha__"

def test_hide_sixth_guess():
    sw = "elephant"
    assert hide_word(sw,['e','l','p','h','a','n']) == "elephan_"

def test_hide_seventh_guess():
    sw = "elephant"
    assert hide_word(sw,['e','l','p','h','a','n','t']) == "elephant"
    
def test_secret_word_atleast_five():
    with open("/tmp/words.txt","w") as f:
        for i in ["wo", "wor", "word", "bigword"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "bigword"
    
def test_secret_word_lowercase():
    with open("/tmp/words.txt","w") as f:
        for i in ["Wording","wOrding","WORDING","wording"]:
            f.write(i+"\n")
    selected_word = get_secret_word('/tmp/words.txt')
    assert selected_word == "wording"

def test_secret_word_no_repeat():
    with open("/tmp/words.txt","w") as f:
        for i in ["disaster","recall","advise","national","infrastructure","shots","fired","federation","duress"]:
            f.write(i+"\n")
    l = []
    for i in range(3):
        l.append(get_secret_word('/tmp/words.txt'))
    assert len(set(l)) == 3

#***

def test_status_message():
    status = hangman.get_status_message(sw = 'elephant',
                                        correct_guesses = ['e','l'],
                                        wrong_guesses = ['x'],
                                        turns_left = 4)
    assert status == """ele_____
Guesses:elx
Turns left:4
"""

#***

def test_play_correct_input_normal_turn():
    #cg = ['e']
    #wg = ['x']
    cg, wg, turns_left, game_over, final_message = hangman.play(sw = 'elephant',
                                                                cg = ['e'],
                                                                wg = ['x'],
                                                                new_guess = 'l',
                                                                turns_left = 4)
    assert cg == ['e', 'l']
    assert wg == ['x']
    assert turns_left == 4
    assert game_over == False

    
def test_play_correct_input_win_turn():
    #cg = ['d']
    #wg = ['x']
    cg, wg, turns_left, game_over, final_message = hangman.play(sw = 'dog',
                                                                cg = ['d', 'o'],
                                                                wg = ['x'],
                                                                new_guess = 'g',
                                                                turns_left = 4)
    assert cg == ['d', 'o', 'g']
    assert wg == ['x']
    assert turns_left == 4
    assert game_over == True
    assert final_message == "You win!"


def test_play_wrong_input_normal_turn():

    cg, wg, turns_left, game_over, final_message = hangman.play(sw = 'dog',
                                                                cg = ['d', 'o'],
                                                                wg = ['x', 'l'],
                                                                new_guess = 'l',
                                                                turns_left = 3)
    assert cg == ['d', 'o']
    assert wg == ['x', 'l']
    assert turns_left == 3
    assert game_over == False

def test_play_wrong_input_lose():
    cg, wg, turns_left, game_over, final_message = hangman.play(sw = 'dog',
                                                                cg = ['d', 'o'],
                                                                wg = ['x','l','z','p'],
                                                                new_guess = 'a',
                                                                turns_left = 1)
    assert cg == ['d', 'o']
    assert wg == ['x','l','z','p','a']
    assert turns_left == 0
    assert game_over == True
    assert final_message == "You lost! The word was 'dog'."


def test_play_repeat_input_correct():
    cg, wg, turns_left, game_over, final_message = hangman.play(sw = 'dog',
                                                                cg = ['d','o'],
                                                                wg = ['x'],
                                                                new_guess = 'd',
                                                                turns_left = 1)
    assert cg == ['d', 'o']
    assert wg == ['x']
    assert turns_left == 1
    assert game_over == False


def test_play_repeat_input_wrong():    

    cg, wg, turns_left, game_over, final_message = hangman.play(sw = 'dog',
                                                                cg = ['d','o'],
                                                                wg = ['x'],
                                                                new_guess = 'x',
                                                                turns_left = 1)
    assert cg == ['d', 'o']
    assert wg == ['x']
    assert turns_left == 1
    assert game_over == False

    
#***    



#pytest -k mask_word test_hangman.py (-k will tell pytest which #test to run)
