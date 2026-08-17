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


i1 = 4
d1 = 4.0
s = "HackerRank"

i2 = int(input(" Enter a number: "))
d2 = float(input(" Enter a float: "))
s2 = input(" Enter a String: ")

print(i1 + i2)
print(d1 + d2)
print(s + s2)