# #Input
# First line of the input file is an integer t (t < 15) which denotes how many sets of inputs are there.
# Each of the next t lines contain two integers a and b (|a|, |b| < 1000000001).
#Ex:
# 1
# 23


# Output
# For each line of input produce one line of output. This line contains any one of the relational operators
# ‘>’, ‘<’ or ‘=’, which indicates the relation that is appropriate for the given two numbers.

#takes in t value
n = int(input())

#iterates through each line, t number of times
for i in range(n):
    #secret sauce
    #creates a mapping bw the numbers on each line
	x, y = map(int, input().split())
	
    #compares the mapping values
	if x > y:
		print(">")
	elif x < y:
		print("<")
	else:
		print("=")