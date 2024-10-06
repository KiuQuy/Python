# return longest word of text
def longest_word(text):
    word        = text.split()
    _len        = len(word[0])
    _longest    = word[0]

    for each_word in word:
        if _len < len(each_word):
            _len        = len(each_word)
            _longest    = each_word
    return _longest