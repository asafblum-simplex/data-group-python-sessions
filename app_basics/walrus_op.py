
words = ['falcon', 'sky', 'ab', 'water', 'a', 'forest']

def validate_word_length():
    for word in words:
        if ((n := len(word)) < 3):
            return f'bigger {word} -- All ok'
        else:
            return f"always print {word} -- nnot ok"

print("is n defined", n) # False