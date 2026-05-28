# 1.Find the sum of all even numbers from 1 to 50
total = 0
for i in range (1,51):
    if i%2 == 0:
        total += i
        print("sum =",total)

# 2.Print the square of numbers from 1 to 10.
total = 0
for i in range (1,11):
    total += i
    print("Square of ",i,"=",i*i)