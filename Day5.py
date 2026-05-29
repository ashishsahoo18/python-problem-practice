# 1. Count digits in a number
# A.using string
num = input("Enter a number:")

print("Total digits:", len(num))

# B.
num = int(input("Enter a number:"))
count = 0
while num != 0:
    num = num//10
    count +=1
print("Total digits:",count)

# C.Code negative numbers aur 0 ko properly handle karke digits count karta hai.
num = abs(int(input("Enter a number:")))
count = 0

if num ==0:
    count =1

while num != 0:
    num = num//10
    count +=1
print("Total digits:",count)


# 2.Check if a number is palindrome
num = int(input("Enter a number:"))
original = num
reverse = 0

while num>0:
    digits = num % 10
    reverse = reverse *10 + digits
    num = num//10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")