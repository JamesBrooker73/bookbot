def get_word_count(book_text):
    return len(book_text.split())

def count_characters(book_text):
    char_dictionary = {}
    for char in book_text:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    return char_dictionary

def sort_on(items):
    return items["num"]

def sort_dictionary(char_dictionary):
    sorted_char_list = []
    
    for char in char_dictionary:
        
        sorted_char_list.append({
            "char": char,
            "num": char_dictionary[char]
        })
        
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list




