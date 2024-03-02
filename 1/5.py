import numpy as np
import random

with open('zad5_input.txt', 'r')as f:
    line = f.readline().split()
    rows, cols, rows_desc, cols_desc = int(line[0]), int(line[1]), [], []
    for _ in range(rows):
        line = f.readline().split()
        rows_desc.append(int(line[0]))
    for _ in range(cols):
        line = f.readline().split()
        cols_desc.append(int(line[0]))
            
np.random.seed()

def check(arr):
    res = 0
    for i in range(rows):
        cnt = 0
        for j in range(cols):
            cnt += arr[i][j]
        res += abs(rows_desc[i]-cnt)
    for i in range(cols):
        cnt = 0
        for j in range(rows):
            cnt += arr[j][i]
        res += abs(cols_desc[i]-cnt)

    return res

def correct_row(idx, arr):
    cnt = 0
    for i in range(cols):
        if arr[idx][i] == 0 and cnt > 0 and cnt != rows_desc[idx]:
            return False
        cnt += arr[idx][i]
    return cnt == rows_desc[idx]

def correct_col(idx, arr):
    cnt = 0
    for i in range(rows):
        if arr[i][idx] == 0 and cnt > 0 and cnt != cols_desc[idx]:
            return False
        cnt += arr[i][idx]
    return cnt == cols_desc[idx]

def solve():
    tries = 1000000
    arr = np.zeros((rows, cols), int)
    while tries > 0:
        tries -= 1
        changes = 1000
        while changes > 0:
            changes -= 1
            q = [i for i in range(rows) if not correct_row(i, arr=arr)]
            if len(q) == 0:
                q = [i for i in range(cols) if not correct_col(i, arr=arr)]
                if len(q) == 0:
                    return arr
                random_col = random.choice(q)
                best_res, best_idx = np.inf, 0
                for i in range(rows):
                    arr[i][random_col] = arr[i][random_col] ^ 1
                    res = check(arr=arr)
                    if res < best_res:
                        best_res = res
                        best_idx = i
                    arr[i][random_col] = arr[i][random_col] ^ 1
                arr[best_idx][random_col] = arr[best_idx][random_col] ^ 1
            random_row = random.choice(q)
            best_res, best_idx = np.inf, 0
            for i in range(cols):
                arr[random_row][i] = arr[random_row][i] ^ 1
                res = check(arr=arr)
                if res < best_res:
                    best_res = res
                    best_idx = i
                arr[random_row][i] = arr[random_row][i] ^ 1
            arr[random_row][best_idx] = arr[random_row][best_idx] ^ 1
        if tries > 0: arr = np.random.randint(2, size=(rows, cols))
    return arr

result = solve()

'''
for i in range(rows):
    for j in range(cols):
        if result[i][j] == 0:
            print('.', end='')
        else:
            print('#', end='')
    print()
print(check(result))
'''

output_file = open('zad5_output.txt', 'w')

for i in range(rows):
    for j in range(cols):
        if result[i][j] == 0:
            output_file.write('.')
        else:
            output_file.write('#')
    output_file.write('\n')

output_file.close()