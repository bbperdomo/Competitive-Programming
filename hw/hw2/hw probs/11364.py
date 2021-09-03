# Input
# The first line of input gives the number of test cases, 1 ≤ t ≤ 100. There are two lines for each test
# case. The first gives the number of stores Michael wants to visit, 1 ≤ n ≤ 20, and the second gives
# their n integer positions on Long Street, 0 ≤ xi ≤ 99.
# Output
# Output for each test case a line with the minimal distance Michael must walk given optimal parking

# Sample Input
# 2
# 4
# 24 13 89 37
# 6
# 7 30 41 14 39 42
# Sample Output
# 152
# 70


def Main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        A.sort()
        res = abs(A[0] - A[n - 1])
        print(res*2)

if __name__ == '__main__':
    Main()



#another way to do it
n = int(input())
for i in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print("{}".format((a[-1]-a[0]) * 2))
