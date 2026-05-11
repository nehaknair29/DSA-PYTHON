#arrays from HackerRank
n=int(input())
arr=list(input())

#another dict
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")
#list comprehension
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = [student[1] for student in students]

    unique_grades = sorted(set(grades))
    second_lowest = unique_grades[1]

    names = [student[0] for student in students if student[1] == second_lowest]

    for name in sorted(names):
        print(name)
