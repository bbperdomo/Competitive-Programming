# Input
# The input contains several test cases. The first line of a test case contains one integer K indicating
# the number of queries that will be made (0 < K ≤ 103
# ). The second line of a test case contains two
# integers N and M representing the coordinates of the division point (−104 < N, M < 104
# ). Each
# of the K following lines contains two integers X and Y representing the coordinates of a residence
# (−104 ≤ X, Y ≤ 104
# ).
# The end of input is indicated by a line containing only the number zero.
# Output
# For each test case in the input your program must print one line containing:
# • the word ‘divisa’ (means border in Portuguese) if the residence is on one of the border lines
# (North-South or East-West);
# • ‘NO’ (means NW in Portuguese) if the residence is in Northwestern Nlogonia;
# • ‘NE’ if the residence is in Northeastern Nlogonia;
# ‘SE’ if the residence is in Southeastern Nlogonia;
# • ‘SO’ (means SW in Portuguese) if the residence is in Southwestern Nlogonia.


from sys import stdin


# my attempt
k = int(stdin.readline())

while k:

    n,m = map(int,stdin.readline().split())

    for _ in range(k):
        x,y = map(int,stdin.readline().split())

        if x == n or y == m:
            print("divisa")
        elif x < n and y > m:
            print("NO")
        elif x > n and y > m:
            print("NE")
        elif x < n and y < m:
            print("SO")
        else:
            print("SE")
    
    n = int(stdin.readline())


#accepted attempt
if __name__ == '__main__':
  n = int(stdin.readline())
  while n:
    x,y = map(int, stdin.readline().split())
    for _ in range(n):
      a,b = map(int, stdin.readline().split())
      if a==x or b==y:
        print('divisa')  
      elif a>x and b>y:
        print('NE')
      elif a>x and b<y:
        print('SE')
      elif b>y:
        print('NO')
      else:
        print('SO')

    n = int(stdin.readline())