#WAP to input a word and:
#a.Print it in reverse order
#b.Check it is Palindrome or not
#c.Print the first and last character of that word
#d.Input another word and check they are equal or not or check first one is existing in the main word or not.
#e.Convert the word into uppercase if it is in lowercase, or convert it into lowercase if it is in uppercase.
#f.Convert the word into another by swapping first and last character.
#g.Convert the word into another by shifting one character right.

wrd = input('Enter WORD: ')
def reverse_word(word):
    return word[::-1]

def is_palindrome(word):
    return word == reverse_word(word)

def first_last_characters(word):
    return word[0], word[-1]

def check_equal_or_in(word1, word2):
    if word1 == word2:
        return "The words are equal."
    elif word1 in word2:
        return "The first word is a substring of the second word."
    else:
        return "The words are different."

def change_case(word):
    if word.islower():
        return word.upper()
    else:
        return word.lower()

def swap_first_last_characters(word):
    return word[-1] + word[1:-1] + word[0]

def shift_one_character_right(word):
    return word[-1] + word[:-1]

word = input("Enter a word: ")

reversed_word = reverse_word(word)
print("Reversed word:", reversed_word)

if is_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

first_char, last_char = first_last_characters(word)
print("First character:", first_char)
print("Last character:", last_char)

word2 = input("Enter another word: ")
print(check_equal_or_in(word, word2))

case_converted_word = change_case(word)
print("Case converted word:", case_converted_word)

swapped_word = swap_first_last_characters(word)
print("Swapped word:", swapped_word)

shifted_word = shift_one_character_right(word)
print("Shifted word:", shifted_word)