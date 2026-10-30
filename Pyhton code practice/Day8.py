# 1 Find the largest number in a list using loop
number = [1,23,19,56,34,78]
largest = number[0]
for num in number:
    if num > largest:
        largest = num
print("largest number:",largest)

# 2.Find the smallest number in a list using loop
number = [1,23,19,56,34,78]
smallest = number[0]
for num in number:
    if num < smallest:
        smallest = num
print("smallest number:",smallest)

# 3.Count vowels in a string
text = input("Enter a string:")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Total vowels:",count)