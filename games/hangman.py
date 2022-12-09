from logics import verify
from words import words
import string

def hangman():
    word = verify(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 8

    print('Word length = ', len(word_letters))
    while len(word_letters) > 0 and lives > 0:
        correct_words =[letter if letter in used_letters else '-' for letter in word]
        print('Correct letters >> ', ' '. join(correct_words))
        print('Lives = ', lives, 'letters used: ', ' ' .join(used_letters))
        user_letter = input('Enter letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")
            else:
                lives -= 1
                
        elif user_letter in used_letters:
            print(user_letter, "letter used")
        else:
            print('Invalid character')
    
    if lives == 0:
        print('You are out of lives, the word was', word.upper())
    else:
        print('You got it!', word)


if __name__ == '__main__':
    hangman()
