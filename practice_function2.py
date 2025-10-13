import random
print("Welcome to my program!")

words = ["hacker", "bounty", "random", "words", "python"]

secret_word = random.choice(words)
guess = input("guss the secret word: \n").lower()
print(guess)
#check if the letter is in the word
for letter in secret_word:
    if letter in guess:
        print("Right")
    else:
        print("Wrong")