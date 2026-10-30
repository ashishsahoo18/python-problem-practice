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

# 2. Print all tables from 1–10 using nested loops.
for i in range(1,11):
    print(f"\n Table of {i}")

    for j in range(1,11):
        print(f"\n {i}*{j}={i*j}",end ="")