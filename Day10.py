# 1.Print this pyramid
#     *
#    ***
#   *****
#  *******

rows = 4
for i in range(rows):
    spaces = rows -i -1
    stars = 2*i+1
    print(" " * spaces + "*" * stars)

# 2.print this pattern
#  *******
#   *****
#    ***
#     *
rows = 5
for i in range(rows):
    spaces = i
    stars = 2*(rows-i)-1
    print(" "* spaces + "*"* stars)

# * *
# * * * *
# * * * * * *
# * * * * * * * *
# * * * * * * * * * *

for i in range(1,6):
    print("* "*(2*i))

# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1

n = 5
for i in range(1,n+1):
    start = 1 if i%4 in(0,1) else 0
    for j in range(i):
        print((start + j) %2,end=" ")
    print()

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