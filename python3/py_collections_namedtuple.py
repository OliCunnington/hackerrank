from collections import namedtuple

no_students = int(input())
Student = namedtuple("Student", input())
students = []
for i in range(no_students):
    inp = input().split()
    students.append(Student(inp[0], inp[1], inp[2], inp[3]))


print("{:,.2f}".format(sum([int(s.MARKS) for s in students]) / len(students)))