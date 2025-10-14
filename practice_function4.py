import random

print("Welcome to my program!")
words = ["hacker", "bounty", "random"]
secret_word = random.choice(words)

print("You get 5 guesses!")
display_word = ["_" for _ in secret_word]
print(display_word)

guess_count = 0
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess not in secret_word:
        guess_count += 1
        print(f"Wrong guess! You have {5 - guess_count} guesses left.")
    else:
        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                display_word[position] = guess

    print(display_word)

    if "_" not in display_word:
        print("You win!")
        game_over = True
    elif guess_count >= 5:
        print("You lose! The word was:", secret_word)
        game_over = True
