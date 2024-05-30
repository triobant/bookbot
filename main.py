def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(str(text))
    chars_dict = get_letter_count(str(text))

    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document\n")

    for char_info in chars_dict:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")

    print(f"--- End report ---")


def count_words(text: str):
    words = text.split()
    return len(words)


def get_letter_count(text: str):
    chars_list = []
    appearing_characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in appearing_characters:
            appearing_characters[lowered] += 1
        else:
            appearing_characters[lowered] = 1

    for key in appearing_characters:
        if key.isalpha():
            char_dict = { "char": key, "num": appearing_characters[key] }
            chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=lambda x: x["num"])
    return chars_list


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
