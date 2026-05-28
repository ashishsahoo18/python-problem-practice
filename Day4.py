# 1.
for i in range(10,0,-1):
    print(i)
# 2.
total = 0
for i in range(1,101):
    total += i
    print("sum",i,"=",total)
# 3.
number = "1234"
for i in number[::-1]:
    print(i)
    
# 4.
num = 5
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")