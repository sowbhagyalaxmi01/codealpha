import random

words = ["python", "banana", "rocket", "guitar", "window"]
word = random.choice(words)

guessed_letters = []

max_attempts = 5
wrong_guesses = 0

print("Welcome to Hangman Game!")

while wrong_guesses < max_attempts:

    # show word progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # win check
    if "_" not in display:
        print("🎉 You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    # check guess
    if guess not in word:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_attempts - wrong_guesses}")
    else:
        print("Correct guess!")

# game result
if wrong_guesses == max_attempts:
    print("💀 Game Over! The word was:", word)