polish_words = set()

with open('polish_words.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        polish_words.add(line.strip())

def f(line):
    dp, prev = [-1]*(len(line)+7), [0]*(len(line)+7)
    dp[0] = 0
    for i in range(len(line)):
        for k in range(0, i+1):
            if dp[k] > -1 and line[k:i+1] in polish_words:
                if dp[k] + (i+1-k)*(i+1-k) >= dp[i+1]:
                    dp[i+1] = dp[k] + (i+1-k)*(i+1-k)
                    prev[i] = k-1
    result, idx = '', len(line)-1
    while idx >= 0:
        result = line[prev[idx]+1:idx+1] + ' ' + result
        idx = prev[idx]
    return result

def solve():
    input_file = open('zad2_input.txt', 'r')
    output_file = open('zad2_output.txt', 'w')
    lines = input_file.readlines()
    for line in lines:
        output_file.write(f(line.strip()) + '\n')
    input_file.close()
    output_file.close()

solve()