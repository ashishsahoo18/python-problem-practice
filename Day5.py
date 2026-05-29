# 1. Count digits in a number
# A.using string
num = int(input("Enter number:"))
print("Total digits:",len(num))

# B.
num = int(input("Enter number:"))
count = 0
while num != 0:
    num = num//10
    count +=1
print("Total digits:",count)

# C.Code negative numbers aur 0 ko properly handle karke digits count karta hai.
num = abs(int(input("Enter number:")))
count = 0

if num ==0:
    count =1

while num != 0:
    num = num//10
    count +=1
print("Total digits:",count)