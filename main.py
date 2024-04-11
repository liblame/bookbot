import re

def count_words(book):
    words = book.split()
    print(len(words))

def count_letters(book):
    letters = {}
    for letter in ((re.findall('[a-z]', book.lower()))):
        letters[letter] = letters.get(letter,0)+1
    for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")


with open("books/frankenstein.txt", 'r') as f:
    read_data = f.read()
    count_letters(read_data)
