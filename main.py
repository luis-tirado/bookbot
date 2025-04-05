import sys
from stats import *

def main():
    # hard coded book path for testing: book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        book_path = sys.argv[1]  # get the book path from command line argument
        text_file = read_file(book_path)            # text file converted to a string
    except FileNotFoundError:
        print(f"File not found: {book_path}")
        sys.exit(1)
    except OSError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # call functions from stats.py to count  words and characters
    number_of_words = count_words(text_file)
    char_dict = count_characters(text_file)           # characters dictionary
    char_sorted_list = dict_to_sorted_list(char_dict)

    # print the number of words and the characters in the text file
    print(f"--- Begin report of book ---")
    print(f"{number_of_words} words found in the document")
    print()
    
    for ch in char_sorted_list:
        print(f"{ch['character']}: {ch['num']}")

    print("--- End report ---")


# simple function to read the book file
def read_file(book_path):
    with open(book_path) as book:
        return book.read()

# returns a list a withh sorted characters in increasing order
def dict_to_sorted_list(char_dict):
    sorted_words_list = []
    for character in char_dict:
        if character.isalpha():
            sorted_words_list.append({"character": character, "num": char_dict[character]})
    sorted_words_list.sort(reverse=True, key=sort_on)
    return sorted_words_list
# helper function to sort the list of characters
def sort_on(dict):
    return dict["num"]

main()