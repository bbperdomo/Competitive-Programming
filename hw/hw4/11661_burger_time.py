# import sys

# sys.stdin = open('input.txt')
# while True:
#     L = int(input())
#     if not L:
#         break
#     A = input().strip()
#     r, d = 0, 0
#     res = 1 << 31
#     for i, c in enumerate(A):
#         if c == 'Z':
#             res = 0
#             break
#         if c == 'R':
#             r = i
#         elif c == 'D':
#             d = i
#             res = min(res, d - r)
#     print (res)


while True:
  num_chars = int(input())
  if num_chars == 0:
    break

  in_map = str(input())
  r = -1
  d = -1

  sol = 200000000
  for i, ch in enumerate(in_map):
    if ch == 'Z':
      sol = 0
      break
    if ch == 'R':
      r = i
      if d != -1:
        if i - d < sol:
          sol = i - d 
    if ch == 'D':
      d = i
      if r != -1:
        if i - r < sol:
          sol = i - r

  print(sol)