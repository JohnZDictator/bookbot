def main():
    bookPath = "books/frankenstein.txt"
    bookText = get_book_text(bookPath)
    # print(bookText)
    words_count = get_words_count(bookText)
    # print(words_count)
    print(f"--- Begin report of {bookPath} ---")
    print(f"{words_count} words found in document\n")
    words_occurence = get_character_occurence(bookText)
    for character in words_occurence:
        if not character.isalpha():
            continue
        print(f"The '{character}' was found {words_occurence[character]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    words = text.split()
    return len(words)

def get_character_occurence(bookText):
    char_occur = {}
    for word in bookText:
        for character in word:
            lower_character = character.lower()
            if lower_character in char_occur:
                char_occur[lower_character] += 1
            else:
                char_occur[lower_character] = 1
    return char_occur

main()