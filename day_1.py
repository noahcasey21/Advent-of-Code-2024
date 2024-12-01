def smallest_pairs(file : str) -> int:
    f = open(file, 'r')
    data_list = f.readlines()

    left = []
    right = []
    for row in data_list:
        l = row.split()
        left.append(int(l[0]))
        right.append(int(l[1]))

    if len(left) != len(right):
        return -1

    # sort
    left = heap_sort(left)
    right = heap_sort(right)

    sol = 0
    for i, j in zip(left, right):
        n = i - j
        n = n if n >= 0 else j-i
        sol += (n)

    return sol

def heap_sort(a : list) -> list:
    '''
    Smallest to largest
    '''
    
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            tmp = a[j]
            if tmp > a[j + 1]:
                a[j] = a[j + 1]
                a[j + 1] = tmp

    return a

if __name__ == '__main__':
    f = 'day_1.txt'
    sol = smallest_pairs(f)
    if sol == -1:
        'An error has occured'
    else:
        print(f'The solution is {sol}')