# 1. Number pyramid
# 1
# 121
# 12321
# 1234321

rows = 4
for i in range(1,rows+1):

    for j in range(1,i+1):
        print(j,end="")

    for j in range(i-1,0,-1):
        print(j,end="")

    print()

# or
n = input("Enter number:")
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
n = 5
ch = ord("A")
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end=" ")
        ch +=1
    print()


# A
# BB
# CCC
# DDDD
# EEEEE
n = 5
for i in range(1,n+1):
    print(chr(ord("A") + i-1) * i)


# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(chr(ord("A")+j),end=" ")
    print()


#     A
#    BCD
#   EFGHI
#  JKLMNOP
# QRSUVWXY
n = 5
ch = ord("A")
for i in range(1, n + 1):
    print( "  " * (n - i), end="")
    for j in range(2 * i - 1):
        print(chr(ch), end="")
        ch += 1
    print()


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
n = 5
for i in range(1,n+1):
    print("*" *i)
for i in range(n-1,0,-1):
    print("*"*i)


# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *
n = 5
for i in range(1,n+1):
    print("*" *i)
for i in range(n,0,-1):
    print("*"*i)


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
n = 5
for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))


#     5
#    545
#   54345
#  5432345
# 543212345
n = 5
for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(n, n - i, -1):
            print(j, end="")
        for j in range(n - i + 2, n + 1):
            print(j, end="")
        print()
