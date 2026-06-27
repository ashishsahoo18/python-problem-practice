# 4.Print this reverse pattern
# 54321
# 5432
# 543
# 54
# 5
for i in range(5,0,-1):
    for j in range(5,5-i,-1):
        print(j,end="")
    print()