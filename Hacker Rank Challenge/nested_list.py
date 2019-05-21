import operator

if __name__ == '__main__':
    dic = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic[name] = score
    
    print(min(dic.values()))
    dic = sorted(dic.items(),key=operator.itemgetter(0))
    # print(dic)
    # second_lowest_grade = min(lst)[1]
    # for i in lst:
    #     if i[1] == second_lowest_grade:
    #         print(i[0]) 