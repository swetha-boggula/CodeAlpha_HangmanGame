import random

# List of predefined words
words = ["apple", "banana", "grapes", "orange", "mango"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("====== HANGMAN GAME ======")

while attempts > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)