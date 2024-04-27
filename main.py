def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    letter_count = count_letters(book_content)
    letter_count_list = change_dict_to_list(letter_count)

    print("----- Report on Frankenstein.txt -----")
    print(f"The program found {word_count} in the document.")
    
    for letters in letter_count_list:
        print(f"The {letters["name"]} character was found {letters["num"]} times.")

    print("----- End report -----")
    

def count_words(novel):
    words = novel.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(novel):
    letter_dict = {}
    for letter in novel:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def change_dict_to_list(letter_dict):
    new_letter_dict = []
    for val in letter_dict:
        if val.isalpha():
            new_letter_dict.append({"name": val, "num": letter_dict[val]})
    new_letter_dict.sort(reverse=True, key=sort_on)
    return new_letter_dict

def sort_on(letter_dict):
    return letter_dict["num"]

main()