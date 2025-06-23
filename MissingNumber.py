import sys
n = int(sys.stdin.readline()) 
total = (n * (n+1)) // 2
for x in map(int, sys.stdin.readline().split()):
    total -= x
print(total)