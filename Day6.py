# 1.Print multiplication table of a number
num = int(input("Enter a number"))
for i in range(1,11):
    print("num *",i,"=",num*i)

# 2.Print this pattern
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print("*"*i)
    
    
# 3.Print this pattern
# 1
# 12
# 123
# 1234
# 12345
for i in range (1,6):
    for j in range(1,1+i):
        print(j,end="")
    print()

# 4.Print this reverse pattern
# 54321
# 5432
# 543
# 54
# 5
for i in range (5,0,-1):
    for j in range(5,5-i,-1):
        print(j,end="")
    print()

# 6.Print Fibonacci series
# Example:
# 0 1 1 2 3 5 8 13

count = 8
a = 0
b = 1
for i in range(count):
    print(a,end=" ")

    next_number = a+b
    a = b
    b = next_number 

# 7.Print this pattern
# 1
# 22
# 333
# 4444
# 55555
for i in range (1,6):
    print(str(i)*i)