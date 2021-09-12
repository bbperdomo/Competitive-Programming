#sample input
# 2
# 3
# LEFT
# RIGHT
# SAME AS 2

#sol 1
from sys import stdin

if __name__ == '__main__':
    #read in num of test cases as tc
    tc = int(stdin.readline())
    #iterate through all tcs
    for _ in range(tc):
        #read in num of instructions for each test case (tc)
        n = int(stdin.readline())
        #this list is used to access previous instructions
        inst = []
        #init robot pos to 0
        pos = 0
        #iterate through each instruction for each test case
        for _ in range(n):
            #read in only first string of each instruction, so in 'SAME AS 2', only 'SAME' is stored
            li_s = stdin.readline()[:-1].split()
            #sets li equal to -1
            li = -1 
            #if 1st string is right, increment li right 1
            if li_s[0] == 'RIGHT':
                #sets li equal to positive 1 
                li = +1
            
            elif li_s[0]=='SAME':
                li = inst[int(li_s[-1])-1]
            #always append every instruction we encounter
            inst.append(li)
            #always update the current position
            pos += li
        print(pos)


#solution 2
cmd = []

def cmdin(c):
	if c == "LEFT":
		cmd.append(-1)
		return -1
	elif c == "RIGHT":
		cmd.append(1)
		return 1
	else:
		cmd.append(cmd[int(c) - 1])
		return cmd[-1]

n = int(input())
for _ in range(n):
	m = int(input())
	
	cmd = []
	now = 0
	for i in range(m):
		k = list(input().split())
		if len(k) == 1:
			now += cmdin(k[0])
		else:
			now += cmdin(k[2])
	print(now)




