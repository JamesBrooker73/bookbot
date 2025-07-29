from stats import get_word_count
from stats import count_characters
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def format_text(num_words, sorted_chars, path):
    header = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {path}..\n"
        "----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        "--------- Character Count -------\n"
    )

    body = ""
    for char in sorted_chars:
        if char["char"].isalpha():
            body += (f"{char["char"]}: {char["num"]}\n")

    footer = ("============= END ===============")


    return header + body + footer

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    counted_chars = count_characters(book_text.lower())
    sorted_chars = sort_dictionary(counted_chars)
    print(format_text(num_words, sorted_chars,sys.argv[1]))
    #print(f"{num_words} words found in the document")
    #print(counter_chars)

main()
