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

# 7.Print this pattern
# 1
# 22
# 333
# 4444
# 55555
for i in range (1,6):
    print(str(i)*i)