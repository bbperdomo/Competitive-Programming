#sample input
# 3 1000 2 3 - N,B,H,W
# 200 - cost per person
# 0 2 2 - num of available beds for each weekend
# 300 - cost per person
# 27 3 20 - num of available beds for each weekend

import sys

#sys.stdin = open('input.txt')

#bitshift. 1 << 30 means 1 * 2^30
INF = 1 << 30
while True:
    result = INF
    try:
        #n=people,b=budget,h=num of hotels,w=num of weeks
        #splits and calls int() on each num; stores them in vars
        N, B, H, W = map(int, raw_input().split())
    except:
        break

    #cycle through total hotels
    for i in range(H):
        #cost per person
        P = int(input())
        #casts each bed num into an int
        beds = map(int, raw_input().split())
        #iter through different num of beds
        for b in beds:
            #for each bed, continually test if the num of beds is at least the same number as the participants
            #AND the cost per person times total participants meets the budget
            #Then do this for each bed number(weekend) and constantly update the minimum cost you encounter
            if b >= N and N * P <= B:
                result = min(result, N * P)
    #if you find a trip in budget, print the cost
    if result != INF:
        print(result)
    else:
        print ('stay home')