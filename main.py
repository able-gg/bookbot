import sys
from stats import count_words, count_characters, sort_char_counts

def get_book_text(books):
    with open(books, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        char = item["char"]
        # Only print single alphabetic characters
        if char.isalpha() and len(char) == 1:
            print(f"{char}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

