if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    selected_student = student_marks[query_name]
    percentage = (selected_student[0] + selected_student[1] + selected_student[2]) / 3
    print("{:.2f}".format( percentage ))