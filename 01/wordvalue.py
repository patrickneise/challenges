from data import DICTIONARY, LETTER_SCORES

def load_words():

    """Load dictionary into a list and return list"""
    with open (DICTIONARY) as words:
        lines = words.read().splitlines()

    return lines

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    try:
        points = [LETTER_SCORES[letter] for letter in word.upper()]
    except KeyError:
        points = []
    
    return sum(points)
    

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    
    word_scores = [calc_word_value(word) for word in words]

    max_score = max(word_scores)
    max_word = words[word_scores.index(max_score)]

    return max_word


if __name__ == "__main__":
    pass # run unittests to validate
