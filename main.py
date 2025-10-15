import sys
from stats import word_count
from stats import char_count
from stats import sorted_chars

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]

    text = get_book_text(path)
    num_words = word_count(text)
    sorted_list = sorted_chars(char_count(text))
   
    # Output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")

main()
