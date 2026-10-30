if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(set(arr))[-2])


# 2.
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    second_lowest = sorted(set(score for _, score in students))[1]
    
    names = []
    for name,score in students:
        if score == second_lowest:
            names.append(name)
    for name in sorted (names):
        print(name)
            
