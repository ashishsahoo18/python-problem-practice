# HackerRank problem practice in 30 Days.

# Day 0
s = input()
print("Hello, World.")
print(s)

# Day 1
i = 4
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


# Day 4
class Person:
    def __init__(self,initialAge):
        if initialAge <0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

    # Day 5
    #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
for i in range(1,11):
    print(n,"x",i,"=",n*i)

# day 6
t = int(input())
for s in range(t):
    s = input()
    print(s[::2],s[1::2])

# Day 7
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
print(*arr[::-1])

# Day8
n = int(input())

phone_book = {}

for i in range(n):
    name,number = input().split()
    phone_book[name] = number
    
while True:
    try:
        query = input()
        
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    
    except EOFError:
        break

# Day 9
#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Day10
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
binary = bin(n)[2:]

count = 0
max_count = 0

for digit in binary:
    if digit == '1':
        count += 1
        max_count = max(max_count,count)
    else:
        count = 0
print(max_count)

# Day11
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum = -63
    
    for i in range(4):
        for j in range(4):
            hourglass = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2]
                + arr[i+1][j+1]
                + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            
            max_sum = max(max_sum, hourglass)
    print(max_sum)


# Day12
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastname,idNumber,scores):
        super().__init__(firstName,lastName,idNumber)
        self.scores = scores
        
    def calculate(self):
        average = sum(self.scores)/ len(self.scores)
        
        if 90 <= average <= 100:
            return'O'
        elif 80 <= average <= 90:
            return'E'
        elif 70 <= average <= 80:
            return'A'
        elif 55 <= average <= 70:
            return'P'
        elif 40 <= average <= 55:
            return'D'
        else:
            return 'T'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

# Day13
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price = price
        
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

# Day14
class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# Day 15
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        new_node = Node(data)
        
        if head is None:
            return new_node
        current = head
        
        while current.next:
            current = current.next
        
        current.next = new_node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  


# Q) Sample Input 1

# 17 28 30
# 99 16 8
# Sample Output 1

# 2 1

# (Code in c++) only logic.
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

vector<int> compareTriplets(vector<int> a, vector<int> b) {
    int Alice = 0;
    int Bob = 0;
    for(int i = 0; i<3; i++){
        if(a[i] > b[i]){
            Alice++;
        }
        else if(a[i] < b[i]){
            Bob++;
        }
    }
    return {Alice , Bob};
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split(rtrim(a_temp_temp));

    vector<int> a(3);

    for (int i = 0; i < 3; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    string b_temp_temp;
    getline(cin, b_temp_temp);

    vector<string> b_temp = split(rtrim(b_temp_temp));

    vector<int> b(3);

    for (int i = 0; i < 3; i++) {
        int b_item = stoi(b_temp[i]);

        b[i] = b_item;
    }

    vector<int> result = compareTriplets(a, b);

    for (size_t i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << " ";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
# Q) Sample Input

# STDIN                                                   Function
# -----                                                   --------
# 5                                                       arr[] size n = 5
# 1000000001 1000000002 1000000003 1000000004 1000000005  arr[...]  
# Output

# 5000000015

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);



long aVeryBigSum(vector<long> ar) {
    long sum = 0;
    for(int i=0; i<ar.size(); i++){
        sum = sum+ar[i];
    }
    return sum;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ar_count_temp;
    getline(cin, ar_count_temp);

    int ar_count = stoi(ltrim(rtrim(ar_count_temp)));

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split(rtrim(ar_temp_temp));

    vector<long> ar(ar_count);

    for (int i = 0; i < ar_count; i++) {
        long ar_item = stol(ar_temp[i]);

        ar[i] = ar_item;
    }

    long result = aVeryBigSum(ar);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
