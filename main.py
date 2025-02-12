import json

def main():
    book_path = "books/frankenstein.txt"
    text_file = read_file(book_path)            # text file converted to a string
    number_of_words = count_words(text_file)
    char_dict = count_characters(text_file)           # characters dictionary
    char_sorted_list = dict_to_sorted_list(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print()
    
    for ch in char_sorted_list:
        print(f"The '{ch['character']}' character was found {ch['num']} times")

    print("--- End report ---")

def read_file(book_path):
    with open(book_path) as book:
        return book.read()

def count_words(text_file):
    # split text file into list of words to get length of list with len() method
    words_list = text_file.split()
    return len(words_list)

def count_characters(text_file):
    # lower
    lowered_file = text_file.lower()
    characters_dict = {}
    # for loop to iterate over each character in the text_file given
    for ch in lowered_file:
        if ch not in characters_dict:
            characters_dict[ch] = 1
        else:
            characters_dict[ch] += 1
    # print each key value in caharcters_dict in a formatted way 
    return characters_dict

def dict_to_sorted_list(char_dict):
    sorted_words_list = []
    for character in char_dict:
        if character.isalpha():
            sorted_words_list.append({"character": character, "num": char_dict[character]})
    sorted_words_list.sort(reverse=True, key=sort_on)
    return sorted_words_list

def sort_on(dict):
    return dict["num"]

main()