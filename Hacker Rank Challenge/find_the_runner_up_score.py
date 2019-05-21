'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given scores. 
Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    print('Enter Length =')
    n = int(input())
    print('Enter Array =')
    arr = map(int, input().split())
    arr = list(arr)
    high_score = max(arr) 
    runner_up_score = min(arr) 
    for i in list(arr):
        if i > runner_up_score and i < high_score:
                runner_up_score = i
    print('Runner-Up Score = ' + str(runner_up_score))
