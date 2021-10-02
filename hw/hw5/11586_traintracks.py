# Input
# Input begins with the number of test cases. Each following line contains one test case. Each test case
# consists of a list of between 1 and 50 (inclusive) train track pieces. A piece is described by two code
# letters: ‘M’ for male or ‘F’ for female connector. Pieces are separated by space characters.
# Output
# For each test case, output a line containing either ‘LOOP’ or ‘NO LOOP’ to indicate whether or not all
# the pieces can be joined into a single loop.
# Sample Input
# 4
# MF MF
# FM FF MF MM
# MM FF
# MF MF MF MF FF
# Sample Output
# LOOP
# LOOP
# LOOP
# NO LOOP



num_tests = int(input())


for test in range(num_tests):
  diff = 0
  num_tracks = 0

  tracks = list(map(str, input().split()))
  for track in tracks:
    if track == "MM":
      diff += 1
    elif track == "FF":
      diff -= 1
    num_tracks += 1
  
  print("LOOP" if diff == 0 and num_tracks > 1 else "NO LOOP")