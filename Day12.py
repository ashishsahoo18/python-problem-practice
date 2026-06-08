
n = int(input("Enter a number:"))
student_marks ={}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float,line))
    student_marks[name] = scores
query_name = input("Enter Student name:")
query_score = student_marks[query_name]
average_score = sum(query_score)/len(query_score)
print(f"{average_score:.2f}")