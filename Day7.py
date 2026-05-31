# Check if a number is prime
num = int(input("Enter a number:"))

if num < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, num):
        if num % i ==0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")

#2. Count how many prime numbers exist between 1–100
count = 0
for num in range(2,101):
    prime =True

    for i in range(2,num):
        if num % i == 0:
            prime = False
            break

    if prime:
        count += 1
print("Total prime numbers:",count)