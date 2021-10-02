# The first line contains the number of words that your little brother has written. Each of the following
# lines contains a single word with all letters in lower-case. The words satisfy the constraints above: at
# most one letter might be wrong, but the word length is always correct. There will be at most 10 words
# in the input.
# Output
# For each test case, print the numerical value of the word.

# Sample Input
# 3
# owe
# too
# theee
# Sample Output
# 1
# 2
# 3


n = int(input())

for i in range(n):
	m = input()

	if len(m) == 5:
		print("3")
		continue
	
	x = 0
	if m[0] == 'o':
		x += 1
	if m[1] == 'n':
		x += 1
	if m[2] == 'e':
		x += 1
		
	if x > 1:
		print("1")
	else:
		print("2")