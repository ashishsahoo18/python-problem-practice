# 1.Create a guessing game using while loop.
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Enter a number(1-10):"))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Congratulation! You correctly Guessed.")