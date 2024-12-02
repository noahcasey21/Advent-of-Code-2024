def count_safe(file : str) -> int:
    f = open(file, 'r')
    data = f.readlines()

    safe_count = 0

    for record in data:
        compare = {
            'increase' : lambda a, b : a < b,
            'decrease' : lambda a, b : a > b
        }
        low_bound = 1
        high_bound = 3
        values = [int(i) for i in record.split()]
        if len(values) == 1:
            safe_count += 1
            continue
        
        if values[0] < values[1]:
            direction = 'increase'
        else:
            direction = 'decrease'

        good_record = True
        for i in range(len(values) - 1):
            if not compare[direction](values[i], values[i + 1]):
                good_record = False
            distance = abs(values[i] - values[i + 1])
            if (distance > high_bound) or (distance < low_bound):
                good_record = False

        if good_record:
            safe_count += 1

    return safe_count

if __name__ == '__main__':
    f = 'day_2.txt'
    safe_count = count_safe(f)
    if safe_count == -1:
        print('There was an error.')
    else:
        print(f'There are {safe_count} safe records.')