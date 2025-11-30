from stats import num_words, character_count
import sys

print("Usage: python3 main.py <path_to_book>")

if len(sys.argv) < 2:
    sys.exit(1)

PATH = sys.argv[1]

def main():
    full_book = get_book_text(PATH)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}")
    print("----------- Word Count -----------")
    print(f"Found {num_words(full_book)} total words")
    print("--------- Character Count -------")
    sorted_by_values = dict(sorted(character_count(full_book).items(), key=lambda items: items[1], reverse=True))
    for value in sorted_by_values:
        if value.isalpha():
            print(f"{value}: {sorted_by_values[value]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()