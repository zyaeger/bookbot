import sys

from stats import count_characters, count_words, sorted_char_counts


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    word_count = count_words(get_book_text(book_path))
    char_dict = count_characters(get_book_text(book_path))
    sorted_chars = sorted_char_counts(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for c_count in sorted_chars:
        if c_count["char"].isalpha():
            print(f"{c_count['char']}: {c_count['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
