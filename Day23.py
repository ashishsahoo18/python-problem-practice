# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

# bbbb*
# bbb*b*
# bb*b*b*
# b*b*b*b*
# *b*b*b*b*
n = 5
for i in range(1,n+1):
    print("b" * (n - i) + "b".join(["*"] * i))