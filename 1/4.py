import numpy as np

def opt_dist(row, number):
	arr = np.zeros(len(row)+1, dtype='int32')
	for i in range(len(row)):
		arr[i+1] = arr[i] + int(row[i])
	ans = len(row)
	for i in range(1, len(row)-number+2):
		ans = min(ans, (number-(arr[i+number-1]-arr[i-1])) + arr[i-1] + (arr[-1]-arr[i+number-1]))
	return ans

input_file = open('zad4_input.txt', 'r')
lines =  input_file.readlines()

output_file = open('zad4_output.txt', 'w')

for line in lines:
	x = line.strip().split(" ")
	output_file.write(str(opt_dist(x[0], int(x[1]))) + '\n')
	
output_file.close()