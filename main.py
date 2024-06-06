def main(): # master list making sure all items are loaded
    toBook = "books/frankenstein.txt" # path to book
    text = get_book_text(toBook) # turn book words/string
    num_words = countWords(text) # count the strings
    count = countLetters(text) # dict character : # of times
    report = only_letters(count) # list letters only
    sorted = sorting(report,count)
    organized = organize(sorted)
    print(f"--- Begin report of{toBook} ---")
    print(f"{num_words} words found in the docutment")
    print(organized)

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

def only_letters(count):
    is_letter = []
    isnot_letter = []
    for each_in_list in count:
        if each_in_list.isalpha() == True:
            is_letter.append(each_in_list)
        else:
            isnot_letter.append(each_in_list)
    return is_letter
    
def sorting(report,count):
    fin_ito = {}
    list_of_dicts = []
    for i in range(len(report)):
        if report[i] in count:
            fin_ito[report[i]] = count[report[i]]
            list_of_dicts.append(fin_ito)
            fin_ito = {}
    return list_of_dicts

def organize(sorted):
    return sorted[0]
sorted.sort(reverse=True,key=organize)
print(sorted)



    






main()    