if __name__ == '__main__':
    students = []
    toPrint = []
    minimum, second = 100,100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        if score < minimum:
            minimum, second = score, minimum
        elif score < second and score != minimum:
            second = score
    for student in students:
        if student[1] == second:
            toPrint.append(student[0])
    toPrint.sort()
    for name in toPrint:
        print(name)
            