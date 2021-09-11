
from sys import stdin
import re

#sol leverages regex module
if __name__ == '__main__':
  #parses number of strings/encrypted codes
  n = int(stdin.readline())
  #iterates through all strings
  for _ in range(n):
    #reads in str
    e = stdin.readline()[:-1]
    if e in ('1','4','78'):
      print('+')
    elif re.match('^.*35$',e):
      print('-')
    elif re.match('^9.*4$',e):
      print('*')
    elif re.match('^190.*',e):
      print('?')


#cpp -> py solution - not submitted to online judge

n = int(stdin.readline())

for _ in range(n):
    s = stdin.readline()
    s_len = len(s)

    if(s == '1' or s == '4' or s == '78'):
        print("+\n")
    elif(s[s_len-1] == '5' and s[s_len-2] == '3'):
        print("-\n")
    elif(s[0] == '1' and s[1] == '9' and s[3] == '0'):
        print("?\n")
    else:
        print("*\n")
