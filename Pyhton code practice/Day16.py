if __name__ == '__main__':
    n = int(input("Enter number of students:"))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_score = student_marks[query_name]
    average_score = sum(query_score)/len(query_score)
    print(f"{average_score:.2f}")


# 2.
import re 

s = input("Enter a string:")
match = re.search(r'([a-zA-Z0-9])\1+',s )
if match:
    print(match.group(1))
else:
    print(-1)
