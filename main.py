def main(): # master list making sure all items are loaded
    toBook = "books/frankenstein.txt" # path to book
    text = get_book_text(toBook) # turn book words/string
    num_words = countWords(text) # count the strings
    count = countLetters(text) # dict character : # of times
    report = only_letters(count) # list letters only
    sorted = sorting(report,count) # making a list of dictionaries
    print(f"--- Begin report of {toBook} ---")
    print(f"{num_words} words found in the docutment")
    print("")
    def sort_on(dict):
        return dict["num"]
    sorted.sort(reverse=True, key=sort_on)
    for each in sorted:
        print(f"The '{each['Letter']}' character was found {each['num']} times")




    
            


def countWords(text): # to count the words
    words = text.split() # split the book into words
    return len(words) # length of book converted to list items

def get_book_text(toBook): # to pull the book into here
    with open(toBook) as f: # to make opening the book f
        return f.read() # to read f

def countLetters(text): #pull book becomes count
    counting = {}
    for letters in text: # break book to letters
        lowered = letters.lower()
        if lowered in counting:
            counting[lowered] += 1
        else:
            counting[lowered] = 1
    return counting

def only_letters(count): # becomes report
    is_letter = []
    isnot_letter = []
    for each_in_list in count:
        if each_in_list.isalpha() == True:
            is_letter.append(each_in_list)
        else:
            isnot_letter.append(each_in_list)
    return is_letter
    
def sorting(report,count): # becomes sorted (Need to assign letter and number both to key pair)
    fin_ito = {}
    list_of_dicts = []
    for i in range(len(report)):
        if report[i] in count:
            fin_ito['Letter'] = report[i]
            fin_ito.update({"num": count[report[i]]})
            list_of_dicts.append(fin_ito)
            fin_ito = {}
    return list_of_dicts

def sort_on(sorted):
    return sorted["num"]






    






main()    