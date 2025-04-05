def count_words(text_file):
    # split text file into list of words to get length of list with len() method
    words_list = text_file.split()
    return len(words_list)


# returns a dictionary with the number of times each character appears in the text file
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
    # print each key value in characters_dict in a formatted way 
    return characters_dict