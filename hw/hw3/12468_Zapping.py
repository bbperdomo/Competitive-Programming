
#my attempt
#logic is correct, just not implemented to parse input and clear online judge
a = -1
b = -1


if b - a > 50:
    print(100-b+a)

else:
    print(b-a)


#accepted solution
from sys import stdin

if __name__ == '__main__':
    while True: #continually parses input until none left
        #handles parsing input, and casts each x as an int, stores in a and b
        a,b = [int(x) for x in stdin.readline().split()]
        #checks for valid input - only positive ints allowed
        if a<0: break

        #finding total distance bw a and b
        d = abs(a-b)
        #does what my if-else above does
        dm = min(d,100-d)
        print(dm)