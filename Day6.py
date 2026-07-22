# 1.Print multiplication table of a number
num = int(input("Enter a number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

# 2.Print this pattern
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print("*"*i)