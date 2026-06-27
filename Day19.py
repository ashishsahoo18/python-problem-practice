# 6.Print Fibonacci series
# Example:
# 0 1 1 2 3 5 8 13 ...........

count = int(input("Enter a number:"))
a = 0
b = 1

for i in range(count):
    print(a,end=" ")

    next_number = a+b
    a = b
    b = next_number

# To continue or extend the sequence, use the recursive formula:\(F_{n} = F_{n-1} + F_{n-2}\)