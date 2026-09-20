import random
#11
def is_palindrome(word):
    return word == word[::-1]


#12
def histogram(numbers):
    for num in numbers:
        print("*" * num)


#13


name = input("Hello! What is your name?\n")

number = random.randint(1, 20)

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")

guesses = 0

while True:
    guess = int(input())
    guesses += 1

    if guess < number:
        print("Your guess is too low.")
        print("Take a guess.")
    elif guess > number:
        print("Your guess is too high.")
        print("Take a guess.")
    else:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
        break


