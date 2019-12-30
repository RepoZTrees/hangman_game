from hangman import get_secret_word
from hangman import hide_word
#from hangman import test_secret_word_atleast_five

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
