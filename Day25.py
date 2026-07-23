# HackerRank problem practice in 30 Days.

# Day 0
s = input()
print("Hello, World.")
print(s)

# Day 1
i = 4
d = 4.0
s = 'HackerRank '
d = 4.0
s = 'HackerRank '

i2 = int(input())
d2 = float(input())
s2 = input()

print(i+i2)
print(d+d2)
print(s + s2)


# Day 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total_cost = meal_cost + tip + tax
    
    print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)


# Day 3
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
if N %2 != 0:
    print("Weird")
elif 2<= N <=5:
    print("Not Weird")
elif 6<= N <=20:
    print("Weird")
else:
    print("Not Weird")
