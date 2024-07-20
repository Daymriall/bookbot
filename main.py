def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    sorted = sorting(character_count)
    report = reporting(sorted, book_path, num_words) 


def sort_on(dict):
    return dict["count"]


def reporting(sorted, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} in this book")
    print("")
    for i in range(len(sorted)):
        print(f"The '{sorted[i]['letter']}' character was found {sorted[i]['count']} times")
    print("--- End report ---")


def sorting(character_count):
    sorted_characters = []
    for letter in character_count:
            sorted_characters.append({"letter": letter, "count": character_count[letter]})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters


def count_characters(text):
    character_count = {}
    for letters in text:
        letter = letters.lower()
        if letter in character_count and letter.isalpha():
            character_count[letter] += 1
        else:
            if letter.isalpha():
                character_count[letter] = 1
    return character_count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()