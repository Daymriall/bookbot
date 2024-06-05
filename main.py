def main(): # master list making sure all items are loaded
    toBook = "books/frankenstein.txt" # path to book
    text = get_book_text(toBook) # turn book words/string
    num_words = countWords(text) # count the strings
    count = countLetters(text)

    print(f"{num_words} words found in the docutment")
    print(count) # letters and how many times

def countWords(text): # to count the words
    words = text.split() # split the book into words
    return len(words) # length of book converted to list items

def get_book_text(toBook): # to pull the book into here
    with open(toBook) as f: # to make opening the book f
        return f.read() # to read f

def countLetters(text): #pull book
    counting = {}
    for letters in text: # break book to letters
        lowered = letters.lower()
        if lowered in counting:
            counting[lowered] += 1
        else:
            counting[lowered] = 1
    return counting
        
        


    













main()    