def num_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    words = (text.lower().split())
    letter_count = {}
    for word in words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count