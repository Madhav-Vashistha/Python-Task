import random

words = ["python", "apple", "chair", "table", "mouse"]

score = 0

print("Word Scramble Game")

word = random.choice(words)

letters = list(word)
random.shuffle(letters)

scrambled = ""
for letter in letters:
    scrambled = scrambled + letter

print("Guess the word:", scrambled)

attempts = 3

while attempts > 0:
    guess = input("Enter your guess: ")

    if guess == word:
        print("Correct!")
        score = score + 1
        break
    else:
        print("Wrong")
        attempts = attempts - 1

if attempts == 0:
    print("You lost. The correct word was:", word)

print("Your score is:", score)