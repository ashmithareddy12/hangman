import random

words = ["python", "computer", "program", "college", "student"]

word = random.choice(words)
guessed_word = ["_"] * len(word)

incorrect_guesses = 0
max_attempts = 6
guessed_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_attempts and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    letter = input("Enter a letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one letter.")
        continue

    if letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(letter)

    if letter in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)