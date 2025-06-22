import sys
n = int(sys.stdin.readline().strip())
lst = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    lst.append(n)
print(" ".join(str(x) for x in lst))