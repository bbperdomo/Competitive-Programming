
#accepted solution
n = int(input())

for i in range(n):
    p = []
    max_ = 0
    

    for _ in range(10):
        #stores url in x, stores score in y
        #calling split() with dot on input() parses the input by strings seperated by white space
        x, y = input().split()
        
        #keep track of largest relevanve score w/ each iteration of test line
        p.append((x, int(y)))
        if int(y) > max_:
            max_ = int(y)
            
    print("Case #{}:".format(i + 1))
    #prints all urls that have max relevance score 
    for x, y in p:
        if y == max_:
            print(x)