import sys
n = (int)(sys.stdin.readline())
arr = map((int), sys.stdin.readline().split())
stack = [0]
total = 0
for x in arr:
    if x > stack[0]:
        stack.pop()
        stack.append(x)
    else:
        total += stack[0] - x
print(total)
