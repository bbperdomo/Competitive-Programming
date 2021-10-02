# Input
# The first line of input is an integer T (T < 30) that indicates the number of test cases. Each case starts
# with an integer N (0 < N < 50) that determines the number of walls. The next line gives the height
# of the N walls from left to right. Each height is a positive integer not exceeding 10.
# Output
# For each case, output the case number followed by 2 integers, total high jumps and total low jumps,
# respectively. Look at the sample for exact format.
# Sample Input
# 3
# 8
# 1 4 2 2 3 5 3 4
# 1
# 9
# 5
# 1 2 3 4 5
# Sample Output
# Case 1: 4 2
# Case 2: 0 0
# Case 3: 4 0

n = int(input())

for i in range(0, n):
	m = int(input())
	
	x = 0
	high = low = 0
	a = list(map(int, input().split()))
	
	for j in a:
		if x == 0:
			x = j
			continue
		
		if j > x:
			high += 1
		elif j < x:
			low += 1
		x = j
	
	print("Case {0}: {1} {2}".format(i+1, high, low))