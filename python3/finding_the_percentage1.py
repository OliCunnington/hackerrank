if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    count = 0
    total = 0
    for marks in student_marks[query_name]:
        count +=1
        total += marks
    average = total/count
    print("%.2f" % average)
        