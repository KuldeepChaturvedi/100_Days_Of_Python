import operator
if __name__ == '__main__':
    # dic = dict()
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
    lst.sort(key=operator.itemgetter(1))
    second_lowest_grade = lst[0][1]
    check = False
    for i in lst:
        if i[1] > second_lowest_grade and check == False:
            second_lowest_grade = i[1]
            check = True
    lst.sort(key=operator.itemgetter(0))
    filterd_lst = list(filter(lambda x: (x[1] == second_lowest_grade),lst))
    for i in filterd_lst:
        print(i[0])