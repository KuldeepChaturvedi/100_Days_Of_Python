'''
Let's learn about list comprehensions! You are given three integers X, Y, and Z 
representing the dimensions of a cuboid along with an integer N. 
You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid 
where the sum of is not equal to N.
Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z; 
'''

if __name__ == '__main__':
    print('Enter X =')
    x = int(input())
    print('Enter Y =')
    y = int(input())
    print('Enter Z =')
    z = int(input())
    print('Enter N =')
    n = int(input())

    list_combinations = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if ((i + j + k) != n):
                    list_combinations.append([i,j,k])

    print('-----------'*10)
    print(list_combinations)
    print('-----------'*10)
    for i in list_combinations:
        print(str(i) + ' i + j + k = ' + str(i[0] + i[1] + i[2]))


    