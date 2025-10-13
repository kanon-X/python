import random
print("welcome to my program!")
words= ["hacker","bounty", "random"]
secret_word = random.choice(words)
display_word = []
for letter in secret_word:
    display_word += "_"
    print(display_word)
guess = input("guess the secret word: \n").lower()

for letter in secret_word:
    if letter in guess:
        print("Right")
    else:
        print("Wrong")