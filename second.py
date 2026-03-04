import random

words = [
    "python", "computer", "keyboard", "monitor", "science",
    "program", "college", "student", "internet", "network"
]

score = 0
play_again = "yes"

print("Word Scrambling Game")

while play_again == "yes":

    word = random.choice(words)

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = ""
    for letter in letters:
        scrambled_word = scrambled_word + letter

    print("\nScrambled word:", scrambled_word)

    attempts = 3
    guessed_correctly = False

    while attempts > 0:
        guess = input("Enter your guess: ")

        if guess.lower() == word:
            print("Correct guess!")
            score = score + 1
            guessed_correctly = True
            break
        else:
            attempts = attempts - 1
            print("Wrong guess. Attempts left:", attempts)

    if guessed_correctly == False:
        print("You failed to guess the word.")
        print("The correct word was:", word)

    print("Current Score:", score)

    play_again = input("Do you want to play another round? (yes/no): ")

print("Final Score:", score)
print("Game Over")
