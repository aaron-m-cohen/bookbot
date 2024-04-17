def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_freq = {}
    for c in text:
        c = c.lower()
        if c in letter_freq:
            letter_freq[c] = letter_freq[c] + 1
        else:
            letter_freq[c] = 1
    return letter_freq

def sort_on(dict):
    return dict["count"]

def sorted_frequency_list(dict):
    dict_list = []
    for item in dict:
        dict_list.append({"char": item, "count": dict[item]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_char_freqs(char_freqs):
    sorted_list = sorted_frequency_list(char_freqs)
    for c in sorted_list:
        if c["char"].isalpha():
            print(f"The '{c["char"]}' character was found {c["count"]} times")

def main():
    file_path = "./books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

        print(f"--- Begin report of {file_path} ---")

        num_words = count_words(file_contents)
        print(f"{num_words} words found in the document")
        print()
        
        char_freqs = count_letters(file_contents)
        print_char_freqs(char_freqs)

    print("--- End report ---")

main()
