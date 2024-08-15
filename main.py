def count_words(string_of_words) -> int:
    word_count = string_of_words.split()

    return len(word_count)




def count_letters(parm_string):
# returns dictionary of letter/count pairs
    letters = {}

    for i in range(0, len(parm_string)):
        letter = (parm_string[i]).lower()
    
        if letter.isalpha():
            if letter in letters:
                current_letter_count = letters[letter]
            else:
                current_letter_count = 0

            letters[letter] = current_letter_count + 1

    return letters




def sort_func(dict):
    return dict['count']

def sort_letter_counts(unsorted_letter_counts):
# method takes a dictionary of letter/count pairs.
# converts to a list of two-entry dictionaries (letter and count)
# doing so enables sorting by the list.sort() method
    list_of_dictionaries = []

    for key, value in unsorted_letter_counts.items(): ## dictionary_entry contains letter/count pair
        double_dict = {
            "letter" : key,
            "count" : value
        }

        list_of_dictionaries.append(double_dict)
    
    list_of_dictionaries.sort(reverse=True, key=sort_func)

    return list_of_dictionaries



def print_letter_count_dictionary(letter_count_dict):
# function takes a dictionary of letter/count pairs.
# prints them.
    for key, value in letter_count_dict.items(): ## dictionary_entry contains letter/count pair
        print(f"The '{key}' letter was found {value} times")



def print_sorted_letter_count_list(letter_count_lod):
# function takes a list of two-item dictionaries, each holding a letter/count pair.
# prints them.
    for dict in letter_count_lod: ## dictionary_entry contains letter/count pair
        print(f"The '{dict['letter']}' letter was found {dict['count']} times")




def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document")
        print("")
        
        letter_counts = count_letters(file_contents)
        # print_letter_count_dictionary(letter_counts)
        sorted_letter_counts = sort_letter_counts(letter_counts)
        print_sorted_letter_count_list(sorted_letter_counts)



main()
